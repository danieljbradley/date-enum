# date-enum
Provides a table which includes an instance for each month a user ID was active.

# Usage:
```
import pandas as pd
from date_enum import date_filter

test_df = pd.read_csv('data.csv')
test_df_output = date_filter(test_df)
test_df_output.to_csv('output.csv')

>>> date_filter(df)
    ID         POI
0    1  01/01/2018
1    1  02/01/2018
2    1  03/01/2018
3    1  04/01/2018
4    1  05/01/2018
5    1  06/01/2018
6    1  07/01/2018
7    1  08/01/2018
8    1  09/01/2018
9    1  10/01/2018
10   1  11/01/2018
11   1  12/01/2018
12   1  01/01/2019
13   1  02/01/2019
14   1  03/01/2019
15   1  04/01/2019
16   1  05/01/2019
17   1  06/01/2019
18   1  07/01/2019
19   1  08/01/2019
20   1  09/01/2019
21   1  10/01/2019
22   1  11/01/2019
23   1  12/01/2019
24   1  01/01/2020
25   2  03/01/2019
26   2  04/01/2019
27   2  05/01/2019
28   2  06/01/2019
```
