# Experiment 8: Configuration Management using Ansible (Chef Solo vs Ansible)

---

## 1. Objective

The primary objective of this experiment is to understand the concept of configuration management and implement infrastructure automation using Ansible. This experiment also aims to compare Chef Solo and Ansible in terms of architecture, execution model, scalability, and real-world usability.

---

## 2. Introduction

Configuration management is a crucial DevOps practice that ensures consistency across systems by automating the deployment, configuration, and maintenance of infrastructure. In modern distributed environments, manual configuration is error-prone and inefficient. Tools like Ansible provide automation capabilities that enable reproducible and scalable infrastructure management.

This experiment demonstrates how Ansible can be used as a configuration management tool to automate the installation and configuration of services. It also compares Ansible with Chef Solo to highlight differences in architecture and operational efficiency.

---

## 3. Background Concepts

### 3.1 Configuration Management
Configuration management refers to the process of maintaining consistency of a system's performance, functional attributes, and physical attributes with its requirements, design, and operational information.

### 3.2 Infrastructure as Code (IaC)
Infrastructure as Code allows infrastructure to be defined using code, making it version-controlled, reproducible, and automated.

### 3.3 Agent-Based vs Agentless Systems
Agent-based systems require software installed on each node, while agentless systems operate remotely without requiring additional software on managed nodes.

---

## 4. Tools and Technologies Used

- Operating System: Ubuntu (WSL)
- Automation Tool: Ansible
- Web Server: Nginx
- Version Control: Git & GitHub

---

## 5. System Architecture

### Control Node
The control node is the machine where Ansible is installed and from which automation tasks are executed.

### Managed Node
The managed node is the target system where tasks are executed. In this experiment, localhost is used as the managed node.

---

## 6. Installation and Setup

### 6.1 System Update

sudo apt update
sudo apt upgrade -y

### 6.2 Fixing Broken Dependencies

sudo apt --fix-broken install -y

### 6.3 Installing Ansible

sudo apt install ansible -y

### 6.4 Verifying Installation

ansible --version

---

## 7. Inventory Configuration

An inventory file is created to define the managed nodes.

[local]
localhost ansible_connection=local

---

## 8. Testing Connectivity

ansible -i inventory local -m ping

Expected Output:
SUCCESS => "pong"

---

## 9. Playbook Creation

- name: Experiment 8 Demo
  hosts: local
  become: yes

  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present

    - name: Start nginx
      service:
        name: nginx
        state: started

---

## 10. Playbook Execution

ansible-playbook -i inventory playbook.yml

Expected Output:
ok=3
failed=0

---

## 11. Debugging and Issue Resolution

During execution, a 502 Bad Gateway error was encountered while accessing the service.

### Root Cause
The default Nginx configuration was acting as a reverse proxy instead of serving static content.

### Solution
The Nginx configuration was modified to serve static files.

---

## 12. Nginx Configuration

server {
    listen 80;
    server_name localhost;

    root /var/www/html;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }
}

---

## 13. Final Output Verification

echo "Hello from Nitanshu Experiment 8" | sudo tee /var/www/html/index.html
curl localhost

Expected Output:
Hello from Nitanshu Experiment 8

---

## 14. Comparison: Chef Solo vs Ansible

### Chef Solo
- Operates without a central server
- Requires local configuration on each node
- Limited orchestration capabilities

### Ansible
- Centralized control
- Agentless architecture
- Uses SSH for communication
- Highly scalable and efficient

---

## 15. Advantages of Ansible

- Simple YAML syntax
- Agentless operation
- Easy to learn and implement
- Scalable for large infrastructures
- Strong community support

---

## 16. Learning Outcomes

- Understanding configuration management principles
- Implementing automation using Ansible
- Writing and executing playbooks
- Debugging system-level issues
- Configuring web servers

---

## 17. Conclusion

This experiment successfully demonstrates the implementation of configuration management using Ansible. The automation of Nginx installation and configuration validates the effectiveness of Ansible as a DevOps tool. The comparison with Chef Solo highlights the advantages of Ansible in terms of simplicity, scalability, and centralized control.

---

## 18. Repository Structure

Experiment-8/
├── inventory
├── playbook.yml
├── README.md

---

## 19. Author

Name: Nitanshu Tak
Program: B.Tech Computer Science Engineering
Specialization: Cloud Computing and Virtualization Technology

