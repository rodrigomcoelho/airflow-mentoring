from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago


def show_macro(start_arg_date, end_arg_date) -> None:
    print(f"{start_arg_date=}")
    print(f"{end_arg_date=}")


with DAG(
    dag_id="demo_004",
    start_date=days_ago(10),
    schedule_interval="@daily",
    max_active_runs=1,
    catchup=True,
    default_args={
        "owner": "rodrigo",
        "depends_on_past": True,
    },
    tags=["demo"],
) as dag:
    jobs = {
        "start": EmptyOperator(task_id="start"),
        "stop": EmptyOperator(task_id="stop"),
    }

    jobs["show"] = PythonOperator(
        task_id="show_macro",
        python_callable=show_macro,
        op_kwargs={
            "start_arg_date": "{{ data_interval_start }}",
            "end_arg_date": "{{ data_interval_end  }}",
        },
    )

    jobs["start"] >> jobs["show"] >> jobs["stop"]
