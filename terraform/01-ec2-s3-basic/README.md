# Terraform 실습 - EC2 & S3 생성

## ✅ 개요  
Terraform을 사용하여 AWS 상에 EC2 인스턴스 1개와 S3 버킷 1개를 생성하는 실습입니다.

---

## 📁 파일 구성

- `main.tf`: EC2 & S3 리소스 정의  
- `provider.tf`: AWS Provider 설정  
- `variables.tf`: 입력 변수 정의  
- `terraform.tfvars`: 변수 값 설정  
- `outputs.tf`: 출력값 설정  
- `.gitignore`: 민감 정보 및 상태파일 제외

---

## 🚀 실행 방법

```bash
terraform init
terraform plan
terraform apply
```

---

## 🔐 사전 준비

- AWS CLI 설정 (`aws configure`)  
- `keonho-key` 키페어 생성 (EC2 접속용)  
- 최신 AMI ID를 조회하여 `main.tf`에 반영  
  - 예시: `ami-0e3e8ebc5f90867c0` (Amazon Linux 2)

---

## 🧹 리소스 삭제

```bash
terraform destroy
```

---

## 🪜 향후 확장 계획 (예정)

- 모듈화 및 변수 분리 적용  
- EBS 추가 / VPC 구성 실습  
- EKS 클러스터 구성 실습으로 확장
