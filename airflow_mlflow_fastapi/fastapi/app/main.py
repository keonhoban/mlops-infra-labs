from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import mlflow.pyfunc
import pandas as pd

app = FastAPI()

# MLflow 모델 로딩 (Production 버전)
mlflow.set_tracking_uri("http://mlflow:5000")
model = mlflow.pyfunc.load_model("models:/IrisModel/Production")

# 🎯 입력 데이터 스키마 정의 (Pydantic)
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get("/")
def home():
    return {"message": "FastAPI + MLflow 예측 API"}

@app.post("/predict")
def predict(data: List[IrisInput]):
    # 입력값을 DataFrame으로 변환
    input_df = pd.DataFrame([item.dict() for item in data])
    
    # 컬럼명을 ML 모델 학습 기준에 맞춰 변환 (필요 시)
    input_df.columns = [
        "sepal length (cm)",
        "sepal width (cm)",
        "petal length (cm)",
        "petal width (cm)"
    ]
    
    preds = model.predict(input_df)
    return {"predictions": preds.tolist()}

#curl -X POST http://localhost:8000/predict \
#  -H "Content-Type: application/json" \
#  -d '[
#    {
#      "sepal_length": 5.1,
#      "sepal_width": 3.5,
#      "petal_length": 1.4,
#      "petal_width": 0.2
#    },
#    {
#      "sepal_length": 6.0,
#      "sepal_width": 2.9,
#      "petal_length": 4.5,
#      "petal_width": 1.5
#    }
#  ]'

