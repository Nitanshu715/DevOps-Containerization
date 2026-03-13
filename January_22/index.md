## Docker Basics & Container Management (Windows Environment)

---

## Overview

This practical session focuses on exploring Docker core concepts and managing containers using Docker Desktop on Windows. The lab demonstrates Docker CLI operations, image management, container lifecycle handling, monitoring, and cleanup processes in a DevOps-oriented workflow.

---

## Tools & Technologies Used

- Windows 11
- Docker Desktop
- Command Prompt (CMD)
- Ubuntu Docker Image
- Docker Hub
- Git & GitHub

---

## Step 1: Verify Docker Client & Server Version

```cmd
docker version
docker info
```

---

## Step 2: Run Docker Test Container

```cmd
docker run hello-world
```

---

## Step 3: List Available Docker Images

```cmd
docker images
```

---

## Step 4: Pull Ubuntu Image from Docker Hub

```cmd
docker pull ubuntu
docker images
```

---

## Step 5: Run Ubuntu Container Interactively

```cmd
docker run -it ubuntu bash
```

Inside container:

```bash
ls
pwd
whoami
exit
```

---

## Step 6: Monitor Containers

```cmd
docker ps
docker ps -a
```

---

## Step 7: Container Lifecycle Management

```cmd
docker start <container_id>
docker stop <container_id>
docker rm <container_id>
```

---

## Step 8: Remove Docker Images

```cmd
docker rmi ubuntu
```

---

## GitHub Version Control Commands

```cmd
cd DevOps-Lab-Assignments
git add .
git commit -m "Added Class Practical 22 Jan - Docker Basics & Container Management"
git push
```

---

## Result

- Docker client and server verified successfully.
- Ubuntu image pulled from Docker Hub.
- Containers executed interactively.
- Container lifecycle managed (start, stop, remove).
- Docker images removed successfully.
- Lab pushed to GitHub repository.

---

## Conclusion

This lab strengthens foundational knowledge of Docker CLI usage and container lifecycle operations. It demonstrates practical container management within a Windows environment, forming a core building block for DevOps workflows and cloud-native development practices.

