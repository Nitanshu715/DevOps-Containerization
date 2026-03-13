## Docker Engine Configuration & Client–Server Architecture (Windows)

---

## Overview

This practical demonstrates Docker Engine verification, daemon architecture understanding, and secure client-server communication using Docker Desktop on Windows.
It includes validation of Docker CLI connectivity, context inspection, container execution, and architectural analysis of Docker's internal communication model.

---

## Objectives

- Verify Docker installation and Engine status
- Understand Docker Client–Server architecture
- Inspect Docker contexts
- Validate daemon connectivity via CLI
- Analyze Docker Named Pipe communication (Windows)
- Execute sample container deployment
- Document DevOps Engine-level workflow

---

## Tools & Technologies Used

- Windows 11
- Docker Desktop v29.x
- Docker CLI
- PowerShell / Command Prompt
- WSL2 Backend
- Git & GitHub

---

## Docker Architecture Concept

Docker follows a Client–Server model:

Docker CLI  →  Docker Daemon  →  Containers

On Windows, communication happens via:

npipe:////./pipe/docker_engine

Unlike Linux/macOS, direct TCP exposure (port 2375) is restricted by Docker Desktop for security reasons.

---

## Step 1: Verify Docker Installation

```cmd
docker --version
docker info
```

---

## Step 2: Check Docker Context

```cmd
docker context ls
```

If required:

```cmd
docker context use desktop-linux
```

---

## Step 3: List Containers

Running Containers:

```cmd
docker ps
```

All Containers:

```cmd
docker ps -a
```

---

## Step 4: List Images

```cmd
docker images
```

---

## Step 5: Validate Daemon Connectivity

Docker CLI communicates with daemon using Named Pipe:

```cmd
docker info
docker ps
```

Successful execution confirms daemon connectivity.

---

## Step 6: Deploy Sample Container

```cmd
docker run hello-world
```

This confirms:

- CLI to Daemon communication
- Image pull from Docker Hub
- Container creation and execution
- Proper Docker Engine functioning

---

## Security Note

Docker Desktop does not expose TCP 2375 by default due to security risks.

Unsecured TCP exposure can allow:
- Unauthorized container execution
- Filesystem access
- Host-level compromise

Modern DevOps environments use:
- TLS-secured TCP
- SSH tunneling
- Docker contexts
- Or orchestration platforms (Kubernetes)

---

## GitHub Integration

```cmd
cd ..
git add .
git commit -m "Added Class Practical 4 Feb - Docker Engine Architecture"
git push
```

---

## Result

- Docker Engine verified successfully
- Client–Server architecture understood
- Named Pipe communication confirmed
- Containers and images validated
- Sample container executed successfully

---

## Conclusion

This lab provided in-depth understanding of Docker Engine internals, daemon communication, and secure architecture practices in Windows-based environments.
It highlights real-world DevOps considerations when working with container runtimes and remote API configurations.

