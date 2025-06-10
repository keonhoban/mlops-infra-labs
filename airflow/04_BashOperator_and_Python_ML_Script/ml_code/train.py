# airflow/ml_code/train.py

import pickle
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import os

# [1] 로그
print("📥 데이터 로딩 중...")
data = load_iris()
X, y = data.data, data.target

# [2] 학습
print("🧠 모델 학습 중...")
model = RandomForestClassifier()
model.fit(X, y)

# [3] 저장 경로 (컨테이너 기준)
model_path = "/opt/airflow/ml_code/model.pkl"

# [4] 저장
print(f"💾 모델 저장 중... → {model_path}")
with open(model_path, "wb") as f:
    pickle.dump(model, f)

print("✅ 모델 저장 완료!")
