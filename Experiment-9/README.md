# Experiment 9 – Ansible Automation with Docker (WSL-Based Windows Environment)

## Table of Contents
1. Introduction
2. Objectives
3. System Architecture
4. Prerequisites
5. Detailed Theory
6. Installation and Configuration
7. SSH Key-Based Authentication
8. Docker Environment Setup
9. Container Deployment Strategy
10. Ansible Inventory Configuration
11. Playbook Design and Execution
12. Verification and Validation
13. Results and Observations
14. Troubleshooting and Error Handling
15. Key Concepts
16. Learning Outcomes
17. Conclusion
18. Repository Structure

---

## 1. Introduction
This experiment demonstrates the implementation of configuration management and automation using Ansible over multiple Docker containers acting as remote servers. The entire setup is executed within a Windows environment using Windows Subsystem for Linux (WSL), ensuring compatibility with native Linux-based tools.

---

## 2. Objectives
- To understand the working of Ansible as a configuration management tool
- To simulate multiple servers using Docker containers
- To establish SSH key-based authentication between control node and managed nodes
- To automate tasks across multiple nodes using YAML-based playbooks
- To demonstrate Infrastructure as Code (IaC) principles

---

## 3. System Architecture
The architecture consists of a control node and multiple managed nodes.

Control Node:
- WSL Ubuntu environment
- Ansible installed

Managed Nodes:
- Docker containers running Ubuntu
- SSH server enabled

Communication:
- SSH protocol using key-based authentication

---

## 4. Prerequisites
- Windows 10/11
- WSL installed with Ubuntu
- Docker Desktop with WSL integration enabled
- Basic knowledge of Linux commands

---

## 5. Detailed Theory

### What is Ansible
Ansible is an open-source automation tool used for configuration management, application deployment, and orchestration. It operates without agents and uses SSH for communication.

### Key Features
- Agentless architecture
- Idempotency
- Declarative configuration
- YAML-based playbooks

### Docker Role
Docker is used to create lightweight containers that simulate multiple servers locally.

---

## 6. Installation and Configuration

### Fixing Dependencies
sudo dpkg --configure -a
sudo apt --fix-broken install -y

### Installing Ansible
sudo apt update
sudo apt install ansible -y

### Verification
ansible --version

---

## 7. SSH Key-Based Authentication

### Generate Key
ssh-keygen -t rsa -b 4096

### Copy Keys
cp ~/.ssh/id_rsa .
cp ~/.ssh/id_rsa.pub .

---

## 8. Docker Environment Setup

### Dockerfile Configuration
FROM ubuntu

RUN apt update -y
RUN apt install -y python3 openssh-server
RUN mkdir -p /var/run/sshd

RUN mkdir -p /run/sshd && \
    echo 'root:password' | chpasswd && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config && \
    sed -i 's/#PubkeyAuthentication yes/PubkeyAuthentication yes/' /etc/ssh/sshd_config

RUN mkdir -p /root/.ssh
COPY id_rsa /root/.ssh/id_rsa
COPY id_rsa.pub /root/.ssh/authorized_keys

RUN chmod 600 /root/.ssh/id_rsa
RUN chmod 644 /root/.ssh/authorized_keys

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]

---

## 9. Container Deployment Strategy

### Build Image
docker build -t ubuntu-server .

### Run Containers
for i in {1..4}; do
docker run -d -p 220$i:22 --name server$i ubuntu-server
done

---

## 10. Ansible Inventory Configuration

[servers]
localhost:2201
localhost:2202
localhost:2203
localhost:2204

[servers:vars]
ansible_user=root
ansible_ssh_private_key_file=~/.ssh/id_rsa
ansible_connection=ssh

---

## 11. Playbook Design and Execution

### playbook.yml
---
- name: Configure servers
  hosts: servers
  become: yes

  tasks:
    - name: Update packages
      apt:
        update_cache: yes

    - name: Install packages
      apt:
        name: ["vim", "htop", "wget"]
        state: present

    - name: Create file
      copy:
        dest: /root/test_file.txt
        content: "Configured using Ansible automation"

### Execution
ansible-playbook -i inventory.ini playbook.yml

---

## 12. Verification and Validation

ansible all -i inventory.ini -m command -a "cat /root/test_file.txt"

---

## 13. Results and Observations
- Successful SSH communication established
- All containers responded to Ansible ping
- Playbook executed across all nodes
- Configuration applied consistently

---

## 14. Troubleshooting and Error Handling
- Fixed dpkg dependency issues
- Enabled Docker WSL integration
- Verified SSH connectivity before automation
- Used logs for debugging containers

---

## 15. Key Concepts
- Control Node
- Managed Nodes
- Inventory
- Playbooks
- Modules
- Idempotency

---

## 16. Learning Outcomes
- Practical understanding of Ansible
- Automation of multi-node systems
- Use of Docker for simulation
- Implementation of IaC principles

---

## 17. Conclusion
The experiment successfully demonstrates the power of Ansible in automating infrastructure tasks across multiple nodes using a Windows-based setup with WSL.

---

## 18. Repository Structure
.
├── Dockerfile
├── inventory.ini
├── playbook.yml
├── README.md
└── screenshots


