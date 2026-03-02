# 🚀 Class Practical — 23 January
## Docker Networking & Multi-Container Basics (Windows Environment)

---

## 📌 Overview

This practical session demonstrates Docker networking concepts including bridge networking, container-to-container communication, port mapping, and multi-container deployment using Docker Desktop on Windows.

---

## 🛠 Tools & Technologies Used

- Windows 11
- Docker Desktop
- Ubuntu Docker Image
- Nginx Docker Image
- Redis Docker Image
- Command Prompt (CMD)
- Git & GitHub

---

## 🔎 Step 1: List Existing Docker Networks

```cmd
docker network ls
```

---

## 🌐 Step 2: Create Custom Bridge Network

```cmd
docker network create my-network
docker network ls
```

---

## 🐧 Step 3: Run First Ubuntu Container

```cmd
docker run -dit --name container1 --network my-network ubuntu
docker ps
```

---

## 🐧 Step 4: Run Second Ubuntu Container

```cmd
docker run -dit --name container2 --network my-network ubuntu
docker ps
```

---

## 🔄 Step 5: Container-to-Container Communication

```cmd
docker exec -it container1 bash
apt update
apt install -y iputils-ping
ping container2
exit
```

---

## 🌍 Step 6: Port Mapping with Nginx

```cmd
docker run -d --name webserver -p 8080:80 nginx
docker ps
```

Access in browser:
http://localhost:8080

---

## 📦 Step 7: Multi-Container Deployment (Redis Service)

```cmd
docker run -d --name redis-server redis
docker ps
```

---

## 🔗 GitHub Version Control Commands

```cmd
cd DevOps-Lab-Assignments
mkdir "Class Practical 23 Jan"
cd "Class Practical 23 Jan"
notepad README.md
```

```cmd
cd ..
git add .
git commit -m "Added Class Practical 23 Jan - Docker Networking"
git push
```

---

## ✅ Result

- Custom Docker bridge network created successfully.
- Containers communicated using internal Docker DNS.
- Nginx service exposed to host using port mapping.
- Multiple containers deployed simultaneously.
- Project successfully pushed to GitHub.

---

## 🎯 Conclusion

This experiment demonstrates Docker networking fundamentals including bridge mode networking, service exposure, and multi-container architecture. These concepts form the foundation of microservices-based application deployment and modern DevOps practices.

