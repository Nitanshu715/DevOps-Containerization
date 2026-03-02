# 🚀 Class Practical — 3 February
## Docker Installation Verification & Nginx Deployment (Windows)

---

## 📌 Overview

This practical demonstrates verification of Docker Desktop installation, testing Docker Engine connectivity through CLI and REST API, and deploying a production-ready Nginx container. It focuses on understanding container lifecycle management and real-world DevOps deployment workflow.

---

## 🛠 Environment Details

- Operating System: Windows 11
- Docker Desktop
- Docker Engine
- Command Prompt (CMD)
- Base Image: Nginx (latest)

---

## 🔎 Step 1: Verify Docker Installation

```cmd
docker --version
docker version
docker info
```

---

## 📦 Step 2: List Containers

```cmd
docker ps
docker ps -a
```

---

## 🔌 Step 3: Test Docker Engine REST API

(Ensure Docker Desktop setting: "Expose daemon on tcp://localhost:2375 without TLS" is enabled)

```cmd
curl http://localhost:2375/_ping
curl http://localhost:2375/version
```

---

## 📡 Step 4: List Containers via Docker REST API

```cmd
curl http://localhost:2375/v1.43/containers/json
curl "http://localhost:2375/v1.43/containers/json?all=true"
```

---

## 🌐 Step 5: Pull Nginx Image

```cmd
docker pull nginx
docker images
```

---

## 🚀 Step 6: Create and Run Nginx Container

```cmd
docker create --name mynginx -p 8080:80 nginx
docker start mynginx
docker ps
```

Access in browser:

http://localhost:8080

---

## 🔍 Step 7: Inspect Container

```cmd
docker inspect mynginx
```

---

## 🛑 Step 8: Stop and Remove Container

```cmd
docker stop mynginx
docker rm mynginx
docker ps -a
```

---

## 🔄 Container Lifecycle Demonstrated

Pull → Create → Start → Inspect → Stop → Remove

---

## ✅ Result

- Docker installation successfully verified.
- Docker Engine connectivity confirmed via CLI and REST API.
- REST API communication validated.
- Nginx container deployed successfully.
- Container lifecycle operations performed successfully.

---

## 🎯 Conclusion

This practical strengthened understanding of Docker architecture, daemon communication, REST API interaction, and production-ready container deployment using Nginx. It demonstrates core DevOps container workflow implementation in a Windows-based environment.

