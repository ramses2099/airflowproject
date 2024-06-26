# airflowproject
Apache Airflow Project

### create virtual enviroment
virtualenv env

### active virtual env
source ./env/bin/activate

### check python version
python --version
Python 3.10.12

### Downloda official docker compose Airflow
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.9.2/docker-compose.yaml'

### Create folder and set .env file
mkdir -p ./dags ./logs ./plugins ./config
echo -e "AIRFLOW_UID=$(id -u)" > .env

### Init database 
docker compose up airflow-init

### Create user and password
login: airflow
password: airflow

### runing
docker compose up -d

### What is Airflow?
- Workflow management platform
- Wirtten in Python

### Workflow
- sequence of task

### DAG
- Directed Acyclic Graph
- Dag,Task, Operator

### Operator
- BashOperator
- PythonOperator
- CustomisedOperator

### clear de DAG example
- docker compose down -v
- AIRFLOW__CORE__LOAD_EXAMPLES: 'true' change to false
- docker compose up airflow-init