# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 09:09:01 2022

@author: Steven
"""

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filename',    help='input filename', default="input.csv")
args = parser.parse_args()

#### Lookup dataframes

# Look ups go here. Needs to be updated
AST_lookup = pd.DataFrame( {'age_group': ['<3wks', '3wks-5y', '6-10y', '11-16y', 
                                      '17-30y', '31-50y', '51-70y', '>70y'],
                        'AST_upper_limit': np.arange(8)*100  }  )

ALT_lookup = pd.DataFrame( {'age_group': ['<3wks', '3wks-5y', '6-10y', '11-16y', 
                                      '17-30y', '31-50y', '51-70y', '>70y'],
                        'ALT_upper_limit': np.arange(8)*100  }  )

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
    df = pd.read_csv(input_filepath, 
                     parse_dates=['DOB', 'sample_date'], 
                     dayfirst = True)  
  
    # Add age in years
    df['age'] = (df.sample_date - df.DOB).dt.days / 365.25
    
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
    df_out = df_out.replace(np.nan, 0)
  
    # Sort columns
    df_out = df_out.reindex(columns=cols)
    
    # Sort rows
    #df_out = df_out.sort_values( by = ['sample_date'])
    
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
    # Merge with lookup so all age groups are present
    # Rest index
    df.insert(0, 'age_group', df.index)
    df.index = np.arange(len(df))
    df = df.merge(AST_lookup['age_group'], how = 'right')   
    df.insert(0, 'count', col_name)
   
    return df


def create_first_AST_ALT_values(df, output_filepath):
    
    df = df.sort_values( by = ['sample_date'])
      
    # AST
    col_name = 'AST_2x_normal'
    
    # Get first elevated AST measurement
    df_elevated = df[df[col_name] == True].groupby(['patient_id'], as_index = False).first()
    df_elevated = df_elevated.drop(['ALT', 'ALT_2x_normal', 'AST_upper_limit', 'ALT_upper_limit'], axis = 1)
    df_elevated = df_elevated.rename(columns={"sample_date": "AST_sample_date",
                                              "month": "AST_sample_month"})
          
    # Remove anyone who has an elevated AST measurement. Get their first AST measurement
    df_normal = df[~df['patient_id'].isin( df_elevated.patient_id.unique() )]
    
    df_normal = df_normal.groupby(['patient_id'], as_index = False).first()
    df_normal = df_normal.drop(['ALT', 'ALT_2x_normal', 'AST_upper_limit', 'ALT_upper_limit'], axis = 1)
    df_normal = df_normal.rename(columns={"sample_date": "AST_sample_date",
                                              "month": "AST_sample_month"})
    
    df_AST = df_elevated.merge(df_normal, how = 'outer')
    
    
    # ALT
    col_name = 'ALT_2x_normal'
    
    # Get first elevated ALT measurement
    df_elevated = df[df[col_name] == True].groupby(['patient_id'], as_index = False).first()
    df_elevated = df_elevated.drop(['AST', 'AST_2x_normal', 'AST_upper_limit', 'ALT_upper_limit'], axis = 1)
    df_elevated = df_elevated.rename(columns={"sample_date": "ALT_sample_date",
                                              "month": "ALT_sample_month"})
          
    # Remove anyone who has an elevated AST measurement. Get their first AST measurement
    df_normal = df[~df['patient_id'].isin( df_elevated.patient_id.unique() )]
    
    df_normal = df_normal.groupby(['patient_id'], as_index = False).first()
    df_normal = df_normal.drop(['AST', 'AST_2x_normal', 'AST_upper_limit', 'ALT_upper_limit'], axis = 1)
    df_normal = df_normal.rename(columns={"sample_date": "ALT_sample_date",
                                              "month": "ALT_sample_month"})
    
    df_ALT = df_elevated.merge(df_normal, how = 'outer')
    
    
    
    df_out = df_AST.merge(df_ALT, how = 'outer')
               
    # Remove identifying columns
    df_out = df_out.drop(['patient_id', 'DOB', 'AST_sample_date', 'age',
                          'ALT_sample_date'], axis = 1)
    
    # reorder columns
    df_out = df_out[ ['age_group', 'AST_sample_month', 'AST', 'AST_2x_normal',
                                   'ALT_sample_month', 'ALT', 'ALT_2x_normal']]
    
    # Save out
    df_out.to_csv(output_filepath, index=False)
    
    return df_out


def create_plots(AST_ALT_counts, output_folderpath):
    '''

    Parameters
    ----------
    AST_ALT_counts : Counts of AST, ALT measurements by age group and month
    
    output_folderpath : Folder where graph pngs will be saved

    Returns
    -------

    '''
          
    # X axis ticks
    x = pd.date_range('2018-01-01','2022-03-01', 
              freq='MS').strftime("%b-%Y").tolist()
            
    for measure in ['AST_all_tests', 'ALT_all_tests', 'AST_2x_normal', 'ALT_2x_normal']:

        df = AST_ALT_counts[ AST_ALT_counts['count'] == measure].reset_index(drop = True)
        
        plt.figure(figsize=(35,20))
        
        for i in range(len(df)):
         
            y = df.loc[i, x]
            
            # plot lines
            plt.plot(x, y, label = df.loc[i, 'age_group'])
        
        plt.xticks(rotation = 320)
        plt.legend()
        plt.title(measure)
        matplotlib.rc('font', size = 15)
        
        plt.savefig(output_folderpath + '/' + measure + '.png')
        
        return
    
  
####  
 
df = pre_process_data(args.filename)

AST_ALT_counts = create_AST_ALT_counts(df, 'summary_table.csv')
first_AST_ALT_values = create_first_AST_ALT_values(df, 'first_AST_ALT_values.csv')


create_plots(AST_ALT_counts, '.')

















