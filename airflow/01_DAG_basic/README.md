# ☁️ Airflow Basic Lab - Docker 기반 로컬 실행

## ✅ 목표

- Docker 기반 로컬 환경에서 Airflow 설치 및 실행
- 기본 DAG 작성 후 Web UI에서 실행 확인

---

## 🧭 전체 흐름

```
[1단계] Docker & Docker Compose 설치 확인
[2단계] 공식 Airflow Docker 예제 다운로드
[3단계] docker compose 실행하여 Airflow 서비스 구동
[4단계] Web UI 접속 및 샘플 DAG 실행
```

---

## 📁 구성 파일

| 파일명 | 설명 |
| --- | --- |
| docker-compose.yaml | Airflow 관련 서비스 정의 (webserver, scheduler 등) |
| dags/hello_airflow.py | 샘플 DAG 예제 파일 |
| .env | 사용자 권한 관련 환경 변수 (AIRFLOW_UID 등) |

---

## 🛠️ 실행 명령어

```bash
# 공식 Docker Compose 예제 다운로드
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.8.2/docker-compose.yaml'

# 작업 디렉토리 생성
mkdir -p ./dags ./logs ./plugins

# 사용자 권한 변수 설정
echo -e "AIRFLOW_UID=$(id -u)" > .env

# 컨테이너 실행
docker-compose up -d
```

---

## 🔍 확인 방법

### 🔸 Web UI 접속

- 브라우저에서 접속: [http://localhost:8080](http://localhost:8080/)
- 기본 로그인 계정:
    - ID: `airflow`
    - PW: `airflow`

---

### 🔸 샘플 DAG 등록

```python
# 파일명: dags/hello_airflow.py

from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(dag_id="hello_airflow", 
         start_date=datetime(2023, 1, 1),
         schedule_interval="@daily",
         catchup=False) as dag:
    
    t1 = BashOperator(
        task_id="print_date",
        bash_command="date"
    )

    t2 = BashOperator(
        task_id="say_hello",
        bash_command="echo 'Hello, Airflow!'"
    )

    t1 >> t2
```

---

## 📈 DAG 실행 확인

1. Airflow UI → 왼쪽 메뉴에서 `hello_airflow` DAG 활성화
2. 실행 버튼 클릭 → 실행 확인
3. 로그 확인: Graph View 또는 Tree View 탭

---

## 🧹 리소스 정리

```bash
docker-compose down --volumes --remove-orphans
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
