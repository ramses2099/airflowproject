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
                CREATE TABLE IF NOT EXISTS pet (
                pet_id SERIAL PRIMARY KEY,
                name VARCHAR NOT NULL,
                pet_type VARCHAR NOT NULL,
                birth_date DATE NOT NULL,
                OWNER VARCHAR NOT NULL);            
            """,
        )
    task2 = PostgresOperator(
            task_id="insert_pet_table",
            postgres_conn_id="postress_connection",
            sql="""
                INSERT INTO pet (name, pet_type, birth_date, OWNER)
                VALUES ( 'Max', 'Dog', '2018-07-05', 'Jane');
                INSERT INTO pet (name, pet_type, birth_date, OWNER)
                VALUES ( 'Susie', 'Cat', '2019-05-01', 'Phil');
                INSERT INTO pet (name, pet_type, birth_date, OWNER)
                VALUES ( 'Lester', 'Hamster', '2020-06-23', 'Lily');
                INSERT INTO pet (name, pet_type, birth_date, OWNER)
                VALUES ( 'Quincy', 'Parrot', '2013-08-11', 'Anne');           
            """,
        )
    [task1,task2]
    
import_data_dbticketsystem_etl()