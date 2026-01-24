# 🚀 Experiment 1: Virtual Machines vs Containers  
### *A Deep Comparative Study using Ubuntu, Vagrant, Docker & Nginx*

---

## 📖 Introduction

Modern DevOps and cloud-native infrastructures rely heavily on **virtualization** and **containerization**.  
This experiment provides a **hands-on, practical comparison** between:

- **Virtual Machines (VMs)** using VirtualBox + Vagrant  
- **Containers** using Docker  

The same application (**Nginx web server**) is deployed in both environments to analyze:

- Resource utilization  
- Performance  
- Isolation  
- Scalability  

---

## 🎯 Objectives

- Understand conceptual differences between Virtual Machines and Containers  
- Create and manage an Ubuntu VM using Vagrant  
- Deploy Nginx inside a Virtual Machine  
- Deploy Nginx inside a Docker container  
- Observe and compare CPU, RAM, and system overhead  
- Analyze real-world DevOps use cases  

---

## 🖥️ System Requirements

### Hardware
- 64-bit processor with virtualization enabled (Intel VT-x / AMD-V)
- Minimum 4 GB RAM (8 GB recommended)
- Internet connection

### Software
- Windows OS  
- Oracle VirtualBox  
- Vagrant  
- Ubuntu (Vagrant box)  
- Docker Engine  

---

## 🏗️ Architecture Overview

### Virtual Machine Architecture
```
Windows Host OS
 └── VirtualBox (Hypervisor)
     └── Ubuntu Guest OS
         └── Nginx Web Server
```

### Container Architecture
```
Ubuntu OS
 └── Docker Engine
     └── Nginx Container (shares host kernel)
```

---

## 🧩 Part A: Virtual Machine using Vagrant

### 🔹 Verify Vagrant Installation
```bash
vagrant --version
```

### 🔹 Create Project Directory
```bash
mkdir vm-lab
cd vm-lab
```

### 🔹 Initialize Ubuntu VM
```bash
vagrant init ubuntu/jammy64
```

### 🔹 Start Virtual Machine
```bash
vagrant up
```

### 🔹 Access VM
```bash
vagrant ssh
```

---

## 🌐 Install Nginx inside VM
```bash
sudo apt update
sudo apt install -y nginx
sudo systemctl start nginx
```

### 🔍 Verify Nginx (VM)
```bash
curl localhost
```

---

## 📊 Resource Observation (VM)
```bash
free -h
htop
systemd-analyze
```

---

## 🧩 Part B: Containerization using Docker

### 🔹 Install Docker inside VM
```bash
sudo apt update
sudo apt install -y docker.io
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker vagrant
```

Apply group changes:
```bash
exit
vagrant ssh
```

### 🔍 Verify Docker
```bash
docker --version
```

---

## 🌐 Run Nginx Container
```bash
docker run -d -p 8080:80 --name nginx-container nginx
```

### 🔍 Verify Nginx (Container)
```bash
curl localhost:8080
```

---

## 📊 Resource Observation (Container)
```bash
docker stats
free -h
```

---

## 📈 Comparison Table

| Parameter | Virtual Machine | Container |
|---------|----------------|-----------|
| Boot Time | High | Very Low |
| RAM Usage | High | Low |
| CPU Overhead | Higher | Minimal |
| Disk Usage | Large | Small |
| Isolation | Strong | Moderate |

---

## 🧹 Cleanup Commands
```bash
docker stop nginx-container
docker rm nginx-container
exit
vagrant halt
```

---

## ✅ Result

Containers were observed to be **significantly more lightweight and resource-efficient** compared to Virtual Machines.  
VMs provide strong isolation and full OS abstraction, while containers offer faster startup and scalability.

---

## 🏁 Conclusion

Virtual Machines are ideal for strong isolation and legacy systems,  
while Containers dominate modern DevOps, CI/CD, and microservices due to their speed and efficiency.

---

## 👨‍💻 Author Notes

This experiment demonstrates real-world DevOps workflows using industry-standard tools  
such as **Vagrant**, **Docker**, and **Nginx**, aligning with modern cloud practices.

