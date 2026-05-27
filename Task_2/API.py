import requests
import pandas as pd
import datetime as dt
from datetime import date

url = "https://archive-api.open-meteo.com/v1/era5?latitude=52.52&longitude=13.41&start_date=2021-01-01&end_date=2021-12-31&hourly=temperature_2m"

response = requests.get(url)
data = response.json()
#print(data)

hourly = data['hourly']

df=pd.DataFrame(data=hourly)
df["time"] = pd.to_datetime(df["time"])
print(df)

print(df.isnull().sum())
df["date"] = df["time"].dt.date
df["year"] = df["time"].dt.year
df["month"] = df["time"].dt.month
df["day"] = df["time"].dt.day
df["hour"] = df["time"].dt.hour
df["day_name"] = df["time"].dt.day_name()

