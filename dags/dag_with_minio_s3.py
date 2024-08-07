from datetime import datetime, timedelta

from airflow.decorators import dag, task
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor

default_args ={
    'owner':'ramses2099',
    'retries':5,
    'retry_delay':timedelta(minutes=5)
}

@dag(default_args = default_args,
    dag_id='our_dag_with_minio_s3',
    description = 'Our first dag using minio s3',
    start_date=datetime(2024, 6, 27, 2),
    schedule_interval = '@daily',
)
def dag_with_minio_etl():
   task1 = S3KeySensor(
       task_id='sensor_minio_s3',
       bucket_name = 'airflow',
       bucket_key='data.cvs',
       aws_con_id='aws_con_id'
   ) 
   
   task1 
    
dag_with_minio_etl()