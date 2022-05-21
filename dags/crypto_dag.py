from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

from crypto_etl import ahhhh, main

now=datetime.now()
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2022,5,21,10-5,8,0,0),
    'email': ['walvdev@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(seconds=30)
}

dag = DAG(
    'crypto',
    default_args=default_args,
    description='Get crypto data and save as json file',
    schedule_interval= timedelta(minutes=1),
    tags=['extract']
)


run_etl = PythonOperator(
    task_id='get_crypto_data',
    python_callable=main,
    dag=dag,
)

run_etl