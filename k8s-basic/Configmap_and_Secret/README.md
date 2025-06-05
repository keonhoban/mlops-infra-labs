# ☸️ Kubernetes Basic Lab - ConfigMap & Secret

## ✅ 목표

- Kubernetes에서 **환경설정(ConfigMap)**과 **민감 정보(Secret)**를 안전하게 관리하고 Pod에 주입하는 방법 학습
- 환경 변수 방식으로 주입된 설정이 컨테이너 내부에서 어떻게 반영되는지 실습

---

## 📁 구성 파일

| 파일명 | 설명 |
|--------|------|
| `configmap.yaml` | 일반 설정값 (`APP_MODE`, `APP_PORT`) 정의 |
| `secret.yaml`    | 민감한 값 (`DB_PASSWORD`)을 base64로 인코딩하여 정의 |
| `pod-env.yaml`   | 위의 ConfigMap과 Secret을 환경 변수로 주입한 Pod 정의 |

---

## 🛠️ 실행 명령어

```bash
# 리소스 생성
kubectl apply -f configmap.yaml
kubectl apply -f secret.yaml
kubectl apply -f pod-env.yaml

# 환경 변수 확인
kubectl exec -it env-demo -- sh
env
```

---

## 🔍 확인 결과

```bash
APP_MODE=production
APP_PORT=8080
DB_PASSWORD=supersecret
```

- `env` 명령어를 통해 Pod 내부에 주입된 환경변수 확인 가능
- `ConfigMap`은 평문 설정 관리, `Secret`은 base64로 민감 정보 처리

---

## 🧹 리소스 정리

```bash
kubectl delete -f .
```

---

## 🧩 기타 참고

- 클러스터: Minikube (Docker 드라이버)
- OS: Ubuntu 24.04 (VMware)
- 인코딩 예시:

```bash
echo -n "supersecret" | base64
```
