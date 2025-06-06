# ☸️ MLflow - Tracking + FastAPI 

## ✅ 목표

- **MLflow Tracking Server**를 로컬에서 실행하고 실험 기록을 남기기
- **모델 저장 및 버전 관리**: MLflow 모델 레지스트리 사용
- **FastAPI**와 연동하여 학습된 모델을 **예측 API**로 배포

---

## 📁 구성 파일

| 파일명 | 설명 |
| --- | --- |
| `train.py` | MLflow 실험 실행 및 모델 학습 코드 |
| `mlruns/` | MLflow 실험 데이터 자동 생성 디렉토리 |
| `fastapi_app/app.py` | FastAPI 예측 API 코드 |
| `Dockerfile` | 선택 사항: Docker로 MLflow, FastAPI 배포 |

---

## 🛠️ 실행 명령어

### 1. 가상환경 설정

```bash
# 1. venv 설치 (한 번만)
sudo apt install python3-venv -y

# 2. 가상환경 생성
python3 -m venv .venv

# 3. 가상환경 활성화
source .venv/bin/activate

# 4. 필요한 패키지 설치
pip install --upgrade pip
pip install mlflow scikit-learn pandas fastapi uvicorn

# 5. 실습 종료 후 가상환경 비활성화
deactivate
```

### 2. MLflow UI 실행

```bash
mlflow ui --port 5000
```

→ 브라우저에서 확인: `http://localhost:5000`

### 3. 모델 학습 코드 실행

```bash
python app/train.py
```

### 4. FastAPI 서버 실행

```bash
uvicorn fastapi_app.app:app --reload --port 8000
```

---

## 🔍 확인 방법

### 🔸 FastAPI 예측 API 테스트

```bash
curl -X POST http://localhost:8000/predict \
     -H "Content-Type: application/json" \
     -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
```

→ 예측 결과가 성공적으로 출력되면 성공 ✅

---

## 🧹 리소스 정리

```bash
# 모델을 레지스트리에서 삭제
mlflow.registered_models.delete("iris-rf")

# 실행된 실험 삭제
rm -rf mlruns/
```

---

## 🧩 기타 참고

- **클러스터**: 로컬 Ubuntu 24.04 (VMware)
- **MLflow UI**: `http://localhost:5000`에서 실험 기록 및 모델 관리 가능
- **FastAPI**: `http://localhost:8000/predict`에서 예측 요청 가능

---

## 🌐 프로젝트 흐름

1. **train.py**로 모델 학습
2. **MLflow**를 통해 실험 기록
3. 학습된 모델을 **FastAPI**로 서비스화
