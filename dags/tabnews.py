from airflow import DAG
from datetime import datetime
from airflow.operators.empty import EmptyOperator
from internal.resources.operators.tabnews import TabNewsOperator

with DAG(
    dag_id="tabnews",
    start_date=datetime(2023, 8, 1),
    schedule_interval="@daily",
    tags=["tabnews", "ingestion"],
    catchup=False,
    default_args={
        "depends_on_past": False,
        "owner": "rodrigomcoelho"
    }
) as dag:
    jobs = {
        "start": EmptyOperator(task_id="start"),
        "stop": EmptyOperator(task_id="stop"),
    }

    jobs["main"] = TabNewsOperator(task_id="main_execution")

    jobs["main"].set_downstream(jobs["stop"])
    jobs["main"].set_upstream(jobs["start"])
