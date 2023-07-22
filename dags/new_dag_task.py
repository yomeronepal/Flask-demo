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
    dag_id="new_dag_task",
    schedule_interval=None,  # Set the desired scheduling interval
    start_date=datetime.now() + timedelta(seconds=30),
    default_args=default_args,
    catchup=True,
    is_paused_upon_creation=False,
) as dag:
    # Define your tasks here
    start_task = DummyOperator(task_id="task_1")
    end_task = DummyOperator(task_id="task_2")

    start_task >> end_task

    # return dag
