from datetime import datetime, timedelta

from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator


defualt_args ={
    'owner':'ramses2099',
    'retries':5,
    'retry_delay':timedelta(minutes=5)
}


def greet():
    print("Hello World!")


# task manager
with DAG(
    defualt_args = defualt_args,
    dag_id='our_dag_with_python_operator_v01',
    description = 'Our first dag using python operator',
    start_date=datetime(2024, 6, 26, 2),
    schedule_interval = '@daily'
)as dg:
    task1 = PythonOperator(
        task_id = 'greet',
        python_callable=greet
    )
    
    task1