# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 레포지토리 개요

MLOps 인프라 학습 랩 + 프로덕션급 플랫폼 3종을 포함하는 모노레포입니다.

```
mlops-infra-labs/
├── mlops-platform/                  # 기본 플랫폼 (Airflow + MLflow + FastAPI)
├── mlops-platform-triton/           # + Triton Inference Server
├── mlops-platform-feature-store/    # + Feast + Redis + Triton
├── airflow/                         # Airflow 튜토리얼 (5개 랩)
├── k8s-basic/                       # Kubernetes 기초 (5개 랩)
├── mlflow/                          # MLflow 추적 튜토리얼
├── airflow_mlflow_fastapi_dockerCompose/  # Docker Compose 통합 예제
├── airflow_mlflow_fastapi_helm/     # Helm 통합 예제
└── terraform/                       # Terraform IaC 예제
```

## 플랫폼 아키텍처 (3종 공통)

모든 플랫폼은 동일한 디렉토리 구조를 따릅니다:

```
mlops-platform*/
├── apps/           # ArgoCD Application 매니페스트
├── bootstrap/      # ArgoCD + MetalLB 초기 설치 스크립트
├── charts/         # Helm 차트 (airflow, fastapi, mlflow, [triton], [feast])
│   └── <chart>/
│       ├── Chart.yaml
│       ├── image/          # Dockerfile + requirements.txt
│       ├── templates/      # K8s 리소스 템플릿
│       └── values/
│           ├── base.yaml   # 공통 설정
│           ├── dev.yaml    # dev 오버라이드
│           └── prod.yaml   # prod 오버라이드
├── envs/
│   ├── dev/
│   │   ├── certificates/       # cert-manager TLS
│   │   ├── monitoring/         # ServiceMonitor, AlertRules
│   │   ├── observability/      # Loki/Promtail values
│   │   └── sealed-secrets/     # 암호화된 시크릿
│   └── prod/                   # (동일 구조)
└── ops/
    ├── storage/        # NFS PV/PVC 정의 (Retain 정책)
    ├── seal/           # SealedSecret 재암호화 스크립트
    └── rotate/         # AWS 자격증명 회전 스크립트
```

### 플랫폼별 차이

| 플랫폼 | 추가 차트 | 추가 스토리지 |
|---|---|---|
| `mlops-platform` | 없음 | 없음 |
| `mlops-platform-triton` | `charts/triton/` | `ops/storage/triton/` (NFS, Airflow 공유) |
| `mlops-platform-feature-store` | `charts/feast/`, `charts/triton/` | `ops/storage/triton/`, `ops/feature-store/` |

## Docker 베이스 이미지

| 서비스 | 베이스 이미지 | 비고 |
|---|---|---|
| Airflow | `apache/airflow:3.0.2-python3.12` | 3종 공통 |
| MLflow | `ghcr.io/mlflow/mlflow:v2.13.0` | 3종 공통 |
| FastAPI | `python:3.12` | non-root UID/GID 2001 (`fastapiuser`) |
| Triton | `nvcr.io/nvidia/tritonserver:24.08-py3` | triton, feature-store 플랫폼 |
| Feast | `feastdev/feature-server:0.40.1` | feature-store 플랫폼만 |

## FastAPI A/B 테스트 모드

`charts/fastapi/app/services/alias_selector.py` 기반 3가지 트래픽 라우팅 모드:

| 모드 | 환경변수 값 | 동작 |
|---|---|---|
| **A/B Test** | `alias_selection_mode=ab_test` | SHA256 해시 기반 90/10 분할 (A 90%, B 10%) |
| **Canary** | `alias_selection_mode=canary` | `canary_percent`만큼 B로 라우팅, 나머지 A |
| **Blue-Green** | `alias_selection_mode=blue_green` | `default_alias`로 100% 고정 라우팅 |

환경변수: `ALIAS_SELECTION_MODE`, `DEFAULT_ALIAS`, `CANARY_PERCENT`

## ArgoCD ApplicationSet 전략

`apps/appset-env-matrix.yaml`: Matrix generator로 환경(dev/prod) × 서비스(mlflow/airflow/fastapi) 조합 생성.

- **릴리스 네이밍**: `{service}-{env}` (예: `mlflow-dev`, `airflow-prod`)
- **sync wave**: `0` (sealed-secrets) → `1` (서비스)
- **Values 머지 순서**: `values/base.yaml` → `values/{env}.yaml` (dev.yaml/prod.yaml은 base의 최소 delta만 포함)
- Triton, Feast는 별도 Application 매니페스트로 배포 (`triton-dev.yaml`, `feast-dev.yaml` 등)

## CI 검증 명령어

CI 워크플로: `.github/workflows/ci-helm-validate.yaml` (각 플랫폼에 동일하게 존재)

트리거: `charts/`, `envs/`, `apps/` 경로 변경 시 PR에서 실행

### 로컬에서 CI 재현

```bash
# Helm 버전 반드시 3.18.3 사용
helm version  # v3.18.3 확인

# Helm lint (차트별, 환경별) — Values는 반드시 base → env 순서로 머지
cd charts/<chart>
helm lint . -f values/base.yaml -f values/dev.yaml --strict
helm lint . -f values/base.yaml -f values/prod.yaml --strict

# Helm template 렌더링
helm template <chart> charts/<chart> -n <chart>-dev \
  -f charts/<chart>/values/base.yaml -f charts/<chart>/values/dev.yaml

# yamllint (templates, sealed-secrets 제외)
yamllint -s <file.yaml>

# kubeconform (K8s 1.30.0 기준)
kubeconform -kubernetes-version 1.30.0 \
  -ignore-missing-schemas \
  -skip "Application,ApplicationSet,AppProject,SealedSecret,Certificate,CertificateRequest,Issuer,ClusterIssuer,Order,Challenge" \
  -summary <rendered.yaml>
```

### CI 매트릭스

- 환경: `[dev, prod]`
- 차트 (기본): `[airflow, fastapi, mlflow]`
- 추가 차트는 플랫폼에 따라 `triton`, `feast` 포함

## yamllint 규칙 (`.yamllint`)

- `charts/**/templates/**`, `charts/**/charts/**`, `envs/**/sealed-secrets/**` 무시
- braces, line-length, document-start, truthy 비활성화
- trailing-spaces: error, colons max-spaces-after: 1

## 시크릿 관리

- 평문 시크릿은 절대 Git에 커밋하지 않습니다
- 모든 시크릿은 SealedSecrets로 암호화 후 `envs/{env}/sealed-secrets/`에 저장
- 키 회전: `ops/seal/rotate-controller-key.sh` → `ops/seal/re-seal.sh`
- AWS 자격증명 회전: `ops/rotate/rotate-aws-credentials.sh`

## 스토리지 규칙

- PV/PVC는 `ops/storage/` 아래에 env별로 정의
- `persistentVolumeReclaimPolicy: Retain` — ArgoCD prune에서도 데이터 보호
- Triton 모델 저장소는 NFS PVC를 통해 Airflow(쓰기)와 Triton(읽기)이 공유

### 스토리지 클래스 역할

| storageClassName | 용량 | 용도 |
|---|---|---|
| `nfs-monitoring` | 50Gi | Prometheus/Grafana 데이터 영속화 |
| `nfs-observability` | 100Gi (Loki), 5Gi (Triton) | Loki 로그 + Triton 모델 리포지토리 |
| `local-path` | 50Gi | Prometheus TSDB (로컬 노드 스토리지) |

NFS 서버: `192.168.18.141`, 경로 패턴: `/mnt/nfs_share/mlops/{service}/{env}/`

## 관측성 스택

- **kube-prometheus-stack**: `65.5.0` (prometheus-community Helm chart)
- **Grafana**: `11.2.2-security-01`
- **ServiceMonitor 선택**: label `release: monitoring-{env}`로 Prometheus가 대상 선택
- **AlertRule**: 동일 label 패턴 (`release: monitoring-{env}`)

## Feature Store 설계 원칙 (mlops-platform-feature-store)

S3 버저닝 패턴:
- **Version 경로**: `s3://{bucket}/feature-store/user_features/v_YYYY.../` — 재현성용
- **Latest 포인터**: `s3://{bucket}/feature-store/user_features/latest/features.parquet` — Feast offline 소비용
- **실패 격리**: `.failed_<version>` / rollback으로 장애 버전 분리
- **Registry**: `s3://{bucket}/feast/{env}/registry.pb` — 환경별 단일 레지스트리

## 운영 스크립트

| 스크립트 | 용도 |
|---|---|
| `bootstrap/00-argocd-helm-install.sh` | ArgoCD Helm 초기 설치 |
| `ops/ab_test.sh` | A/B 테스트 헬퍼 |
| `ops/seal/re-seal.sh` | SealedSecret 재암호화 |
| `ops/rotate/rotate-aws-credentials.sh` | AWS 자격증명 회전 |

## ArgoCD 동기화 순서

Helm 차트 내부 sync wave: MLflow(10) → Airflow(20) → Triton(30) → FastAPI(40)

ApplicationSet sync wave: sealed-secrets(0) → 서비스(1)

## 주의사항

- kubeconform에서 3rd-party CRD(ArgoCD, cert-manager, SealedSecret)는 `SKIP_KINDS`로 스킵
- Triton은 explicit model-control-mode 사용 — 모델 자동 폴링 없음, API를 통한 명시적 리로드 필요
- dev/prod는 namespace, label, storage, alert rule 모두 완전 분리
