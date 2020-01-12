# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 20:36:18 2019

@author: DB
"""

import pandas as pd
from date_enum import date_filter
#path = 'C:\\Users\\DB\\Documents\\GitHub\\date-enum'

test_df = pd.read_csv('data.csv')
test_df_output = date_filter(test_df)
test_df_output.to_csv('output.csv')
