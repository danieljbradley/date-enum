import pandas as pd
import numpy as np

# Input raw dataset
def date_filter(df):

    df['Start Date'] = pd.to_datetime(
        df['Start Date'],
        infer_datetime_format=True
        )
    df['End Date'] = pd.to_datetime(
        df['End Date'],
        infer_datetime_format=True
        ).replace(to_replace=np.nan, value=np.datetime64('today'))

    def date_range(df):
        return pd.date_range(start=df['Start Date']-pd.DateOffset(months=1),
            end=df['End Date'],
            freq='MS',
            normalize=True
            )

    df['Date Range'] = df.apply(date_range, axis=1)

    list_col = 'Date Range'
    df = pd.DataFrame({
            col:np.repeat(df[col].values, df[list_col].str.len())
            for col in df.columns.drop(list_col)
        }).assign(**{list_col:np.concatenate(df[list_col].values)})[df.columns]

    df['POI'] = df['Date Range'].dt.strftime("%m/%d/%Y")

    df = df[['ID', 'POI']]

    return(df)
