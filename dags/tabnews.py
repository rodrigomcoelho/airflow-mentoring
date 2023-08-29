from datetime import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from internal.resources.operators.tabnews import TabNewsToJSONFileOperator

with DAG(
    dag_id="tabnews",
    start_date=datetime(2023, 8, 1),
    schedule_interval="@daily",
    tags=["tabnews", "ingestion"],
    catchup=False,
    max_active_runs=1,
    default_args={"depends_on_past": False, "owner": "rodrigomcoelho"},
) as dag:
    jobs = {
        "start": EmptyOperator(task_id="start"),
        "stop": EmptyOperator(task_id="stop"),
    }

    jobs["main"] = TabNewsToJSONFileOperator(
        task_id="main_execution",
        tabnews_conn_id="conn_tabnews",
        endpoint="/contents",
        execution_date="{{ ds }}",
        root_directory="/opt/airflow/output",
    )

    jobs["main"].set_downstream(jobs["stop"])
    jobs["main"].set_upstream(jobs["start"])
