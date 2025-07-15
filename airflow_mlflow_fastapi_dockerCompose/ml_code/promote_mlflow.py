from mlflow.tracking import MlflowClient

def promote_model():
    client = MlflowClient()

    # 최신 버전 가져오기
    latest_versions = client.get_latest_versions("IrisModel", stages=["None"])
    if not latest_versions:
        print("❗ 등록된 모델이 없습니다.")
        return

    latest_version = latest_versions[0].version

    # Production으로 전환
    client.transition_model_version_stage(
        name="IrisModel",
        version=latest_version,
        stage="Production"
    )
    print(f"🚀 IrisModel version {latest_version} → Production 등록 완료")
