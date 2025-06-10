# ☸️ Airflow + MLflow 연동 실습

## ✅ 목표

- **Airflow**에서 **PythonOperator**를 통해 MLflow 실험 자동화
- 모델의 **파라미터**, **메트릭**, **모델**을 **MLflow**로 자동 기록

---

## 📁 프로젝트 구조

```
airflow/
├── dags/
│   ├── train_with_mlflow.py        ← Airflow DAG 정의 파일
├── ml_code/
│   ├── train_mlflow.py             ← MLflow 연동 학습 스크립트
└── mlruns/                         ← MLflow 로깅 결과 저장 폴더
```

---

## 🛠️ 실행 방법

### 1. **Airflow 환경 설정**

- `train_with_mlflow.py` 파일을 Airflow DAG로 등록
- **Airflow UI**에서 DAG 실행 후 로그를 확인

### 2. **MLflow 로깅 확인**

- `/opt/airflow/mlruns/` 폴더 내에 실험 결과가 기록

---

## 🧪 확인 방법

### 🔸 실행 결과 확인

- **MLflow 로그**: `/opt/airflow/mlruns/` 하위에 `experiment_id/run_id/metrics/params/` 등을 확인합니다.
- **정확도 로그**: DAG 로그에서 `acc = ...` 출력 확인

---

## 🔧 문제 해결

### ❓ 만약 모듈 에러가 발생하면?

1. `docker-compose.yaml`에서 `ml_code` 디렉토리 마운트 확인:
    
    ```yaml
    volumes:
      - ./ml_code:/opt/airflow/ml_code
    ```
    
2. `docker-compose restart`로 컨테이너 재시작 후 정상 반영

---

## 🧩 실무 팁

| 항목 | 설명 |
| --- | --- |
| **mlruns 디렉토리** | MLflow가 자동으로 실험 결과를 기록하는 저장소 |
| **추가 확장** | `train.py`, `predict.py`, `evaluate.py` 등 파일을 Airflow DAG로 연계하여 관리 가능 |
| **MLflow Registry** | 모델을 **레지스트리에 등록** → **자동 배포** 흐름으로 확장 가능 |

---

## 🔧 MLOps 실전 연결

- **Airflow DAG** + **MLflow Tracking**을 활용한 **실험 자동화 파이프라인 구축**
- 추후 **MLflow Registry** + **Model Serving** + **SageMaker 연계**
