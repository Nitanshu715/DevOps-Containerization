
# Dockerized Flask Application
---

<p align="center">
  <strong>Production-Ready Containerized Python Web Application</strong><br>
  Built with Docker | Optimized with Multi-Stage Builds | Published to Docker Hub
</p>

---

# Table of Contents

- [Project Overview](#project-overview)
- [Architecture](#architecture)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Application Source Code](#application-source-code)
- [Single-Stage Docker Implementation](#single-stage-docker-implementation)
- [Multi-Stage Docker Implementation](#multi-stage-docker-implementation)
- [Image Lifecycle Management](#image-lifecycle-management)
- [Container Lifecycle Management](#container-lifecycle-management)
- [Image Tagging & Versioning Strategy](#image-tagging--versioning-strategy)
- [Publishing to Docker Hub](#publishing-to-docker-hub)
- [Pull & Deploy Anywhere](#pull--deploy-anywhere)
- [Security Best Practices Implemented](#security-best-practices-implemented)
- [Optimization Techniques Used](#optimization-techniques-used)
- [Complete Command Reference](#complete-command-reference)
- [Conclusion](#conclusion)

---

# Project Overview

This project demonstrates full lifecycle containerization of a Python Flask web application using Docker.

It includes:

- Application packaging
- Dependency management
- Layer optimization
- Multi-stage builds
- Non-root runtime configuration
- Image versioning
- Registry publishing
- Portable deployment

The result is a reproducible, portable, and production-ready containerized application.

---

# Architecture

Application Code  
        ↓  
Dockerfile  
        ↓  
Docker Image  
        ↓  
Docker Container  
        ↓  
Docker Hub Registry  

---

# Technology Stack

- Python 3.9 (Slim Base Image)
- Flask 2.3.3
- Docker Desktop
- Docker Hub
- Windows CMD Environment

---

# Project Structure

```
Docker-Essentials/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── Dockerfile.multistage
└── .dockerignore
```

---

# Application Source Code

## app.py

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Docker!"

@app.route('/health')
def health():
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

## requirements.txt

```
Flask==2.3.3
```

---

# Single-Stage Docker Implementation

## Dockerfile

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]
```

## Build Image

```
docker build -t flask-essentials .
```

## Run Container

```
docker run -d -p 5000:5000 --name flask-container flask-essentials
```

---

# Multi-Stage Docker Implementation

## Dockerfile.multistage

```dockerfile
# Stage 1: Builder
FROM python:3.9-slim AS builder

WORKDIR /app
COPY requirements.txt .

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Runtime
FROM python:3.9-slim

WORKDIR /app

COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY app.py .

RUN useradd -m appuser
USER appuser

EXPOSE 5000

CMD ["python", "app.py"]
```

## Build Multi-Stage Image

```
docker build -f Dockerfile.multistage -t flask-essential-multi .
```

---

# Image Lifecycle Management

```
docker images
docker history flask-essentials
docker inspect flask-essentials
docker rmi flask-essentials
docker image prune
```

---

# Container Lifecycle Management

```
docker ps
docker ps -a
docker logs flask-container
docker stop flask-container
docker start flask-container
docker rm flask-container
docker container prune
```

---

# Image Tagging & Versioning Strategy

```
docker tag flask-essentials nitanshutak/flask-essentials:1.0
docker tag flask-essentials nitanshutak/flask-essentials:latest
docker tag flask-essential-multi nitanshutak/flask-essentials:production
```

Versioning Strategy:

- latest → most recent stable build
- 1.0 → initial release version
- production → optimized multi-stage release

---

# Publishing to Docker Hub

## Login

```
docker login
```

## Push

```
docker push nitanshutak/flask-essentials:1.0
docker push nitanshutak/flask-essentials:latest
docker push nitanshutak/flask-essentials:production
```

---

# Pull & Deploy Anywhere

```
docker pull nitanshutak/flask-essentials:latest
docker run -d -p 5000:5000 nitanshutak/flask-essentials:latest
```

---

# Security Best Practices Implemented

- Slim base image to reduce attack surface
- Non-root container execution
- Minimal runtime dependencies
- Clean build separation using multi-stage
- Ignoring unnecessary files using .dockerignore

---

# Optimization Techniques Used

- Layer caching via ordered COPY instructions
- Multi-stage dependency separation
- Slim base image selection
- Reduced build context using .dockerignore
- Detached container execution

---

# Complete Command Reference

```
docker build -t flask-essentials .
docker build -f Dockerfile.multistage -t flask-essential-multi .
docker run -d -p 5000:5000 --name flask-container flask-essentials
docker logs flask-container
docker tag flask-essentials nitanshutak/flask-essentials:1.0
docker push nitanshutak/flask-essentials:1.0
docker pull nitanshutak/flask-essentials:latest
docker stop flask-container
docker rm flask-container
```

---

# Conclusion

This repository represents a complete Docker containerization workflow including development, optimization, versioning, publishing, and deployment.

The application is:

- Portable
- Reproducible
- Versioned
- Secure
- Production-ready
- Globally deployable via Docker Hub

