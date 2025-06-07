# 🛠️ Airflow 실습 3단계 - ML 파이프라인 DAG 구성

## ✅ 목표

- Airflow DAG으로 머신러닝 학습 흐름 시뮬레이션
- 데이터 로딩 → 모델 학습 → 모델 저장의 흐름 구성
- XCom을 통해 Task 간 결과 전달

---

## 📁 구성 파일

| 파일명 | 설명 |
| --- | --- |
| ml_simulation.py | DAG 정의 파일 (dags/ 디렉토리에 위치해야 함) |

---

## 🛠️ 실행 명령어

```bash
# DAG 파일 작성
nano dags/ml_simulation.py

# Airflow 웹서버 및 스케줄러 실행 확인
docker-compose up -d
```

---

## 🔧 DAG 코드 구성 요약

- `load_data` → "가상의 데이터 로딩" 메시지 출력 및 경로 반환
- `train_model` → 전달받은 데이터 경로 출력 후 "모델 학습 완료" 메시지 출력
- `save_model` → 전달받은 모델 경로 출력 후 "모델 저장 완료" 메시지 출력

---

## 🔍 확인 방법

---

1. 브라우저에서 Airflow UI 접속 → [http://localhost:8080](http://localhost:8080/)
2. DAG 목록에서 `ml_simulation` ON
3. ▶ 클릭하여 실행
4. 각 Task의 로그 확인 (UI 또는 CLI)

| Task | 로그 메시지 |
| --- | --- |
| load_data | 📥 데이터 로딩 완료 (가상) |
| train_model | 🧪 데이터 경로: /tmp/fake_data.csv  (🚀 모델 학습 완료 (가상)) |
| save_model | 💾 모델 저장 경로: /tmp/fake_model.pkl   (✅ 저장 완료 (가상)) |

---

## 🧹 리소스 정리

- DAG 파일 삭제 시, Airflow에서 DAG 사라짐
- (실제 리소스 없음 – 시뮬레이션용)

---

## 🧩 실무 팁

| 실제 단계 | 구현 방법 |
| --- | --- |
| 데이터 수집 | S3 / DB에서 CSV, Parquet 등 로딩 |
| 모델 학습 | sklearn / PyTorch / XGBoost 등 |
| 결과 저장 | 모델 파일을 Registry / S3로 업로드 |
| 메트릭 공유 | XCom / MLflow 사용하여 전달 |

---

## 🔧 MLOps 실전 연결

- 이 DAG 흐름은 이후 MLflow Tracking, Slack 알림, Kubeflow 연동 등으로 확장 가능
- 실무형 MLOps 파이프라인 자동화의 첫 걸음
