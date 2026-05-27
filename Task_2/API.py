import requests
import pandas as pd
import datetime as dt
from datetime import date
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Starting the API data retrieval process")

url = "https://archive-api.open-meteo.com/v1/era5?latitude=52.52&longitude=13.41&start_date=2021-01-01&end_date=2021-12-31&hourly=temperature_2m"

response = requests.get(url)
response.raise_for_status()
logging.info("API request successful")
data = response.json()
#print(data)

hourly = data['hourly']

df=pd.DataFrame(data=hourly)
df["time"] = pd.to_datetime(df["time"])
print(df)

logging.info("Checking null values")
print(df.isnull().sum())

df['date']=df['time'].dt.date
df["year"] = df["time"].dt.year
df["month"] = df["time"].dt.month
df["day"] = df["time"].dt.day
print(df)
print(df.dtypes)

logging.info("Converting temperature from Celsius to Fahrenheit")
df["temperature_f"] = (df["temperature_2m"] * 9/5) + 32
print(df)
print(df.dtypes)

Result = df.to_csv("/workspaces/Tacheon-tasks/Task_2/weather_data.csv", index=False)
logging.info("Data saved to weather_data.csv")