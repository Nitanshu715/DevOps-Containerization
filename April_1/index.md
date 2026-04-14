
# Jenkins CI/CD Server Deployment using Docker

## Overview
This project demonstrates the deployment of Jenkins, a widely used continuous integration and continuous delivery (CI/CD) automation server, using Docker. The setup provides a reproducible, isolated, and persistent environment for running Jenkins locally.

## Architecture
- Jenkins container running inside Docker
- Named Docker volume for persistent storage
- Port mapping for web interface and agent communication

## Tools and Technologies
- Docker Engine
- Docker Compose
- Jenkins LTS

## Setup Instructions

### Create Project Directory
mkdir jenkins-docker
cd jenkins-docker

### Create docker-compose.yml
Define Jenkins service with ports and volume.

### Run Jenkins
docker compose up -d

### Access Jenkins
http://localhost:8081

### Unlock Jenkins
docker exec jenkins-server cat /var/jenkins_home/secrets/initialAdminPassword

### Install Plugins
Install suggested plugins.

### Create User
Set username, password, and email.

## Verification

### Check Containers
docker ps

### View Logs
docker logs jenkins-server

## Observations
- Jenkins container deployed successfully
- Accessible via browser
- Persistent data storage implemented
- Plugins installed and user configured

## Conclusion
This setup demonstrates containerized Jenkins deployment using Docker and forms a base for CI/CD pipeline implementation.

