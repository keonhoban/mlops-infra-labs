### 🧪 MLOps 통합 실습 프로젝트

이 프로젝트는 **MLflow + Airflow + FastAPI**를 사용하여

ML 모델의 학습, 추적, 프로모션, 배포까지 한 번에 실습할 수 있는 구조입니다.

---

## 📁 프로젝트 구조

```bash
mlops_project/
├── airflow/               🛫 Airflow 설정 및 DAG
│   ├── dags/              └── 학습 DAG (MLflow 연동)
│   ├── Dockerfile.airflow
│   └── requirements.txt
│
├── fastapi/               ⚡ FastAPI 예측 API 서버
│   ├── app/               └── 모델 서빙 main.py
│   ├── Dockerfile.api
│   └── requirements.txt
│
├── ml_code/               🧠 모델 학습 및 프로모션 코드
│   ├── train_mlflow.py    └── 학습 & MLflow 로깅
│   └── promte_mlflow.py   └── 모델 프로모션 (Staging → Production)
│
├── mlflow_store/          🗂️ MLflow 실험 DB & 아티팩트 저장소
│   ├── mlflow.db          └── sqlite 기반 저장소
│   ├── mlruns/            └── 실험 결과 로그
│   ├── artifacts/         └── 모델 파일 저장
│   └── Dockerfile.mlflow  └── MLflow 서버 Dockerfile (옵션)
│
├── docker-compose.yaml    🧩 전체 구성 통합
├── .env                   🔐 민감 정보 (환경 변수)
└── README.md              📝 프로젝트 소개 문서
```

---

## ⚙️ 사용 기술 스택

| 구성 요소 | 기술 |
| --- | --- |
| 모델 추적 | `MLflow` |
| 스케줄링 | `Airflow` |
| 모델 서빙 | `FastAPI`, `Uvicorn` |
| 실험 저장소 | `SQLite`, `Artifacts` |
| 인프라 구성 | `Docker`, `Docker Compose` |

---

## 🚀 실행 방법 (요약)

```bash
# 1. 환경변수 파일 생성
cp .env.example .env

# 2. Docker Compose 실행
docker-compose up --build

# 3. 웹 대시보드 확인
# Airflow: http://localhost:8080
# MLflow : http://localhost:5000
# FastAPI (예측 API): http://localhost:8000
```

---

## 📌 주의사항

- `mlflow_store` 디렉토리는 볼륨으로 마운트되어 **Model Registry & Artifacts가 영속화**됩니다.
- Airflow에서 `MLflow` API 호출 시 `Tracking URI`는 반드시 **컨테이너 간 주소 (`http://mlflow:5000`)** 를 사용해야 합니다.
- `registered_model_name` 등록 시에는 `-serve-artifacts` 옵션이 활성화되어 있어야 합니다.
- MLflow 관련 권한 문제 발생 시, `/mlflow/*` 디렉터리 권한을 확인해주세요.
