"""
What is the count of Congressional members on state by state basis?
Generally groupby() returns a Series obj hence use as_index=False param to turn to Df
"""
from uslegislators import df

print("\nAbt data: ")
print("First 10 rows:  ", df.head(n=10))
print("\nLast 100 rows: ", df.tail(n=100))
print("\nData size: ", df.shape)
print("\nDatatypes: ", df.dtypes)
print("\nColumns: ", df.columns)
print("\nSummary stats: ", df.describe())

# Examine GropBy() method
print(" ")
df_by_state_gender = df.groupby(["state", "gender"], as_index=False, observed=True, sort=True)["last_name"].count()
print(df_by_state_gender)
print(type(df_by_state_gender))

print(" ")
df_by_state = df.groupby("state", as_index=False, observed=True, sort=True)["last_name"].size()
print(df_by_state)
print(type(df_by_state))
