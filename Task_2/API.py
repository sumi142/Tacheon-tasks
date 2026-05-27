import requests
import pandas as pd

url = "https://archive-api.open-meteo.com/v1/era5?latitude=52.52&longitude=13.41&start_date=2021-01-01&end_date=2021-12-31&hourly=temperature_2m"

response = requests.get(url)
data = response.json()
#print(data)


df=pd.DataFrame(data['hourly']['temperature_2m'], columns=['temperature_2m'])
print(df)