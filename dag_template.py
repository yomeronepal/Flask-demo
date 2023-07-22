from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta


def create_dag(dag_id, user_datetime):
    default_args = {
        "start_date": datetime(2023, 7, 1),
        "retries": 3,
        "retry_delay": timedelta(minutes=5),
    }

    with DAG(
        dag_id=dag_id,
        schedule_interval=None,  # Set the desired scheduling interval
        default_args=default_args,
    ) as dag:
        # Define your tasks here
        start_task = DummyOperator(task_id="start_task")
        end_task = DummyOperator(task_id="end_task")

        start_task >> end_task

    return dag
