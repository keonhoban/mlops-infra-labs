# ml_code/train_mlflow.py

import mlflow
import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def run_experiment():
    # 실험 세팅
    mlflow.set_tracking_uri("http://mlflow:5000")
    mlflow.set_experiment("iris_experiment")

    with mlflow.start_run() as run:
        # 데이터 준비
        data = load_iris()
        X, y = data.data, data.target

        # 모델 학습
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X, y)
        preds = model.predict(X)

        # 메트릭 계산
        acc = accuracy_score(y, preds)

        # 로깅
        mlflow.log_param("n_estimators", 100)
        mlflow.log_metric("accuracy", acc)
        mlflow.sklearn.log_model(model, artifact_path="model", registered_model_name="IrisModel")
        #mlflow.sklearn.log_model(model, artifact_path="model")

        print(f"✅ Run ID: {run.info.run_id}, Accuracy: {acc}")

if __name__ == "__main__":
    run_experiment()
