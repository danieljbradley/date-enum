# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 11:51:07 2019

@author: DBradley
"""

import pandas as pd
import datetime as dt
        
path = 'C:\\Users\\DBradley\\OneDrive - Big Brothers Big Sisters Independence '
path = path + 'Region\\Python\\date-enum\\'
filename = 'data.csv'

parse_dates = ['Start Date', 'End Date']

df = pd.read_csv(path+filename,
                 #encoding = 'ISO-8859-1', 
                 parse_dates=parse_dates)

df['End Date'] = df['End Date'].fillna(dt.date.today())

# BONM means 'beginning of next month' 
# date_range will only count full months, so I need to artificially extend 
# date range to so that upper bound is included
df['End Date_BONM'] = (df['End Date'] + pd.offsets.MonthBegin(n=1))

########################################
# generate active months for each match
df.reset_index(drop=True, inplace=True)

for i in df.index:
    if i != 0: # append dates for subsequent rows onto df created in 'else'
        # generate sequence of months
        # during our meeting, I said that the enumerated date was the first 
        # of the month.  I was mistaken - it is the last of the month
        dt_range = pd.date_range(df['Start Date'].iloc[i],
                                 df['End Date_BONM'].iloc[i],
                                 freq='M')
        # count number of months (for creating series of repeated index)
        dt_range_size = dt_range.size
        # convert index to pandas series that will be repeated for each month
        idx = pd.Series(i)
        idx_repeated = idx.repeat(dt_range_size)
        dt_active_temp = pd.DataFrame(dt_range, index=idx_repeated)
        dt_active = pd.concat([dt_active, dt_active_temp], axis=0)
        
    else: # start dataframe for first row
        # generate sequence of months
        dt_range = pd.date_range(df['Start Date'].iloc[i],
                                 df['End Date_BONM'].iloc[i],
                                 freq='M')
        # count number of months (for creating series of repeated index)
        dt_range_size = dt_range.size
        # convert index to pandas series that will be repeated for each month
        idx = pd.Series(i)
        idx_repeated = idx.repeat(dt_range_size)
        dt_active = pd.DataFrame(dt_range, index=idx_repeated)

# rename month column
dt_active = dt_active.rename(columns={0:'active_month'})
#######################
# merge active months with mf_grouped
df_bymonth = pd.merge(dt_active, df, left_index=True, right_index=True)

#df_bymonth.to_csv(path + 'df_bymonth.csv',encoding='latin1')
df_bymonth.to_csv(path + 'df_bymonth.csv')
