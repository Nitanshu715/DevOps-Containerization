# Containerization & DevOps Lab  
### *Master Repository for All Experiments*

---

<p align="center">
  <b>Course:</b> Containerization and DevOps<br/>
  <b>Focus:</b> Virtualization, Containers, CI/CD, Cloud-Native Systems<br/>
</p>

---
<p align="center">
  <b>Name:</b> Nitanshu Tak <br/>
  <b>SapID:</b> 500121943 <br/>
  <b>Course:</b> BTech. CSE (CCVT) <br/>
  <b>Batch:</b> 2 <br/>
</p>

## About This Repository

This repository serves as the **master lab repository** for the subject  
**Containerization and DevOps**.

Each experiment is organized in its **own folder**, containing:
- Experiment-specific source files
- Individual README documentation
- Commands, configurations, and outputs
- Observations and results

This structure reflects **real-world DevOps repositories**, where infrastructure,
automation, and documentation coexist in a clean, scalable manner.

---

## Why This Repository Exists

Modern software systems require:
- Fast deployment
- Scalability
- Automation
- Reproducibility

This lab repository demonstrates **hands-on implementation** of:
- Infrastructure as Code (IaC)
- Virtualization vs Containerization
- Linux system administration
- Docker-based application deployment
- DevOps best practices

---


## Experiments Performed

### [Experiment 1 — Virtual Machines vs Containers](./Experiment-1/)

A DevOps-oriented comparison between Virtual Machines and Containers using Ubuntu, VirtualBox, Vagrant, Docker, and Nginx. Demonstrates infrastructure provisioning, VM-based service deployment, containerized application execution, and architectural differences in resource usage and isolation.

---

### [Experiment 2 — Docker Installation & Container Lifecycle](./Experiment-2/)

Covers Docker fundamentals including image pulling, container execution with port mapping, service verification, port conflict handling, and full container lifecycle management — reflecting real-world container deployment workflows.

---

### [Experiment 3 — Deploying NGINX Using Different Base Images and Comparing Image Layers](./Experiment-3/)

This lab demonstrates how NGINX can be deployed using different Docker base images and analyzes how base OS choices affect image size, layers, and efficiency. It highlights the practical trade-offs between official, Ubuntu-based, and Alpine-based containers in real-world DevOps environments.

---

### [Experiment 4 — NGINX Containerization and Reverse Proxy](./Experiment-4/)

A comprehensive, production-style exploration of NGINX deployment using Docker, custom image engineering, volume management, native WSL installation, and reverse proxy architecture implementation.

---

### [Experiment 5 — Docker Essentials](./Experiment-5/)

This project demonstrates the complete containerization lifecycle of a Python Flask web application using Docker. It includes single-stage and multi-stage Docker builds, optimized image layering, dependency management, container execution, version tagging, and publishing to Docker Hub.

---


## Technologies & Tools Used

```text
Operating Systems:
- Ubuntu Linux
- Windows (Host)

Virtualization:
- Oracle VirtualBox
- Vagrant

Containerization:
- Docker Engine
- Docker CLI

Networking & Services:
- Nginx

DevOps Concepts:
- Infrastructure as Code (IaC)
- Automation
- CI/CD
- Cloud-Native Architecture
```

---

## Learning Outcomes

By completing all experiments in this repository, the learner will be able to:

- Understand differences between VMs and containers
- Deploy applications in isolated environments
- Automate infrastructure provisioning
- Use Docker for container-based deployment
- Follow DevOps-style repository organization
- Apply concepts used in real-world DevOps roles

---

## How to Use This Repository

```bash
# Clone repository
git clone https://github.com/<your-username>/containerization-and-devops-lab.git

# Navigate to an experiment
cd experiment-01-vm-vs-container

# Read experiment-specific documentation
cat README.md
```

---

## DevOps Mindset Demonstrated

This repository reflects:
- Modular design
- Clear documentation
- Automation-first thinking
- Scalability
- Industry-aligned practices

The structure and workflow mirror professional DevOps projects,
making this repository suitable for **academic evaluation** as well as **portfolio use**.

---

## Future Enhancements

- GitHub Actions CI pipelines
- Docker image versioning
- Kubernetes basics
- Cloud deployment (AWS / Azure / GCP)
- Monitoring & logging integration

---

## Author

**Name:** Nitanshu  
**Program:** B.Tech Computer Science Engineering  
**Specialization:** Cloud Computing & Virtualization Technology  
**Focus Areas:** DevOps · Cloud · Automation · Linux

---

## Final Note

This repository is not just a lab submission —  
it is a **foundation for real DevOps engineering practices**.

Build it. Improve it. Ship it. 🚀

