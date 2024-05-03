from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime

# Define default arguments
default_args = {
    'owner': 'you',
    'start_date': datetime(2024, 5, 1),
    'retries': 1
}

# Instantiate the DAG object
dag = DAG(
    'first_dag',
    default_args=default_args,
    description='My First DAG',
    schedule_interval='@daily',
)

# Define tasks
start_task = DummyOperator(task_id='start_task', dag=dag)
end_task = DummyOperator(task_id='end_task', dag=dag)

# Define task dependencies
start_task >> end_task
