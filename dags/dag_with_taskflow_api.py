from datetime import datetime, timedelta

from airflow.decorators import dag, task

default_args ={
    'owner':'ramses2099',
    'retries':5,
    'retry_delay':timedelta(minutes=5)
}

@dag(default_args = default_args,
    dag_id='our_dag_with_taskflow_api_v01',
    description = 'Our first dag using taskflow',
    start_date=datetime(2024, 6, 26, 2),
    schedule_interval = '@daily')
def hello_world_etl():
    
    @task()
    def get_name():
        return "Juan Perez"
    
    @task()
    def get_age():
        return 45
    
    @task()
    def greet(name, age):
        print(f"Hello World! My name is {name} and I am {age} years old ")
    
    name = get_name()
    age = get_age()
    greet(name=name, age=age)
    
greet_dag = hello_world_etl()