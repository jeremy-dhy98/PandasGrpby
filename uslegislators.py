import pandas as pd

# Turn data types to categorical dtypes for space efficiency by reducing memory load
dtypes = { "first_name": "category",
          "gender": "category",
          "type": "category",
          "state": "category",
          "party": "category"}

df = pd.read_csv("legislators-historical.csv", dtype=dtypes,
                 usecols=list(dtypes) + ["birthday", "last_name"], parse_dates=["birthday"])




