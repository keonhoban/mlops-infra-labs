# airflow/dags/train_with_mlflow.py

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
sys.path.append("/opt/airflow/ml_code")  # 경로 설정

from train_mlflow import run_experiment  # 학습 함수 import
from promote_mlflow import promote_model # 승격 함수 import

default_args = {
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

with DAG(
    dag_id='train_with_mlflow',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    tags=['ml', 'mlflow'],
) as dag:

    # 모델 학습 + 등록
    train_task = PythonOperator(
        task_id='run_training',
        python_callable=run_experiment,
    )

    # 최신 버전을 Production 스테이지로 Promote
    promote_task = PythonOperator(
        task_id='promote_model_to_production',
        python_callable=promote_model,
    )

    # 작업 순서 정의
    train_task >> promote_task


