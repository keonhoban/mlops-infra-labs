# ☸️ Kubernetes Basic Lab - Ingress + Nginx Controller

## ✅ 목표

- 여러 서비스를 Ingress로 라우팅하여 외부에 노출하는 실습
- `minikube addons enable ingress`를 통해 Nginx Ingress Controller 구성
- `/nginx`, `/httpd` 등 URL 경로 기반으로 서비스 분기 처리 구현

---

## 📁 구성 파일

| 파일명             | 설명                                      |
|--------------------|-------------------------------------------|
| `deploy-nginx.yaml`| nginx Deployment 및 Service 정의          |
| `deploy-httpd.yaml`| httpd Deployment 및 Service 정의          |
| `ingress.yaml`     | 두 서비스에 대한 Ingress 경로 라우팅 정의 |

---

## 🛠️ 실행 명령어

```bash
# Ingress Controller 활성화
minikube addons enable ingress

# 리소스 생성
kubectl apply -f deploy-nginx.yaml
kubectl apply -f deploy-httpd.yaml
kubectl apply -f ingress.yaml

# Ingress 확인
kubectl get ingress
```

---

## 🔍 확인 방법

### 🔸 `/etc/hosts`에 도메인 등록

```bash
sudo nano /etc/hosts
```

```
<minikube ip>   foo.local
```

→ 예: `192.168.49.2   foo.local`

---

### 🔸 curl로 테스트

```bash
curl http://foo.local/nginx
curl http://foo.local/httpd
```

→ 각각 nginx, httpd의 응답이 출력되면 성공 ✅

---

## 🧹 리소스 정리

```bash
kubectl delete -f .
```

---

## 🧩 기타 참고

- 클러스터: Minikube (Docker 드라이버)
- OS: Ubuntu 24.04 (VMware)
- 참고 명령어:
```bash
minikube ip
kubectl describe ingress example-ingress
kubectl get svc
```
