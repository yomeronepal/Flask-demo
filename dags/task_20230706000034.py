from airflow import DAG
from airflow.operators.dummy import DummyOperator
from datetime import datetime, timedelta


# def create_dag(dag_id, user_datetime):


# create_dag()


default_args = {
    "start_date": datetime.now() + timedelta(seconds=30),
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="task_20230706000034",
    schedule_interval="@daily",  # Set the desired scheduling interval
    start_date=datetime.now() + timedelta(seconds=30),
    default_args=default_args,
    catchup=True,
    is_paused_upon_creation=False,
) as dag:
    # Define your tasks here
    start_task = DummyOperator(task_id="start_task")
    end_task = DummyOperator(task_id="end_task")

    start_task >> end_task

    # return dag
