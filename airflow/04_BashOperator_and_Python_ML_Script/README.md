# ☸️ Airflow Lab - BashOperator로 외부 Python ML 스크립트 실행

## ✅ 목표

- `train.py`를 DAG 외부에서 독립된 스크립트로 실행
- Airflow의 `BashOperator`를 통해 모델 학습 수행
- 학습 결과인 `model.pkl` 파일 생성 여부 및 로그 확인

---

## 📁 디렉토리 구조

```
airflow/
├── dags/
│   └── run_train_script.py     ← Airflow DAG 정의
├── ml_code/
│   ├── train.py                ← ML 학습 스크립트
│   └── model.pkl               ← 학습된 모델 저장 파일 (실행 후 생성)
```

---

## 🛠️ 실행 명령어

```bash
# Airflow 컨테이너 진입
docker exec -it airflow-airflow-webserver-1 bash

# 파일 확인
cd /opt/airflow/ml_code
ls -l
```

> ❗ 컨테이너 이름이 다를 경우 docker ps로 확인해서 수정 필요
> 

---

## 🔍 확인 방법

### 🔸 /opt/airflow/ml_code 경로 내 파일 확인

```bash
ls -l /opt/airflow/ml_code
```

→ `train.py`, `model.pkl`이 보이면 성공 ✅

### 🔸 웹 UI 로그 확인

- DAG: `bash_run_train`
- Task: `run_train_script`
- 로그 내 아래 메시지 확인:
    - 📥 데이터 로딩 중...
    - 🧠 모델 학습 중...
    - 💾 모델 저장 중...
    - ✅ 모델 저장 완료!

---

## 🧹 리소스 정리

```bash
# 필요 시 리소스 정리
docker-compose down
```

---

## 🔧 환경 설정 참고

### 📌 Docker Volume 설정 확인

```yaml
# docker-compose.yaml

services:
  airflow-webserver:
    volumes:
      - ./ml_code:/opt/airflow/ml_code
```

> 위 설정 없을 경우 train.py 실행해도 컨테이너 안에 파일이 없을 수 있음
> 

---

### 📌 scikit-learn 설치 (requirements.txt 방식)

```
# requirements.txt
scikit-learn
```

```
# Dockerfile
FROM apache/airflow:2.8.2

COPY requirements.txt /requirements.txt
USER airflow
RUN pip install --no-cache-dir -r /requirements.txt
```

```bash
# 컨테이너 재빌드
docker-compose down
docker-compose build
docker-compose up -d
```

---

## ✅ 실행 절차 요약

1. `ml_code/train.py` 작성
2. `dags/run_train_script.py` DAG 생성
3. Airflow 웹 UI → DAG 실행
4. 로그와 `/opt/airflow/ml_code/model.pkl`로 결과 확인

---

## 🔎 확인 포인트

| 항목 | 확인 방법 |
| --- | --- |
| 모델 생성 여부 | `ml_code/model.pkl` 파일 존재 확인 |
| 로그 출력 | UI 로그에서 각 단계별 메시지 확인 |

---

## 🧩 실무 팁

| 항목 | 설명 |
| --- | --- |
| BashOperator | `.py`, `.sh` 등 외부 실행파일에 적합 |
| PythonOperator | 내부 Python 로직 직접 실행 시 사용 |
| 실무 응용 흐름 | train → predict → 결과 업로드 등 연속 실행 가능 |

---

## 🔧 MLOps 실전 연결

- 이후에는 이 흐름을 기반으로 다음 단계 연결 가능:
    - **MLflow로 모델 성능 로깅**
    - **S3로 모델 업로드**
    - **SageMaker 배포 자동화**
- 현재 단계는 BashOperator의 **기초 실행 흐름 이해**가 핵심
