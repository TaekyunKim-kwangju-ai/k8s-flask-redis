# 프로젝트 제목

이 프로젝트는 간단한 Flask 애플리케이션을 Docker Compose와 Kubernetes로 배포하는 방법을 보여줍니다. 애플리케이션 스택은 Flask 웹 애플리케이션, Redis, 그리고 NGINX로 구성되어 있습니다.

## 목차

- [사전 준비](#사전-준비)
- [프로젝트 구조](#프로젝트-구조)
- [Docker Compose로 프로젝트 실행하기](#Docker-Compose로-프로젝트-실행하기)
- [Kubernetes로 마이그레이션](#Kubernetes로-마이그레이션)
- [Kubernetes로 프로젝트 실행하기](#Kubernetes로-프로젝트-실행하기)

## 사전 준비

- Docker 및 Docker Compose가 설치되어 있어야 합니다.
- Kubernetes 클러스터(로컬 개발 환경에서는 Minikube를 권장합니다).

## 프로젝트 구조

프로젝트 구조는 다음과 같습니다:

```plaintext
flask-web/
│
├── redis.yaml          # Redis용 Kubernetes Deployment 및 서비스
├── web.yaml            # Flask 웹 앱용 Kubernetes Deployment 및 서비스
│
├── nginx/
│   ├── Dockerfile      # NGINX 이미지 빌드를 위한 Dockerfile
│   └── nginx.conf      # NGINX 설정 파일
│
├── web/
│   ├── src/
│   │   ├── __pycache__/   # 컴파일된 Python 파일
│   │   └── app.py      # Flask 애플리케이션 소스 코드
│   ├── Dockerfile      # Flask 웹 앱을 위한 Dockerfile
│   ├── requirements.txt # Python 의존성 파일
│
└── compose.yml         # 프로젝트용 Docker Compose 파일
```

## Docker Compose로 프로젝트 실행하기

Docker Compose를 사용하여 프로젝트를 실행하려면 다음 단계를 따르세요:

1. **서비스 빌드 및 시작**:
   ```bash
   docker-compose -f compose.yml up --build
   ```

2. **애플리케이션 접근**:
   - Flask 애플리케이션은 `http://localhost:5000`에서 접근할 수 있습니다.
   - NGINX는 `http://localhost`에서 접근 가능하며, Flask 애플리케이션으로 요청을 프록시합니다.

3. **서비스 중지**:
   ```bash
   docker-compose down
   ```

## Kubernetes로 마이그레이션

이 프로젝트에는 Docker Compose 설정을 Kubernetes로 마이그레이션하기 위한 YAML 파일(`redis.yaml`, `web.yaml`)이 포함되어 있습니다.

- **Redis**는 Deployment로 배포되며, ClusterIP 서비스로 노출됩니다.
- **Flask 웹 애플리케이션**은 Deployment로 배포되며, NGINX 대신 NodePort 서비스로 노출됩니다.

## Kubernetes로 프로젝트 실행하기

1. **Minikube 상태 확인**:
   Minikube가 이미 실행 중이거나 Docker Desktop에서 Kubernetes를 실행 중이라면 추가로 시작할 필요가 없습니다. 확인하려면 다음 명령어를 사용하세요:

   ```bash
   minikube status
   ```

   만약 Minikube나 Docker Desktop에서 Kubernetes가 실행 중이지 않다면 Minikube를 시작하세요:

   ```bash
   minikube start
   ```

2. **Redis 및 Flask 웹 애플리케이션 배포**:
   ```bash
   kubectl apply -f flask-web/
   ```

3. **애플리케이션 접근**:
   Flask 애플리케이션은 NodePort 서비스로 노출되었기 때문에 다음 명령어를 사용하여 접근할 수 있습니다:

   ```bash
   minikube service flask-web
   ```

   이 명령어를 실행하면 기본 웹 브라우저에서 Flask 웹 애플리케이션이 열립니다.

4. **정리하기**:
   생성된 Deployment 및 서비스를 삭제하려면 다음 명령어를 사용하세요:

   ```bash
   kubectl delete -f flask-web/
   ```
