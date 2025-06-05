# ☸️ Kubernetes Basic Lab - Nginx Deployment & Service

## ✅ 목표

- Minikube 환경에서 Kubernetes 리소스 실습
- Nginx 웹 서버를 Deployment로 배포하고 NodePort로 노출

## 📁 구성 파일

| 파일명 | 설명 |
|--------|------|
| `nginx-deployment.yaml` | Nginx Pod 2개를 생성하는 Deployment 정의 |
| `nginx-service.yaml`    | 외부에서 접근 가능한 NodePort 서비스 정의 |

## 🛠️ 실행 명령어

```bash
# 리소스 생성
kubectl apply -f nginx-deployment.yaml
kubectl apply -f nginx-service.yaml

# 배포 상태 확인
kubectl get all

# 서비스 접속 (로컬 브라우저 or curl)
minikube service nginx-service
curl $(minikube ip):30080
```

## 🔍 확인 결과
- Nginx welcome 페이지 출력 성공
- kubectl logs, kubectl exec로 Pod 접근 가능

## 🧹 리소스 정리

```bash
kubectl delete -f .
```

## 🧩 기타 참고
- 클러스터: Minikube (Docker 드라이버)
- OS: Ubuntu 24.04 (VMware)
