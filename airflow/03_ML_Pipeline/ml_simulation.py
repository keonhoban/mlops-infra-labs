# dags/ml_simulation.py

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os

def load_data():
    print("📥 데이터 로딩 완료 (가상)")
    return {"data_path": "/tmp/fake_data.csv"}

def train_model(**context):
    data = context['ti'].xcom_pull(task_ids='load_data')
    print(f"🧪 데이터 경로: {data['data_path']}")
    print("🚀 모델 학습 완료 (가상)")
    return {"model_path": "/tmp/fake_model.pkl"}

def save_model(**context):
    model = context['ti'].xcom_pull(task_ids='train_model')
    print(f"💾 모델 저장 경로: {model['model_path']}")
    print("✅ 저장 완료 (가상)")

with DAG(
    dag_id='ml_simulation',
    start_date=datetime(2023, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:

    t1 = PythonOperator(
        task_id='load_data',
        python_callable=load_data
    )

    t2 = PythonOperator(
        task_id='train_model',
        python_callable=train_model,
        provide_context=True
    )

    t3 = PythonOperator(
        task_id='save_model',
        python_callable=save_model,
        provide_context=True
    )

    t1 >> t2 >> t3
