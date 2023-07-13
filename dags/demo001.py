from datetime import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="demo_001",
    start_date=datetime(2023, 7, 1),
    schedule_interval="@once",
    default_args={},
) as dag:
    start = EmptyOperator(task_id="start")
