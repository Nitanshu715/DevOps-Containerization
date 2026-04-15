# Experiment -7 - CI/CD Pipeline using Jenkins, GitHub, and Docker Hub

## Introduction

This experiment focuses on the design and implementation of a complete Continuous Integration and Continuous Deployment (CI/CD) pipeline using Jenkins as the automation server, GitHub as the source code repository, and Docker Hub as the container registry. The pipeline automates the process of building, packaging, and deploying applications in a consistent and reproducible manner.

## Objective

The objective of this experiment is to:
- Understand CI/CD concepts and workflow
- Integrate Jenkins with Docker for automated builds
- Build Docker images from application source code
- Push Docker images to Docker Hub
- Automate the pipeline execution through Jenkins

## Tools and Technologies

- Jenkins (Automation Server)
- Docker (Containerization Platform)
- Docker Hub (Container Registry)
- GitHub (Version Control System)
- Python (Flask Framework)
- Windows Command Prompt

## Workflow Overview

Developer → Code Commit → Jenkins Pipeline → Docker Build → Docker Hub

## Project Structure

- app.py: Flask application
- requirements.txt: Python dependencies
- Dockerfile: Docker image instructions
- Jenkinsfile: CI/CD pipeline definition

## Application Development

A simple Flask application was developed to demonstrate the CI/CD workflow. The application responds with a message confirming successful deployment.

## Docker Image Creation

A Dockerfile was created to containerize the Flask application. The image uses a lightweight Python base image and installs required dependencies before exposing the application on port 80.

## Jenkins Pipeline Configuration

A Jenkins pipeline was created using declarative syntax. The pipeline consists of the following stages:

1. Build Docker Image
2. Login to Docker Hub
3. Push Docker Image

Each stage executes specific commands required for automation.

## Credentials Management

Docker Hub credentials were securely stored in Jenkins using the credentials manager. The credentials were injected into the pipeline during execution to authenticate Docker operations.

## Pipeline Execution

The pipeline was executed successfully through Jenkins. Each stage completed without errors, indicating proper configuration and integration between Jenkins and Docker.

## Docker Hub Integration

The Docker image was successfully built and pushed to Docker Hub. The repository contains the latest image version tagged appropriately.

## Results

- Jenkins pipeline executed successfully
- Docker image built without errors
- Docker Hub login completed securely
- Image pushed to Docker Hub repository
- End-to-end CI/CD workflow achieved

## Observations

- Jenkins provides an intuitive interface for pipeline management
- Docker ensures consistent build environments
- Credential management enhances security
- Automation reduces manual intervention and errors
- CI/CD pipelines improve development efficiency

## Conclusion

This experiment successfully demonstrates the implementation of a CI/CD pipeline using Jenkins, Docker, and Docker Hub. The pipeline automates the process of building and deploying applications, ensuring consistency and reliability. The successful execution of all pipeline stages confirms that the system is correctly configured and functioning as intended.

## Learning Outcomes

- Gained hands-on experience with CI/CD pipelines
- Understood integration between Jenkins and Docker
- Learned how to build and push Docker images
- Explored automation in software development workflows
- Developed skills relevant to modern DevOps practices


