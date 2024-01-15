# In this script we are using a pandas index to group data using groupby()-->df.index.day_name()
# In case of a pandas series use-->Series_obj.dt.day_name()

import pandas as pd
from datetime import datetime
from air_quality import df

print(df.head(n=10))
print("\n", df.shape)
print("\n", df.dtypes)
print("\n", df.info)
print("\n", df.columns)
print("\n", df.isna().sum())