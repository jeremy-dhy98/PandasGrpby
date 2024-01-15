# Air quality dataset contains hourly readings from a gas sensor device in italy.
# Missing values are denoted as -200 in  the csv file.
# One can use read_csv() to combine two columns into a timestamp while using subset of other cols.

import  pandas as pd
# from datetime import datetime

# dateparse = lambda x : [datetime.strptime(x, "%d/%m/%Y %H:%M:%S")]
df = pd.read_csv("groupby-data/airqual.csv", parse_dates={"date_time": ["Date","Time"]},
                 date_format={"date_time": "%d/%m/%Y %H:%M:%S"},na_values=[-200],
                 usecols=["Date", "Time", "CO(GT)", "T", "RH", "AH"])\
                 .rename(columns={
                           "CO(GT": "co",
                           "T": "temp_c",
                            "RH": "rel_hum",
                            "AH": "abs_hum"})
