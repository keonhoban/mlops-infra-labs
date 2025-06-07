# 🛠️ Airflow Lab - PythonOperator + BashOperator + XCom

## ✅ 목표

- PythonOperator로 메시지를 생성하고 XCom으로 전달
- XCom을 통해 태스크 간 데이터 전달 확인
- BashOperator를 통한 간단한 쉘 명령 실행
- Graph View와 로그에서 전체 흐름 시각화

---

## 📁 구성 파일

| 파일명 | 설명 |
| --- | --- |
| `python_bash_xcom.py` | DAG 정의 (PythonOperator + XCom + BashOperator) |

---

## 🛠️ 실행 명령어

```bash
# dags/ 디렉토리에 python_bash_xcom.py 추가

# Airflow 웹서버 및 스케줄러 실행 확인
docker compose up -d

# UI 접속
http://localhost:8080

# DAG 트리거 후 그래프 & 로그 확인
```

---

## 🔍 확인 방법

### 🔸 UI에서 확인

1. `python_bash_xcom` DAG ON
2. ▶ 클릭 → Trigger
3. 각 태스크 Graph View 확인
4. Logs 탭에서 다음 메시지 확인:
    - `generate_task`: 🌟 Hello from PythonOperator!
    - `consume_task`: 📬 XCom received message: ...
    - `bash_task`: 🎉 Bash task is running!

---

## 💡 주요 개념 정리

| 개념 | 설명 |
| --- | --- |
| PythonOperator | Python 함수 실행 |
| BashOperator | Bash 명령 실행 |
| XCom | 태스크 간 소규모 데이터 전달 |
| provide_context | XCom 사용을 위한 실행 컨텍스트 제공 |

---

## 🧩 실무 팁

- XCom은 경량 메시지(예: 경로, 상태 코드) 전송에 적합
- 대용량 데이터는 외부 저장소(S3, DB)에 저장하고 경로만 전달

---

## 🔧 MLOps 실전 연결

- 학습 태스크 → 평가 태스크로 모델 ID 전달
- 평가 결과에 따라 등록/서빙 등 분기 처리 가능

---

## 🧹 리소스 정리

```bash
# 필요 시 DAG 파일 삭제
rm dags/python_bash_xcom.py
```

---

## 🧩 기타 참고

- OS: Ubuntu 24.04 (VMware)
- 클러스터: 로컬 Docker 기반 (Minikube 아님)
- 포트: Airflow UI는 기본적으로 8080 사용
- 참고 명령어:

```bash
docker ps
docker-compose logs
```
