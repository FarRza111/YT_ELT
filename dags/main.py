import pendulum
from airflow import DAG
from datetime import datetime, timedelta
from api.video_stats import(
    get_playlist_id,
    get_video_ids,
    extract_video_data,
    save_to_json
)

from datawarehouse.dwh import create_schema, staging_table, core_table
# from airflow.sdk import DAG

local_tz = pendulum.timezone('Europe/Tallinn')

default_args = {
    'owner': 'farrza111',
    'depends_on_past': False,
    'start_date': datetime(2025, 1,1, tzinfo=local_tz),
    'dagrun_timeout': timedelta(hours=1),
    'email': 'data@engineers.com',
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'max_active_runs': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id="produce_json",
    default_args = default_args,
    description = 'Dag to produce JSON file with raw data',
    start_date=datetime(2021, 1, 1),
    schedule="0 14 * * *",
    catchup = False
):
    # Define Tasks
    playlsts_id = get_playlist_id()
    video_ids = get_video_ids(playlsts_id)
    extract_data = extract_video_data(video_ids)
    save_to_json_task = save_to_json(extract_data)
    playlsts_id >> video_ids >> extract_data >> save_to_json_task


with DAG(
    dag_id="update_db",
    default_args = default_args,
    description = 'Dag to process JSON file and insert data both to staging and core schema',
    start_date=datetime(2021, 1, 1),
    schedule="0 15 * * *",
    catchup = False
):
    update_staging = staging_table()
    update_core = core_table()
    
    update_staging >> update_core