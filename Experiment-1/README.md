# 🚀 Experiment 1: Virtual Machines vs Containers  
## A Comprehensive DevOps-Level Comparative Study using Ubuntu, Vagrant, Docker & Nginx

---

## 📌 Overview

This experiment is designed to provide a **deep, practical, and architectural understanding** of two foundational
technologies used in modern DevOps and cloud infrastructure:

- **Virtual Machines (VMs)**
- **Containers**

Both technologies are implemented using **Ubuntu Linux** and a common application stack (**Nginx Web Server**)
to ensure a fair, real-world comparison.

---

## 🧠 Why This Experiment Matters (DevOps Perspective)

In real-world DevOps pipelines:
- Virtual Machines are used for **infrastructure isolation**
- Containers are used for **application portability and scalability**

Understanding *when and why* to use each is critical for:
- CI/CD pipelines
- Cloud-native deployments
- Microservices architecture
- Platform engineering

This experiment bridges **theory + hands-on execution**.

---

## 🎯 Learning Objectives

- Understand virtualization vs containerization at the architectural level
- Automate VM provisioning using Vagrant
- Deploy and manage services inside a Linux VM
- Containerize applications using Docker
- Observe and analyze system resource utilization
- Compare performance, isolation, and scalability
- Align academic concepts with industry DevOps practices

---

## 🖥️ System & Software Requirements

### Hardware Requirements
- 64-bit processor with Intel VT-x / AMD-V enabled
- Minimum 4 GB RAM (8 GB recommended)
- Active internet connection

### Software Requirements
- Windows Operating System
- Oracle VirtualBox (Hypervisor)
- Vagrant (Infrastructure as Code tool)
- Ubuntu Linux (Vagrant Box)
- Docker Engine
- Nginx Web Server

---

## 🏗️ High-Level Architecture

### Virtual Machine Stack
```
Physical Hardware
 └── Windows Host OS
     └── VirtualBox Hypervisor
         └── Ubuntu Guest OS
             └── Nginx Service
```

### Container Stack
```
Physical Hardware
 └── Ubuntu OS (inside VM)
     └── Docker Engine
         └── Nginx Container
```

---

## 🔍 Conceptual Difference: VM vs Container

| Aspect | Virtual Machine | Container |
|------|----------------|-----------|
| Kernel | Own Kernel | Shares Host Kernel |
| Startup Time | Slow | Very Fast |
| Resource Usage | High | Low |
| Isolation | Strong | Process-level |
| Portability | Moderate | Very High |
| Use Case | OS-level isolation | App-level deployment |

---

## 🧩 Part A: Virtual Machine Implementation using Vagrant

### 🔹 Why Vagrant?
Vagrant allows **Infrastructure as Code (IaC)**, enabling reproducible, automated,
and consistent virtual machine environments without manual OS installation.

---

### 🔹 Step 1: Verify Vagrant Installation
```bash
vagrant --version
```

---

### 🔹 Step 2: Create Project Workspace
```bash
mkdir vm-lab
cd vm-lab
```

---

### 🔹 Step 3: Initialize Ubuntu VM Configuration
```bash
vagrant init ubuntu/jammy64
```

This generates a `Vagrantfile` which defines:
- Base OS image
- Provider (VirtualBox)
- Networking and provisioning behavior

---

### 🔹 Step 4: Provision and Boot the VM
```bash
vagrant up
```

Vagrant performs:
- Image download
- VM creation
- Network configuration
- Headless boot

---

### 🔹 Step 5: Access the VM via SSH
```bash
vagrant ssh
```

This opens a secure terminal session into the Ubuntu VM.

---

## 🌐 Deploying Nginx inside the Virtual Machine

### 🔹 Update Package Index
```bash
sudo apt update
```

### 🔹 Install Nginx
```bash
sudo apt install -y nginx
```

### 🔹 Start Nginx Service
```bash
sudo systemctl start nginx
```

---

### 🔍 Verify Nginx Deployment (VM)
```bash
curl localhost
```

Successful HTML output confirms the service is running.

---

## 📊 Resource Monitoring (Virtual Machine)

```bash
free -h
htop
systemd-analyze
```

These commands provide:
- Memory utilization
- CPU load
- System boot time

---

## 🧩 Part B: Containerization using Docker

### 🔹 Why Containers?
Containers allow applications to run consistently across environments,
eliminating dependency and configuration mismatches.

---

### 🔹 Step 1: Install Docker Engine
```bash
sudo apt update
sudo apt install -y docker.io
```

---

### 🔹 Step 2: Start and Enable Docker
```bash
sudo systemctl start docker
sudo systemctl enable docker
```

---

### 🔹 Step 3: Configure Docker Permissions
```bash
sudo usermod -aG docker vagrant
```

Apply changes:
```bash
exit
vagrant ssh
```

---

### 🔍 Verify Docker Installation
```bash
docker --version
```

---

## 🌐 Deploying Nginx as a Container

```bash
docker run -d -p 8080:80 --name nginx-container nginx
```

Explanation:
- `-d` → Detached mode
- `-p` → Port mapping (Host → Container)
- `nginx` → Official Docker image

---

### 🔍 Verify Nginx Container
```bash
curl localhost:8080
```

---

## 📊 Resource Monitoring (Container)

```bash
docker stats
free -h
```

Demonstrates significantly lower resource usage compared to VM-based deployment.

---

## 🧹 Cleanup & Environment Management

```bash
docker stop nginx-container
docker rm nginx-container
exit
vagrant halt
```

---

## 📈 Final Comparative Analysis

| Parameter | Virtual Machine | Container |
|---------|----------------|-----------|
| Boot Time | High | Very Low |
| Memory Usage | High | Low |
| CPU Overhead | Higher | Minimal |
| Disk Footprint | Large | Small |
| Isolation Level | Strong | Moderate |
| Scalability | Moderate | High |

---

## ✅ Result

The experiment confirms that:
- Containers are more lightweight and resource-efficient
- Virtual Machines provide stronger isolation and OS-level abstraction
- Containers are better suited for modern DevOps and microservices workflows

---

## 🏁 Conclusion

Virtual Machines and Containers serve different but complementary purposes.
While VMs remain essential for strong isolation and infrastructure boundaries,
containers dominate application deployment due to speed, efficiency, and scalability.

This experiment successfully demonstrates both technologies in a real-world DevOps context.

---

## 👨‍💻 Author Notes

This documentation follows **industry-standard DevOps practices** and mirrors
real production workflows involving virtualization, containerization,
and automated infrastructure management.

