import mlflow
import mlflow.pyfunc
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

# MLflow URI 설정
mlflow.set_tracking_uri("http://localhost:5000")  # MLflow 서버 URI 설정

# FastAPI 인스턴스 생성
app = FastAPI()

# MLflow 모델 로드
model = mlflow.pyfunc.load_model("models:/iris-rf@production")  # 모델 alias를 이용

# 입력 데이터 구조 정의
class InputData(BaseModel):
    features: list  # 4개의 특성값을 받음

# 예측 API 엔드포인트
@app.post("/predict")
def predict(data: InputData):
    input_df = pd.DataFrame([data.features], columns=["sepal_length", "sepal_width", "petal_length", "petal_width"])
    pred = model.predict(input_df)
    return {"prediction": int(pred[0])}
