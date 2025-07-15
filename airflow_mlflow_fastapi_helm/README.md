# 🧠 MLOps 실무형 인프라 구축 프로젝트

본 프로젝트는 **ML 실험, 모델 관리, 자동화 파이프라인, 실시간 서빙까지**  
실무 환경을 가정하여 **Kubernetes 기반으로 MLOps 인프라 전체를 구축**한 실전 예제입니다.

---

## 📦 구성 요소

| 구성 | 설명 |
|------|------|
| **MLflow** | 모델 실험 및 Registry 관리 (PostgreSQL + S3 연동) |
| **Airflow** | DAG 기반 모델 학습 및 Promotion 자동화 |
| **FastAPI** | MLflow 모델 로딩 기반 실시간 추론 API |
| **Helm Charts** | 각 구성 요소 배포 자동화 |
| **Secrets / Ingress** | 보안 및 서비스 라우팅 구성 |
| **모델 핫스왑** | DAG → MLflow → FastAPI 연동을 통한 실시간 버전 교체 구조 |

---

## 🧰 기술 스택

- Kubernetes (Local Cluster)
- Helm
- Docker
- MLflow 2.13
- Apache Airflow
- FastAPI
- PostgreSQL (external)
- AWS S3 (object storage)
- GitSync (Airflow DAG 연동)
- Custom Docker Image

---

## 🚀 배포 순서 요약

\`\`\`bash
# 예시: MLflow
cd mlflow-helm
helm install mlflow . -n mlflow

# 예시: FastAPI
cd fastapi-helm
helm install fastapi . -n fastapi
\`\`\`

- `kubectl`, `helm`, `docker`, `jq` 설치 필요
- hosts 파일 수정: `fastapi.local`, `mlflow.local` 등 로컬 도메인 접근 설정

---

## ✨ 블로그 시리즈

- 전체 구성 및 설명은 블로그에서 확인할 수 있습니다.  
👉 [🔗 MLOps 구축 여정 시리즈](https://keonhoban.github.io/mlops-journey/projects/mlops_pipeline/helm/)
