from datetime import datetime
from time import sleep
from random import randint

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator



def sleeping(seconds: int, task_name: str) -> None:
    print(f"Olá, sou a task {task_name}")
    print(f"Vou dormir por {seconds} segundos.")
    sleep(seconds)
    print("Estou acordado agora.")


with DAG(
    dag_id="demo_003",
    start_date=datetime(2023, 7, 1),
    schedule_interval="@daily",
    max_active_runs=1,
    default_args={
        "owner": "rodrigo",
        "depends_on_past": True,
    },
    tags=["sleeping", "demo"],
) as dag:

    jobs = {
        "start": EmptyOperator(task_id="start"),
        "stop": EmptyOperator(task_id="stop"),
    }

    for index in range(1, 11):
        task_id = f"task_{str(index).zfill(2)}"

        jobs[task_id] = PythonOperator(
            task_id=task_id,
            python_callable=sleeping,
            op_kwargs={
                "seconds": (index * randint(1, 10)) / 2,
                "task_name": task_id
            }
        )

        jobs[task_id].set_upstream(jobs["start"])
        jobs[task_id].set_downstream(jobs["stop"])
