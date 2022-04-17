# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 09:09:01 2022

@author: Steven
"""

import pandas as pd
import argparse


s = pd.Series(['1/1/22'])
pd.to_datetime('1/1/22')


parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filename',    help='input filename', default="input.csv")
args = parser.parse_args()

#### Lookup dataframes

# Look ups for upper limit or normal range 
# Just now its 50 in all age groups for AST and ALT
AST_lookup = pd.DataFrame( {'age_group': ['<3wks', '3wks-5y', '6-10y', '11-16y', 
                                      '17-30y', '31-50y', '51-70y', '>70y'],
                        'AST_upper_limit': [50]*8  }  )

ALT_lookup = pd.DataFrame( {'age_group': ['<3wks', '3wks-5y', '6-10y', '11-16y', 
                                      '17-30y', '31-50y', '51-70y', '>70y'],
                        'ALT_upper_limit': [50]*8  }  )

#### Functions

def pre_process_data(input_filepath):
    '''

    Parameters
    ----------
    input_filepath : Path of csv file input. This csv should have the following column headings:
                     patient_id, DOB, sample_date, AST, ALT
    
    Returns
    -------
    df : Identical to datframe that is read from input_filepath, but with additional columns:
            age, age_group, month, AST_upper_limit, ALT_upper_limit, AST_2x_normal, ALT_2x_normal
        
    '''
    
    # Read in data
    df = pd.read_csv(input_filepath, na_values = 'NA ')
    
    # If both AST and ALT are missing, drop the row
    df = df.dropna(subset = ['AST', 'ALT'], how = 'all')
    
    # If any of sample_date, DOB or patient_id are missing, drop the row
    df = df.dropna(subset = ['sample_date', 'DOB', 'patient_id'])
    
    # Keep a copy of the dates column, because entries that don't parse as dates
    # will be coerced to NaT
    df_dates = df[ ['patient_id', 'DOB', 'sample_date'] ]
    
    # Convert date columns to datetimes
    df['sample_date'] = pd.to_datetime(df['sample_date'], 
                                       infer_datetime_format=True,
                                       dayfirst = True,
                                       errors = 'coerce')
    
    df['DOB'] = pd.to_datetime(df['DOB'], 
                               infer_datetime_format=True,
                               dayfirst = True,
                               errors = 'coerce')

    
    # Get DOB entries that did not convert to datetimes
    error_indices = df.loc[pd.isna(df["DOB"]), :].index
    
    
    # First round of replacements: If dates that didn't parse when part of
    # the entire column do parse when we isolate them, then use these as
    # the DOB
    replacements  = pd.to_datetime( df_dates.loc[error_indices, 'DOB'],
                         infer_datetime_format=True,
                         dayfirst = True,
                         errors = 'coerce').dropna()
    
    for i in replacements.index:
        
        df.loc[i, 'DOB'] = replacements[i]
                         
    # Second round of replacements: If DOB does not parse as a date, but is numeric between 0 and 120,
    # assume it is their age
    replacements = pd.to_numeric(df_dates.loc[error_indices, 'DOB'], errors='coerce').dropna()
    
    are_numeric = [x&y for (x,y) in zip(replacements > 0, replacements < 120)]
    
    replacements = replacements[are_numeric] 
  
    for i in replacements.index:
        
        df.loc[i, 'DOB'] = df.loc[i, 'sample_date'] - pd.DateOffset(years= replacements[i])
                       
    # Drop any entries that are still missing in DOB
    df = df.dropna(subset = ['DOB']) 
    
    # If their date of birth is after March 2022, then their year of birth has
    # likely been recorded as two numbers, and pandas interprets that as a date
    # that is post 2000, rather than pre. In that case, subtract 100 off.
    df.loc[ df['DOB'] >=  pd.to_datetime('1/4/2022'), 'DOB']  -= pd.DateOffset(years= 100)
    
    
    df = clean_numeric_cols(df, ['AST', 'ALT'])

    # Add age in years
    df['age'] = (df.sample_date - df.DOB).dt.days / 365.25
    
    # Drop any values of age <0 or > 120
    df = df[ (df['age'] > 0) & (df['age'] < 120) ]
   
    # Add age group       
    df['age_group'] = pd.cut( df['age'], 
                              bins = [0, 21/365.25, 5, 10, 16, 30, 50, 70, 120],
                              labels = ['<3wks', '3wks-5y', '6-10y', '11-16y', 
                                '17-30y', '31-50y', '51-70y', '>70y'])
    
    # Add month
    df['month'] = df['sample_date'].dt.strftime('%b-%Y')
    
    # Add threshold values for AST, ALT
    df = df.merge(AST_lookup, how = 'left')
    df = df.merge(ALT_lookup, how = 'left')
    
    # Add flags for above threshold value
    df['AST_2x_normal'] = df['AST'] > 2* df['AST_upper_limit']
    df['ALT_2x_normal'] = df['ALT'] > 2* df['ALT_upper_limit']
        
    return df


def clean_numeric_cols(df, cols):
    '''

    Parameters
    ----------
    df : Semi-processed dataframe
    cols : list of numeri columns to clean
    
    Returns
    -------
    df : Identical to df, except any numerical columns with '<', '>' 
        have them removed
        
    '''
    
    # Keep a copy of the dates column, because entries that don't parse as dates
    # will be coerced to NaT
    df_numeric = df[['patient_id'] + cols ]

    for col in cols:

        # Coerce column to numeric
        df[col] = pd.to_numeric(df[col], errors = 'coerce')
            
        # Get entries that did not convert to numeric, that weren't nan to begin with
        error_indices = df.index[ [x&y for (x,y) in zip(pd.isna(df[col]) , ~pd.isna(df_numeric[col]) )] ]
        
        # Coerce to string, replace '>' and '<' with '', coerce back to numeric,
        # and drop any that fail to coerce back to numeric
        replacements = df_numeric.loc[error_indices, col].astype(str)
        replacements = replacements.str.replace('>', '')
        replacements = replacements.str.replace('<', '')
        
        replacements = pd.to_numeric(replacements, errors='coerce').dropna()
            
        df.loc[replacements.index, col] = replacements
            
    return df


def create_AST_ALT_counts(df, output_filepath):    
    '''

    Parameters
    ----------
    df : Path of csv file input. This csv should have the following column headings:
                     patient_id, DOB, sample_date, AST, ALT, age, age_group, month

    output_filepath : Path of csv file output

    Returns
    -------
    df_out : dataframe with counts of unique patients by measurement, month and age group

    '''
    
    # Remove any samples that are taken after the first sample that has
    # elevated AST or ALT
    df = df.sort_values(['sample_date'])
      
    # Select all elevated tests
    elevated = df[ df['AST_2x_normal'] | df['ALT_2x_normal'] ]
    
    # Get first elevated test by patient
    first_elevated = elevated[ ~elevated['patient_id'].duplicated()]
    
    # Add a column that is the date of first elevated test, that will 
    # get repated for each patient when joining
    first_elevated.loc[:, 'cutoff'] = first_elevated['sample_date']
           
    df = df.merge(first_elevated[ ['patient_id', 'cutoff'] ], how = 'outer')
    
    # Select all rows where cutoff is null (patient never had an elevated test)
    # or sample date is less than or equal to date of first elevated test
    df = df[ (df['cutoff'].isnull() ) | 
                     (df['sample_date'] <= df['cutoff'] ) ] 
    
    
         
    # Create dataframe that will be filled out and be the final output
    cols = ['count', 'age_group'] + pd.date_range('2018-01-01','2022-03-01', 
              freq='MS').strftime("%b-%Y").tolist()
    
    df_out = pd.DataFrame(columns=cols)
     
    # Merge 
    df_sub = sub_process(df, 'AST', False)    
    df_out = df_out.merge(df_sub, how = 'outer')
    
    df_sub = sub_process(df, 'AST', True)    
    df_out = df_out.merge(df_sub, how = 'outer')
    
    df_sub = sub_process(df, 'ALT', False)    
    df_out = df_out.merge(df_sub, how = 'outer')
    
    df_sub = sub_process(df, 'ALT', True)    
    df_out = df_out.merge(df_sub, how = 'outer')
    
    # All nan are zero counts
    df_out = df_out.fillna(0)
  
    # Sort columns
    df_out = df_out.reindex(columns=cols)
        
    # Save out
    df_out.to_csv(output_filepath, index=False)  
    
    return df_out

    
def sub_process(df, measure, elevated):
    '''

    Parameters
    ----------
    df : Semi-processed dataframe
    measure : 'AST' or 'ALT'
    elevated : True or False. If True, counts unique patients who value for 
               measure was at least 2x the upper limit

    Returns
    -------
    df : dataframe with counts for the chosen measure, by month and age group

    '''
    
    # Find number of unique patients with an AST measurement.
    # Drop any that have nan
    df = df.dropna(subset = [measure])
    
    if elevated == True:       
        col_name = measure + '_2x_normal'
        
        df = df[ df[col_name] == True ]
        
    else:        
        col_name = measure + '_all_tests'
    
    # Count unique patient ids, grouped by age_group and month
    df = df.groupby(['age_group', 'month'])['patient_id'].nunique()
    
    # Turn multi-index series into a dataframe
    df = df.unstack(level=1)
    
    # Get rid of redundant column multi-index
    df.columns = df.columns.get_level_values('month')
    
    # Insert age group and name of variable being counted
    # Reset index
    # Merge with lookup so all age groups are present
    df.insert(0, 'age_group', df.index)
    df = df.reset_index(drop = True)
    df = df.merge(AST_lookup['age_group'], how = 'right')   
    df.insert(0, 'count', col_name)
   
    return df


def create_first_AST_ALT_values(df, output_filepath):
    '''

    Parameters
    ----------
    df : df : Semi-processed dataframe
    output_filepath : Path of csv file output
    
    Returns
    -------
    df_out : Dataframe with one row per person. If they have any elevated
            AST measurement, the row contains information recorded at the date
            of their first elevated measurement. Similarly for ALT. 
            If they do not have an elevated AST (ALT) measurement, then the row
            contains information recorded at their first AST (ALT measurement)

    '''
          
    df = df.sort_values( by = ['sample_date'])
      
    # AST
    col_name = 'AST_2x_normal'
    
    # Get first elevated AST measurement
    df_elevated = df[df[col_name] == True].groupby(['patient_id'], as_index = False).first()
    df_elevated = df_elevated.drop(['ALT', 'ALT_2x_normal', 'AST_upper_limit', 'ALT_upper_limit'], axis = 1)
        
    # Remove anyone who has an elevated AST measurement. Get their first AST measurement
    df_normal = df[~df['patient_id'].isin( df_elevated.patient_id.unique() )]
    
    df_normal = df_normal.groupby(['patient_id'], as_index = False).first()
    df_normal = df_normal.drop(['ALT', 'ALT_2x_normal', 'AST_upper_limit', 'ALT_upper_limit'], axis = 1)
    
    df_AST = df_elevated.merge(df_normal, how = 'outer').rename(columns={
                                              "month": "AST_sample_month",
                                              "age_group":"AST_age_group"}).drop(['sample_date', 'age', 'DOB'], axis = 1)
    
    
    # ALT
    col_name = 'ALT_2x_normal'
    
    # Get first elevated ALT measurement
    df_elevated = df[df[col_name] == True].groupby(['patient_id'], as_index = False).first()
    df_elevated = df_elevated.drop(['AST', 'AST_2x_normal', 'AST_upper_limit', 'ALT_upper_limit'], axis = 1)
          
    # Remove anyone who has an elevated AST measurement. Get their first AST measurement
    df_normal = df[~df['patient_id'].isin( df_elevated.patient_id.unique() )]
    
    df_normal = df_normal.groupby(['patient_id'], as_index = False).first()
    df_normal = df_normal.drop(['AST', 'AST_2x_normal', 'AST_upper_limit', 'ALT_upper_limit'], axis = 1)

    df_ALT = df_elevated.merge(df_normal, how = 'outer').rename(columns={
                                              "month": "ALT_sample_month",
                                              "age_group":"ALT_age_group"}).drop(['sample_date','age', 'DOB'], axis = 1)
       
    df_out = df_AST.merge(df_ALT, how = 'outer', on = ['patient_id'])
               
    # Remove identifying columns
    df_out = df_out.drop(['patient_id'], axis = 1)
    
    # reorder columns
    df_out = df_out[ ['AST_age_group', 'AST_sample_month', 'AST', 'AST_2x_normal',
                      'ALT_age_group', 'ALT_sample_month', 'ALT', 'ALT_2x_normal']]
    
    # Save out
    df_out.to_csv(output_filepath, index=False)
    
    return df_out
 
#### Main
 
df = pre_process_data(args.filename)

AST_ALT_counts = create_AST_ALT_counts(df, 'summary_table.csv')

#first_AST_ALT_values = create_first_AST_ALT_values(df, 'first_AST_ALT_values.csv')
 
