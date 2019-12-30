# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 20:36:18 2019

@author: DB
"""

import pandas as pd

#path = 'C:\\Users\\DB\\Documents\\GitHub\\date-enum'

from date_enum import date_filter
test_df = pd.read_csv('data.csv')
test_df_filtered = date_filter(
  test_df,
  start_date='1/1/2017',
  end_date='12/31/2020'
  )

test_df_filtered.head()

test_df_filtered.to_csv('output.csv')