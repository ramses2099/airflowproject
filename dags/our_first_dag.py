from datetime import datetime, timedelta

from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner':'ramse2099',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id ='our_first_dag',
    default_args = default_args,
    description ='this is our first dag that we write',
    start_date = datetime(2024,6,25,2),
    schedule_interval='@daily'
)as dag:
    task1 = BashOperator(
        task_id = 'first_task',
        bash_command = 'echo hello world, this is the first task!'
    )
    
    task1

