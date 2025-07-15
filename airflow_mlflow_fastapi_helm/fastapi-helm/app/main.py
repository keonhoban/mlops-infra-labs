# app/main.py
# app/main.py
from fastapi import FastAPI, Request
import mlflow.pyfunc
import mlflow
from mlflow.tracking import MlflowClient
import os

app = FastAPI()
model = None
model_info = {}

@app.on_event("startup")
def load_model():
    global model, model_info

    tracking_uri = os.environ.get("MLFLOW_TRACKING_URI")
    model_name = os.environ.get("MODEL_NAME")
    model_stage = os.environ.get("MODEL_STAGE", "Production")

    # MLflow 설정
    mlflow.set_tracking_uri(tracking_uri)
    model_uri = f"models:/{model_name}/{model_stage}"

    # 모델 로딩
    model = mlflow.pyfunc.load_model(model_uri)

    # 모델 버전 정보 확인
    client = MlflowClient()
    latest = client.get_latest_versions(name=model_name, stages=[model_stage])[0]
    run_id = latest.run_id
    version = latest.version

    # 로깅 + 저장
    print(f"✅ Loaded model: name={model_name}, stage={model_stage}, version={version}, run_id={run_id}")
    model_info = {
        "model_name": model_name,
        "stage": model_stage,
        "version": version,
        "run_id": run_id,
        "model_uri": model_uri,
    }

@app.get("/")
def root():
    return {"message": "FastAPI MLOps is running!"}

@app.get("/model-info")
def get_model_info():
    return model_info

@app.post("/predict")
async def predict(request: Request):
    input_data = await request.json()
    prediction = model.predict(input_data)
    return {"prediction": prediction.tolist()}
