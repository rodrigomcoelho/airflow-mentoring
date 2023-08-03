from datetime import datetime
from time import sleep

from airflow import DAG
from airflow.operators.python import PythonOperator



def sleeping() -> None:
    print("Vou dormir por 10 segundos.")
    sleep(10)
    print("Legal, estou acordado.")


def sleeping2() -> None:
    print("Vou dormir por 3 segundos.")
    sleep(3)
    print("Legal, estou acordado.")


with DAG(
    dag_id="demo_002",
    start_date=datetime(2023, 7, 1),
    schedule_interval="@daily",
    default_args={"owner": "rodrigocoelho"},
) as dag:
    start = PythonOperator(task_id="start", python_callable=sleeping)
    stop = PythonOperator(task_id="stop", python_callable=sleeping2)

    start.set_downstream(stop)
