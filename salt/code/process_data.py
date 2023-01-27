# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 09:09:01 2022

@author: Steven
"""

import os
import argparse
import pandas as pd
import math

scriptpath = os.path.dirname(os.path.realpath(__file__))

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filename', help='input filename', default=os.path.join(scriptpath, "input.csv"))
args = parser.parse_args()

#### Lookup dataframes

# Look ups for upper limit or normal range 
# Just now its 100 in all age groups for AST and ALT
AST_lookup = pd.DataFrame( {'age_group': ['<3wks', '3wks-5y', '6-10y', '11-16y', 
                                      '17-30y', '31-50y', '51-70y', '>70y'],
                        'AST_upper_limit': [200]*8}  )

ALT_lookup = pd.DataFrame( {'age_group': ['<3wks', '3wks-5y', '6-10y', '11-16y', 
                                      '17-30y', '31-50y', '51-70y', '>70y'],
                        'ALT_upper_limit': [200] * 8  }  )

#### Functions

def read_data(input_filepath):
    '''

    Parameters
    ----------
    input_filepath : file path of input.csv

    Returns
    -------
    found_header : Boolean, whether or not heading was succesfully found.
        Only proceed with rest of programme is this is True
    df : If all goes well, this will be a df with appropriate column headers.
        Otherwise it will just be input.csv and the rest of the programme won't run'
    '''
    
    # For testing
    #input_filepath = 'input.csv'
    
    # Read in data
    df = pd.read_csv(input_filepath, na_values = 'NA ', header = None)
 
    # Columns as a set
    set_cols1 = set( ['patient_id', 'DOB', 'sample_date', 'AST', 'ALT'])  
    set_cols2 = set( ['patient_id', 'age', 'sample_date', 'AST', 'ALT'])
 
    # Flag for if header has been found. Initialise as false
    found_header = False   
 
    # Search first 100 rows for header
    i = 0
    while i <= min(100, len(df)-1):
    
         if set_cols1.issubset( set(df.loc[i, :])) or set_cols2.issubset( set(df.loc[i, :])):
             
             df.columns = df.loc[i, :]
             df = df.loc[i+1:, :]
             
             found_header = True
             break
         i += 1
     
    # Move on to the next chunk of code if header is not found in the first 100 rows         
    if not found_header:
        
        print('\nIn order to proceed, input.csv must have columns with the following names: \n \
              \npatient_id, sample_date, AST, ALT, \n \
              \nas well as at least one of \n \
             \nage, DOB. \n \
             \nI have not detected these headings in the first hundred rows of input.csv')
        
        j = 0
        while j <= min(10,  math.ceil( (len(df)-1))/10 ): 
            
            print('\nHere are lines ' + str( 10*j+1) + '-' + str( 10*(j+1)) + ' of input.csv: \n')
            
            print(  df.iloc[ (10*j): 10*(j+1), :]  )
            
            row = input("\nIf you can see the row with column names, please type its row number and press enter. Otherwise, press enter. \n")
            
            try:
                row = int(row)
            except:
                pass

            
            if row in range(10*j, 10*(j+1)):
                    
                print("\nOf the following column headings, which corresponds to patient_id? Type its row number and press enter. \n")
                
                print_df = df.iloc[row, :]
                print_df.index = range(len(print_df))
                print(print_df)
                print('\n')
                
                patient_col_num = input()
                
                try:
                    patient_col_num = int(patient_col_num)
                except:
                    print('\nNon-numeric input. Programme aborted.')
                    break
                
                if not(patient_col_num in range(len(print_df))):
                       print('\n Input not in range. Programme aborted.')
                       break
                


            
                print("\nOf the following column headings, which corresponds to sample_date? Type its row number and press enter. \n")
                
                print_df = df.iloc[row, :]
                print_df.index = range(len(print_df))
                print(print_df)
                print('\n')
                
                sample_col_num = input()
                
                try:
                    sample_col_num = int(sample_col_num)
                except:
                    print('\nNon-numeric input. Programme aborted.')
                    break
                
                if not(sample_col_num in range(len(print_df))):
                       print('\nInput not in range. Programme aborted.')
                       break
                


                    
                print("\nOf the following column headings, which corresponds to AST? Type its row number and press enter. \n")
                
                print_df = df.iloc[row, :]
                print_df.index = range(len(print_df))
                print(print_df)
                print('\n')
                
                ast_col_num = input()
                
                try:
                    ast_col_num = int(ast_col_num)
                except:
                    print('\nNon-numeric input. Programme aborted.')
                    break
                
                if not(ast_col_num in range(len(print_df))):
                       print('\n Input not in range. Programme aborted.')
                       break
                


                print("\nOf the following column headings, which corresponds to ALT? Type its row number and press enter. \n")
                
                print_df = df.iloc[row, :]
                print_df.index = range(len(print_df))
                print(print_df)  
                print('\n')
                
                alt_col_num = input()
                
                try:
                    alt_col_num = int(alt_col_num)
                except:
                    print('\nNon-numeric input. Programme aborted.')
                    break
                
                if not(alt_col_num in range(len(print_df))):
                       print('\nInput not in range. Programme aborted.')
                       break
                


                print("\nOf the following column headings, which corresponds to DOB? Type its row number and press enter. \n \
If none correpond to DOB, press enter \n")
                
                print_df = df.iloc[row, :]
                print_df.index = range(len(print_df))
                print(print_df)
                print('\n')                
                
                dob_col_num = input()
                
                try:
                    dob_col_num = int(dob_col_num)
                except:
                    pass
                
                if dob_col_num in range(len(print_df)):
                    
                    dob_flag = True
                    
                else:
                    dob_flag = False
                    
                    print('\nDOB column header not found.\n')
                    
                    print("\nOf the following column headings, which corresponds to age? Type its row number and press enter." )
                    
                    print_df = df.iloc[row, :]
                    print_df.index = range(len(print_df))
                    print(print_df)
                    print('\n')
                    
                    age_col_num = input()
                    
                    try:
                        age_col_num = int(age_col_num)
                    except:
                        print('\nNon-numeric input. Programme aborted.')
                        break
                    
                    if not(age_col_num in range(len(print_df))):
                           print('\nInput not in range. Programme aborted.')
                           break
                    
                    
                                  
                if dob_flag:    
                    col_numbers = [patient_col_num,
                                   dob_col_num,
                                   sample_col_num, 
                                   ast_col_num,
                                   alt_col_num]
                    
                    if len(col_numbers) > len(set(col_numbers)):
                        
                        print('\nSorry, the column numbers you entered are not all distinct.\n \
                              Please run process_data.py again. \n')
                              
                        break
                              
                    else:
                        df = df.iloc[ (row+1):, col_numbers]
                        df.columns = ['patient_id', 'DOB', 'sample_date', 'AST', 'ALT']
                        
                        found_header = True                         
                        break
                                              
                else:
                    col_numbers = [patient_col_num,
                                   age_col_num,
                                   sample_col_num, 
                                   ast_col_num,
                                   alt_col_num]
                    
                    if len(col_numbers) > len(set(col_numbers)):
                        
                        print('\nSorry, the column numbers you entered are not all distinct.\n \
                              Please run process_data.py again. \n')
                              
                        break
                    
                    else:
                        df = df.iloc[ (row+1):, col_numbers]
                        df.columns = ['patient_id', 'age', 'sample_date', 'AST', 'ALT']
                        
                        found_header = True
                        
                        break               
            j += 1
 
    if found_header:
    
        print('\nColumn headings successfully found! \n')

    else:

        print('\nI have been unable to find suitable column headings. Please run process_data.py and try again, \n \
or edit the column headings of input.csv as required. \n') 
              
    return found_header, df                 


def clean_data(df):
    '''

    Parameters
    ----------
    df : 
    
    Returns
    -------
    df : Cleaned version of df, with additional columns:
        age, age_group, month, AST_upper_limit, ALT_upper_limit, AST_above200, ALT_above200
        
    '''

    # If both AST and ALT are missing, drop the row
    df = df.dropna(subset = ['AST', 'ALT'], how = 'all')
    
    # Convert date columns to datetimes
    df['sample_date'] = pd.to_datetime(df['sample_date'], 
                                       infer_datetime_format=True,
                                       dayfirst = True,
                                       errors = 'coerce')
    
    today = pd.to_datetime("today")
    
    # Get entries that have incorrectly been interpreted with months and days
    # switched
    error_df = df.loc[ (df['sample_date'] > today) & \
                      (df['sample_date'].dt.year == today.year), :] 
    

    # Switch months and days for sample_date entries that are the wrong way round
    error_df.loc[:, ['sample_date'] ] = pd.to_datetime( error_df['sample_date'].dt.strftime('%Y-%d-%m'))
    df.loc[error_df.index, 'sample_date'] = error_df['sample_date']
    
    # Drop any entries that have sample dates in the future
    df = df[ (df['sample_date'] >= '2012-01-01') & (df['sample_date'] <= today) ] 
       
    cols = df.columns
    
    if 'DOB' in cols:
        
        # If any of sample_date, DOB or patient_id are missing, drop the row
        df = df.dropna(subset = ['sample_date', 'DOB', 'patient_id'])
        
        # Keep a copy of the dates column, because entries that don't parse as dates
        # will be coerced to NaT
        df_dates = df[ ['patient_id', 'DOB', 'sample_date'] ]
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
        
        # If their date of birth is after today's date then their year of birth has
        # likely been recorded as two numbers, and pandas interprets that as a date
        # that is post 2000, rather than pre. In that case, subtract 100 off.
        df.loc[ df['DOB'] >=  today, 'DOB']  -= pd.DateOffset(years= 100)
        
        # Add age in years
        df['age'] = (df.sample_date - df.DOB).dt.days / 365.25
        
    elif 'age' in cols:
        # If any of sample_date, DOB or patient_id are missing, drop the row
        df = df.dropna(subset = ['sample_date', 'age', 'patient_id'])
      
    df = clean_numeric_cols(df, ['AST', 'ALT'])
  
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
    df['AST_above200'] = df['AST'] >  df['AST_upper_limit']
    df['ALT_above200'] = df['ALT'] > df['ALT_upper_limit']
       
    return df


def clean_numeric_cols(df, cols):
    '''

    Parameters
    ----------
    df : Dataframe
    cols : list of numeric columns to clean
    
    Returns
    -------
    df : Similar to df, except any numerical columns with '<', '>' 
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

def create_AST_ALT_stats(df, output_filepath):    
    '''

    Parameters
    ----------
    df : Dataframe

    output_filepath : Path of csv file output

    Returns
    -------
    df_out : dataframe with summary statistics by measurement, month and age group

    '''
    
    # Remove any samples that are taken after the first sample that has
    # elevated AST or ALT
    df = df.sort_values(['sample_date'])
      
    # Select all elevated tests
    elevated = df[ df['AST_above200'] | df['ALT_above200'] ]
    
    # Get first elevated test by patient
    first_elevated = elevated[ ~elevated['patient_id'].duplicated()].copy()
    
    # Add a column that is the date of first elevated test, that will 
    # get repated for each patient when joining 
    first_elevated['cutoff'] = first_elevated['sample_date']
             
    df = df.merge(first_elevated[ ['patient_id', 'cutoff'] ], how = 'outer')
      
    # Select all rows where cutoff is null (patient never had an elevated test)
    # or sample date is less than or equal to date of first elevated test
    df = df[ (df['cutoff'].isnull() ) | 
                     (df['sample_date'] <= df['cutoff'] ) ] 
    
    print("Dataframe of first elevated tests constructed")
    
    first_date_in_data = df.sample_date.min()
    last_date_in_data = df.sample_date.max()
              
    # Create dataframe that will be filled out and be the final output
    month_cols = pd.date_range(first_date_in_data, last_date_in_data, 
              freq='M').strftime("%b-%Y").tolist()
    
    if first_date_in_data.month != last_date_in_data.month:
        month_cols = month_cols + [last_date_in_data.strftime("%b-%Y")]
    
    other_cols = ['statistic', 'test', 'age_group'] 
    cols = other_cols + month_cols
    
    df_template = pd.DataFrame(columns=cols)
    df_template[cols] = df_template[cols].astype('float64')
     
    print("Output dataframe template constructed")
    
    # Merge 
    df_sub = sub_process(df, 'AST', False)     
    df_out = df_template.merge(df_sub, how = 'outer')
    
    print("Statistics for all AST tests added")
    
    df_sub = sub_process(df, 'AST', True)    
    df_out = df_out.merge(df_sub, how = 'outer')
    
    print("Statistics for elevated AST tests added")
    
    df_sub = sub_process(df, 'ALT', False)    
    df_out = df_out.merge(df_sub, how = 'outer')
    
    print("Statistics for all ALT tests added")
    
    df_sub = sub_process(df, 'ALT', True)    
    df_out = df_out.merge(df_sub, how = 'outer')
    
    print("Statistics for elevated ALT tests added")
    
    # Sort columns      
    df_out = df_out[cols]
    
    # Set nan for counts equal to zero
    df_out[df_out['statistic'] == 'count'] = df_out[df_out['statistic'] == 'count'].fillna(0)
       
    # Save out
    df_out.to_csv(output_filepath, index=False)  
    
    return df_out

    
def sub_process(df, measure, elevated):
    '''

    Parameters
    ----------
    df : Dataframe
    measure : 'AST' or 'ALT'
    elevated : True or False. If True, counts unique patients who value for 
               measure was at least 200

    Returns
    -------
    df : dataframe with summary statistics for the chosen test, by month and age group

    '''
    
    # Find number of unique patients with an AST measurement.
    # Drop any that have nan
    df = df.dropna(subset = [measure])
    
    if elevated == True:       
        col_name = measure + '_above200'
        
        df = df[ df[col_name] == True ]
        
    else:        
        col_name = measure + '_all_tests'
    

    # Create dataframe of counts
    df_count = df.groupby(['age_group', 'month'])['patient_id'].nunique()
    df_count = df_count.unstack(level=1)
    df_count.columns = df_count.columns.get_level_values('month')  
    df_count.insert(0, 'age_group', df_count.index)
    df_count = df_count.reset_index(drop = True)
    df_count = df_count.merge(AST_lookup['age_group'], how = 'right')   
    df_count.insert(0, 'statistic', 'count')

       
    # Create dataframe of means
    df_mean = df[ ['age_group', 'month', measure]].groupby(['age_group', 'month']).mean()    
    df_mean = df_mean.unstack(level=1)   
    df_mean.columns = df_mean.columns.get_level_values('month') 
    df_mean.insert(0, 'age_group', df_mean.index)
    df_mean = df_mean.reset_index(drop = True)
    df_mean = df_mean.merge(AST_lookup['age_group'], how = 'right')  
    df_mean.insert(0, 'statistic', 'mean')
    
  
    # Create dataframe of variances
    df_var = df[ ['age_group', 'month', measure]].groupby(['age_group', 'month']).var()    
    df_var = df_var.unstack(level=1)   
    df_var.columns = df_var.columns.get_level_values('month')   
    df_var.insert(0, 'age_group', df_var.index)
    df_var = df_var.reset_index(drop = True)
    df_var = df_var.merge(AST_lookup['age_group'], how = 'right')  
    df_var.insert(0, 'statistic', 'var')
    
    # Vertically concatenate
    df = df_count.merge(df_mean, how = 'outer')
    df = df.merge(df_var, how = 'outer')
    df.insert(0, 'test', col_name)
        
    return df


def create_first_AST_ALT_values(df, output_filepath):
    '''

    Parameters
    ----------
    df : Cleaned dataframe
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
    col_name = 'AST_above200'
    
    # Get first elevated AST measurement
    df_elevated = df[df[col_name] == True].groupby(['patient_id'], as_index = False).first()
    df_elevated = df_elevated.drop(['ALT', 'ALT_above200', 'AST_upper_limit', 'ALT_upper_limit'], axis = 1)
        
    # Remove anyone who has an elevated AST measurement. Get their first AST measurement
    df_normal = df[~df['patient_id'].isin( df_elevated.patient_id.unique() )]
    
    df_normal = df_normal.groupby(['patient_id'], as_index = False).first()
    df_normal = df_normal.drop(['ALT', 'ALT_above200', 'AST_upper_limit', 'ALT_upper_limit'], axis = 1)
    
    df_AST = df_elevated.merge(df_normal, how = 'outer').rename(columns={
                                              "month": "AST_sample_month",
                                              "age_group":"AST_age_group"})
    
    df_AST = df_AST[ ['patient_id', 'AST', 'AST_age_group', 'AST_sample_month', 'AST_above200', 'cutoff']]
    
    
    # ALT
    col_name = 'ALT_above200'
    
    # Get first elevated ALT measurement
    df_elevated = df[df[col_name] == True].groupby(['patient_id'], as_index = False).first()
    df_elevated = df_elevated.drop(['AST', 'AST_above200', 'AST_upper_limit', 'ALT_upper_limit'], axis = 1)
          
    # Remove anyone who has an elevated AST measurement. Get their first AST measurement
    df_normal = df[~df['patient_id'].isin( df_elevated.patient_id.unique() )]
    
    df_normal = df_normal.groupby(['patient_id'], as_index = False).first()
    df_normal = df_normal.drop(['AST', 'AST_above200', 'AST_upper_limit', 'ALT_upper_limit'], axis = 1)

    df_ALT = df_elevated.merge(df_normal, how = 'outer').rename(columns={
                                              "month": "ALT_sample_month",
                                              "age_group":"ALT_age_group"})
    
    df_ALT = df_ALT[ ['patient_id', 'ALT', 'ALT_age_group', 'ALT_sample_month', 'ALT_above200', 'cutoff']]
       
    df_out = df_AST.merge(df_ALT, how = 'outer', on = ['patient_id'])
               
    # Remove identifying columns
    df_out = df_out.drop(['patient_id'], axis = 1)
    
    # reorder columns
    df_out = df_out[ ['AST_age_group', 'AST_sample_month', 'AST', 'AST_above200',
                      'ALT_age_group', 'ALT_sample_month', 'ALT', 'ALT_above200']]
    
    # Save out
    df_out.to_csv(output_filepath, index=False)
    
    return df_out


#### Main
 
# Suppress annoying warnings
pd.options.mode.chained_assignment = None

found_header, df = read_data(args.filename)

if found_header:

    try:
        
        print('\n Cleaning data \n')
        
        df = clean_data(df)
        
        print('\n Creating summary table \n')
        
        AST_ALT_stats = create_AST_ALT_stats(df, 'summary_table.csv')
        
        # first_AST_ALT_values = create_first_AST_ALT_values(df, 'first_AST_ALT_values.csv')
     
    except:
        print('\n An error has occurred. Please try again, and if issues persist \n\
send an email to steven.kerr@ed.ac.uk and we will do our best to fix them! \n')
    
    else:
        print('\n Programme finished. \n \
        \n A File titled summary_table.csv has been written to the working directory. \n \
Please check the contents, and then email to us at ccp@ed.ac.uk \n \
\nIf you encounter any issues, please send an email to steven.kerr@ed.ac.uk \n \
and we will do our best to fix them! \n')
              
          
          
          
          
          