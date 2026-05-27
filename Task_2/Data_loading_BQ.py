import os
from nbconvert import export
import pandas as pd
from google.cloud import bigquery
import os
import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logging.info("Starting the BigQuery data loading process")


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/workspaces/Tacheon-tasks/Task_2/key.json"
client = bigquery.Client()
table_id = "single-actor-432513-n6.Weather_data.Temperature"
job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV,
    skip_leading_rows=1,
)
with open("/workspaces/Tacheon-tasks/Task_2/weather_data.csv", "rb") as source_file:
    job = client.load_table_from_file(source_file, table_id, job_config=job_config)
job.result()
logging.info("Data loaded into BigQuery successfully")

