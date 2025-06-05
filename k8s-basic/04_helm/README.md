# ☸️ Kubernetes Basic Lab - Helm 기초 실습

## ✅ 목표

- Helm을 사용하여 Kubernetes 리소스를 간편하게 배포하는 흐름 학습
- Nginx 웹 서버를 Helm Chart로 설치
- 기본 설정 → values.yaml 수정 → Helm 재배포까지 실습

---

## 📁 구성 파일

| 파일명              | 설명                                      |
|---------------------|-------------------------------------------|
| `values-nginx.yaml` | Nginx NodePort 서비스 커스터마이징 설정   |

---

## 🛠️ 실행 명령어

```
# Helm 설치
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

# 저장소 추가 및 업데이트
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update

# 차트 검색
helm search repo nginx

# 기본 설치
helm install my-nginx bitnami/nginx

# 커스터마이징 설치
helm uninstall my-nginx
helm install my-nginx bitnami/nginx -f values-nginx.yaml
```

---

## 🔍 확인 방법

```
kubectl get all
minikube ip
curl http://<minikube-ip>:30090
```

→ Nginx welcome 페이지가 뜨면 성공 ✅

---

## 📑 values-nginx.yaml 예시

```
service:
  type: NodePort
  nodePorts:
    http: 30090
```

---

## 🧹 리소스 정리

```
helm uninstall my-nginx
```

---

## 🧩 기타 참고

- 클러스터: Minikube (Docker 드라이버)
- OS: Ubuntu 24.04 (VMware)
- 참고 명령어:

```
helm list
helm get all my-nginx
helm upgrade my-nginx bitnami/nginx -f values-nginx.yaml
```

