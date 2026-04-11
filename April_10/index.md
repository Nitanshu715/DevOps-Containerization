# Class Practical — End-to-End CI/CD Pipeline for FastAPI using Docker and GitHub Actions

## 1. Introduction
This practical demonstrates the implementation of a complete Continuous Integration and Continuous Deployment (CI/CD) pipeline by integrating application development, containerization, and automated deployment workflows. The project focuses on building a FastAPI-based application, containerizing it using Docker, and automating the build and push process using GitHub Actions.

The pipeline ensures that every change pushed to the repository triggers an automated workflow that builds a Docker image and publishes it to Docker Hub securely.

---

## 2. Objectives
- To develop a FastAPI-based backend application
- To containerize the application using Docker
- To implement a CI/CD pipeline using GitHub Actions
- To automate Docker image build and push operations
- To secure credentials using GitHub Secrets
- To validate deployment through container execution

---

## 3. Technology Stack
- Programming Language: Python
- Framework: FastAPI
- Containerization: Docker Engine
- Container Registry: Docker Hub
- CI/CD Tool: GitHub Actions
- Version Control: Git and GitHub
- Environment: Windows with WSL integration

---

## 4. System Architecture
Developer → Git Push → GitHub Repository → GitHub Actions Workflow → Docker Build → Docker Push → Container Deployment

---

## 5. Project Structure
DevOps-Containerization/
│
├── .github/
│   └── workflows/
│       └── april10-docker.yml
│
└── April_10/
    ├── main.py
    ├── Dockerfile
    ├── requirements.txt
    └── README.md

---

## 6. Application Development
A FastAPI application was developed to provide REST endpoints. The application returns structured JSON responses containing user information including name, SAP ID, and location.

The application supports:
- Root endpoint for static data
- Dynamic endpoint for parameter-based responses

---

## 7. Dependency Management
Dependencies were managed using a requirements.txt file, ensuring consistent and reproducible environments across builds.

Dependencies include:
- fastapi
- uvicorn

---

## 8. Dockerization Process
The application was containerized using Docker. A lightweight base image (python:3.10-slim) was used to optimize performance and reduce image size.

### Dockerfile Configuration
- Base Image: Python 3.10 slim
- Working Directory: /app
- Copy Application Files
- Install Dependencies
- Expose Port 80
- Run application using Uvicorn server

### Build Command
docker build -t fastapi-app .

### Run Command
docker run -p 8081:80 fastapi-app

---

## 9. Docker Hub Integration
A repository was created on Docker Hub to store container images.

### Tagging Image
docker tag fastapi-app nitanshutak/fastapi-app:v0.1

### Pushing Image
docker push nitanshutak/fastapi-app:v0.1

---

## 10. CI/CD Pipeline using GitHub Actions
A GitHub Actions workflow was created to automate the process of building and pushing Docker images.

### Workflow Features
- Triggered on push events
- Builds Docker image from April_10 directory
- Logs into Docker Hub using secure token
- Pushes image to Docker Hub

### Workflow Location
.github/workflows/april10-docker.yml

---

## 11. Secure Authentication
Authentication with Docker Hub was implemented using GitHub Secrets.

Secret Used:
- Name: DOCKER_TOKEN
- Purpose: Secure login to Docker Hub

This ensures that sensitive credentials are not exposed in code.

---

## 12. Automated Pipeline Execution
Upon pushing code:
- GitHub Actions workflow is triggered
- Docker image is built automatically
- Image is pushed to Docker Hub
- Logs are generated for monitoring

---

## 13. Deployment Verification
The deployed image was tested locally by pulling from Docker Hub and running the container.

### Command
docker run -p 8082:80 nitanshutak/fastapi-app:v0.1

### Verification
Application output was successfully accessed through the browser.

---

## 14. Results
- FastAPI application successfully containerized
- Docker image built and stored in Docker Hub
- CI/CD pipeline executed successfully
- Secure authentication implemented using secrets
- Deployment validated through container execution

---

## 15. Learning Outcomes
- Understanding of containerization using Docker
- Practical implementation of CI/CD pipelines
- Experience with GitHub Actions workflows
- Secure credential management using secrets
- Real-world DevOps workflow implementation

---

## 16. Conclusion
This practical demonstrates a complete DevOps lifecycle starting from application development to automated deployment. The integration of Docker and GitHub Actions provides a scalable and efficient workflow for modern software development.

The implementation reflects industry-standard practices for building automated, reliable, and production-ready systems.

