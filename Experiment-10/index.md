
# Experiment 10: CI/CD Pipeline using Jenkins, Docker, and SonarQube

## 1. Introduction

In modern software development, Continuous Integration and Continuous Deployment (CI/CD) play a critical role in ensuring faster delivery, higher code quality, and automation of repetitive tasks. This experiment demonstrates the implementation of a complete CI/CD pipeline using Jenkins, Docker, and SonarQube integrated with GitHub.

The pipeline automates the process of building, analyzing, containerizing, and preparing applications for deployment.

---

## 2. Objectives

- To understand CI/CD concepts and workflow
- To set up Jenkins using Docker
- To integrate SonarQube for code quality analysis
- To containerize applications using Docker
- To integrate GitHub with CI/CD pipeline
- To automate build and deployment process

---

## 3. Tools and Technologies

- Docker Desktop (WSL2 backend)
- Jenkins (Docker container)
- SonarQube Cloud
- GitHub
- Java (Maven)
- GitHub Actions

---

## 4. System Setup

### 4.1 Docker Installation

Docker Desktop was installed and configured using WSL2 backend. Verification:

docker --version

### 4.2 Creating Docker Network

docker network create devops-lab

---

## 5. Jenkins Setup

### 5.1 Running Jenkins Container

docker run -d --name jenkins --network devops-lab -p 8085:8080 jenkins/jenkins:lts

### 5.2 Access Jenkins

http://localhost:8085

### 5.3 Retrieve Admin Password

docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword

### 5.4 Install Plugins

- Pipeline
- GitHub Integration
- Docker Pipeline

---

## 6. SonarQube Setup (Cloud)

Due to local resource limitations, SonarQube Cloud was used.

### Steps:
1. Login using GitHub
2. Create organization
3. Import repository
4. Generate SONAR_TOKEN

---

## 7. GitHub Repository Setup

Repository Name: DevOps-Containerization

### Files Included:

- App.java
- pom.xml
- Dockerfile

---

## 8. Dockerfile

FROM openjdk:17
WORKDIR /app
COPY . .
RUN javac App.java
CMD ["java", "App"]

---

## 9. GitHub Secrets

Configured under Settings > Secrets:

- SONAR_TOKEN
- DOCKER_TOKEN

---

## 10. CI/CD Workflow (GitHub Actions)

Workflow includes:

- Checkout code
- Build using Maven
- Run SonarQube analysis
- Build Docker image
- Push to Docker Hub

---

## 11. Jenkins Pipeline

Stages:

1. Build Docker Image
2. Login to Docker Hub
3. Push Image

---

## 12. Execution Flow

1. Code pushed to GitHub
2. GitHub triggers workflow
3. Jenkins builds Docker image
4. SonarQube analyzes code
5. Docker image pushed

---

## 13. Observations

- Jenkins successfully executed pipelines
- Docker containers were running properly
- SonarQube provided code quality insights
- Minor issues were detected in analysis

---

## 14. Results

The CI/CD pipeline was successfully implemented with integration between Jenkins, Docker, GitHub, and SonarQube.

---

## 15. Advantages

- Automation of builds
- Improved code quality
- Faster deployment
- Scalable architecture

---

## 16. Limitations

- Requires sufficient system resources
- Setup complexity for beginners

---

## 17. Conclusion

This experiment demonstrates real-world DevOps practices and provides hands-on experience with CI/CD pipelines. The integration ensures efficient software delivery with quality assurance.

---

## 18. Learning Outcomes

- CI/CD pipeline understanding
- Jenkins pipeline creation
- Docker containerization
- SonarQube integration
- GitHub automation


