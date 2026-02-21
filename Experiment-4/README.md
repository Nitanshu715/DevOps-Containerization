

# ───────────────────────────────────────────────────────────────
# NGINX CONTAINERIZATION & REVERSE PROXY ARCHITECTURE LAB
# ───────────────────────────────────────────────────────────────

<p align="center">
  <strong>Enterprise‑Style Web Infrastructure Deployment using Docker, WSL, and Native NGINX</strong>
</p>

---

## PROJECT OVERVIEW

This project demonstrates a complete infrastructure lifecycle for deploying and managing NGINX across multiple environments, including:

- Official Docker container deployment
- Custom Ubuntu-based image engineering
- Lightweight Alpine-based image optimization
- Volume binding for dynamic content management
- Native NGINX installation inside WSL Ubuntu
- Reverse proxy implementation with backend routing
- Cross-environment debugging between Windows and WSL

The implementation replicates production‑style architecture principles in a controlled development environment.

---

## ARCHITECTURE DESIGN

### Infrastructure Layers

```
Client Browser
      │
      ▼
NGINX Reverse Proxy (Port 80 - WSL)
      │
      ▼
Backend Service (Port 3000 - Python HTTP Server)
```

### Dockerized Instances

| Container Name   | Base Image | Port Mapping | Purpose |
|------------------|-----------|-------------|----------|
| nginx-official   | nginx     | 8080:80     | Official optimized image |
| nginx-ubuntu     | ubuntu    | 8081:80     | Full OS-based custom image |
| nginx-alpine     | alpine    | 8082:80     | Minimal lightweight image |
| nginx-volume     | nginx     | 8083:80     | Bind-mounted static content |

---

## TECHNOLOGY STACK

- Docker Engine
- Ubuntu 22.04 (WSL2)
- NGINX 1.24
- Python 3 HTTP Server
- Windows 10/11 with WSL2

---

## 1. OFFICIAL NGINX DEPLOYMENT

```bash
docker pull nginx
docker run -d --name nginx-official -p 8080:80 nginx
```

This container provides a production-optimized NGINX runtime environment.

---

## 2. UBUNTU-BASED CUSTOM IMAGE

### Dockerfile

```dockerfile
FROM ubuntu:22.04

RUN apt update && \
    apt install -y nginx && \
    apt clean

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

### Build & Run

```bash
docker build -t nginx-ubuntu .
docker run -d --name nginx-ubuntu -p 8081:80 nginx-ubuntu
```

This approach demonstrates OS-level package control and extended system tooling availability.

---

## 3. ALPINE-BASED LIGHTWEIGHT IMAGE

### Dockerfile

```dockerfile
FROM alpine:latest

RUN apk add --no-cache nginx

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

### Build & Run

```bash
docker build -t nginx-alpine .
docker run -d --name nginx-alpine -p 8082:80 nginx-alpine
```

Alpine significantly reduces image size and attack surface.

---

## 4. VOLUME BIND MOUNT IMPLEMENTATION

```bash
docker run -d \
  --name nginx-volume \
  -p 8083:80 \
  -v %cd%\html:/usr/share/nginx/html \
  nginx
```

Bind mounts allow real-time content updates without rebuilding images.

---

## 5. NATIVE NGINX INSTALLATION (WSL)

```bash
sudo apt update
sudo apt install nginx
sudo service nginx start
```

This provides system-level control beyond container isolation.

---

## 6. BACKEND SERVICE IMPLEMENTATION

```python
from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello from Backend Server on Port 3000!")

server = HTTPServer(("127.0.0.1", 3000), Handler)
server.serve_forever()
```

Run inside WSL:

```bash
python3 app.py
```

---

## 7. REVERSE PROXY CONFIGURATION

Edit:

```
/etc/nginx/sites-available/default
```

Replace server block with:

```nginx
server {
    listen 80;

    location / {
        proxy_pass http://127.0.0.1:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

Restart service:

```bash
sudo service nginx restart
```

---

## IMAGE SIZE COMPARISON

| Image Type      | Approximate Size |
|-----------------|------------------|
| nginx:latest   | ~140MB |
| nginx-ubuntu   | ~220MB+ |
| nginx-alpine   | ~25-30MB |

Alpine provides maximum efficiency. Ubuntu provides extensibility.

---

## NETWORKING & DEBUGGING INSIGHTS

- Identified Apache and NGINX port conflicts
- Diagnosed 502 Bad Gateway errors
- Resolved Windows vs WSL loopback isolation
- Verified upstream availability using:
  ```bash
  curl http://127.0.0.1:3000
  sudo ss -tulpn
  ```
- Ensured backend service executed inside WSL environment

---

## PRODUCTION CONCEPTS DEMONSTRATED

- Containerization
- OS-based image engineering
- Minimal attack surface optimization
- Bind-mounted storage abstraction
- Reverse proxy routing
- Service isolation
- Layer inspection using `docker history`
- Infrastructure debugging methodology

---

## CONCLUSION

This project demonstrates a structured, production-style deployment workflow incorporating container orchestration, system-level configuration, network isolation debugging, and reverse proxy architecture design.

It represents a complete DevOps pipeline from container creation to service routing abstraction.

