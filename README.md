# date-enum
Subsets a dataframe on rows which overlap a given date range.

# Usage:
```
from date_enum import date_filter
test_df = pd.read_csv('data.csv')
test_df_filtered = date_filter(
  test_df,
  start_date='3/6/2016',
  end_date='5/9/2016'
)

>>> test_df_filtered.groupby('Race').count()
                 ID  Start Date  End Date  Gender  Zip  Age
Race
Asian             4           4         3       4    4    4
Black            12          12         2      12   12   12
Hispanic          9           9         5       9    9    9
Multi-race        6           6         3       6    6    6
Some Other Race   8           8         2       8    8    8
White             6           6         4       6    6    6

>>> test_df_filtered.groupby('Gender').count()
ID  Start Date  End Date  Zip  Age  Race
Gender
Female  15          15         6   15   15    15
Male    30          30        13   30   30    30

```
