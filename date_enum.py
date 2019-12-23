import pandas as pd
import numpy as np

# Input raw dataset, as well as start and end dates to filter on
# End date defaults to today
def date_filter(df, start_date, end_date=np.datetime64('today', 'D')):

    # Return boolean check on whether a given date lies within the specified range
    def date_check(test_date, start, end):
        if test_date in pd.date_range(start=start, end=end):
            return True
        else:
            return False

    # Vectorize the boolean check to operate on an array
    df_filter = np.vectorize(date_check)
    # Create boolean array on the match start dates
    start_mask = df_filter(df['Start Date'], start_date, end_date)
    # Create boolean array on the match end dates
    end_mask = df_filter(df['End Date'], start_date, end_date)
    # Subset dataframe values where the Start Date OR End Date are within the given range
    df = df[start_mask | end_mask]
    # Return filtered dataframe
    return(df)
