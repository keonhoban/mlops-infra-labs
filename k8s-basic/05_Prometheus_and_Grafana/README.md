# ☸️ Kubernetes Basic Lab - Prometheus + Grafana Monitoring

## ✅ 목표

- Helm을 사용해 Prometheus, Grafana 설치
- 쿠버네티스 리소스 모니터링 환경 구성
- Grafana UI를 통해 대시보드로 시각화

---

## 📁 구성 파일

| 파일명                  | 설명                                               |
|-------------------------|----------------------------------------------------|
| `values-prometheus.yaml`| Prometheus 설치 시 커스터마이징 값 지정            |
| `values-grafana.yaml`   | Grafana 설치 시 NodePort 및 비밀번호 설정 포함     |

---

## 🛠️ 실행 명령어

```bash
# Helm 저장소 추가
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update

# Prometheus 설치
helm install prometheus prometheus-community/prometheus -f values-prometheus.yaml

# Grafana 설치
helm install grafana grafana/grafana -f values-grafana.yaml
```

---

## 🔍 확인 방법

### 🔸 Prometheus 접속

```bash
minikube ip         # ex) 192.168.49.2
curl http://<minikube-ip>:30091
```

### 🔸 Grafana 접속

```bash
http://<minikube-ip>:30092
```

- ID: `admin`
- PW: `admin1234` *(또는 kubectl get secret ... 명령어로 확인)*

---

## 📊 Grafana 대시보드 구성

1. 좌측 메뉴 → ⚙️ **Data Sources**
   - `Add data source` → Prometheus 선택
   - URL: `http://prometheus-server`

2. 좌측 메뉴 → ➕ **Import**
   - Dashboard ID: `6417` or `315` 입력
   - → 쿠버네티스 리소스 모니터링 대시보드 확인

---

## 🧹 리소스 정리

```bash
helm uninstall prometheus
helm uninstall grafana
```

---

## 🧩 기타 참고

- 클러스터: Minikube (Docker 드라이버)
- OS: Ubuntu 24.04 (VMware)
- 참고 명령어:
```bash
kubectl get svc
kubectl get pods
kubectl get secrets
```
