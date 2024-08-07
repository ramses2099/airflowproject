from datetime import datetime, timedelta

from airflow.decorators import dag, task
from airflow.providers.postgres.operators.postgres import PostgresOperator


default_args ={
    'owner':'ramses2099',
    'retries':2,
    'retry_delay':timedelta(minutes=1)
}

@dag(default_args = default_args,
    dag_id='our_dag_with_postgree_operator',
    description = 'Our first dag using postgress operator',
    start_date=datetime(2024, 8, 7),
    schedule_interval = '@once',
    catchup = False,
)
def import_data_dbticketsystem_etl():
    task1 = PostgresOperator(
            task_id="create_pet_table",
            postgres_conn_id="postress_connection",
            sql="""
                insert into api_department (name, created, user_id) values ('Business Development', '2023-11-21', 1);
                insert into api_department (name, created, user_id) values ('Product Management', '2023-08-31', 1);
                insert into api_department (name, created, user_id) values ('Accounting', '2023-07-17', 1);
                insert into api_department (name, created, user_id) values ('Human Resources', '2024-05-29', 1);
                insert into api_department (name, created, user_id) values ('Accounting', '2023-11-17', 1);
                insert into api_department (name, created, user_id) values ('Research and Development', '2023-12-03', 1);
                insert into api_department (name, created, user_id) values ('Services', '2023-08-02', 1);
                insert into api_department (name, created, user_id) values ('Business Development', '2024-01-03', 1);
                insert into api_department (name, created, user_id) values ('Research and Development', '2024-05-06', 1);
                insert into api_department (name, created, user_id) values ('Training', '2023-07-27', 1);           
            """,
        )
    task2 = PostgresOperator(
            task_id="drop_pet_table",
            postgres_conn_id="postress_connection",
            sql="""
                drop table if exists public.pet           
            """,
        )
    [task1,task2]
    
import_data_dbticketsystem_etl()