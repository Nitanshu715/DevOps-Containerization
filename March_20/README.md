# Docker & Portainer Setup

## Objective
To explore Docker container management and deploy Portainer for GUI-based container orchestration and monitoring.

## Tools & Technologies Used
- Docker Desktop
- kubectl
- Portainer

## Step 1: Verify Docker Installation
Command:
docker ps

Docker engine was verified to be running successfully.

## Step 2: Kubernetes Context Verification
Commands:
kubectl config get-contexts
kubectl config current-context

The active Kubernetes context was verified.

## Step 3: Create Portainer Volume
Command:
docker volume create portainer_data

A persistent volume was created to store Portainer data.

## Step 4: Run Portainer Container
Command:
docker run -d -p 8000:8000 -p 9443:9443 ^
--name portainer ^
--restart=always ^
-v //var/run/docker.sock:/var/run/docker.sock ^
-v portainer_data:/data ^
portainer/portainer-ce:lts

Portainer container was successfully deployed.

## Step 5: Verify Running Container
Command:
docker ps

The Portainer container was verified to be running with exposed ports.

## Step 6: Access Portainer Web Interface
URL:
https://localhost:9443

Browser security warning was bypassed due to self-signed certificate.

## Step 7: Initial Setup
- Created admin user
- Configured password
- Selected local Docker environment

## Step 8: Dashboard Analysis
Observed:
- Running and stopped containers
- Available images
- Docker volumes and networks
- Real-time container statistics

## Step 9: Features Observed
- GUI-based container management
- Container lifecycle control (start, stop, restart)
- Volume and network inspection
- Stack deployment support
- Container logs and inspection

## Step 10: Error Handling
- Incorrect kubectl command syntax corrected
- Minikube limitations identified in certain environments
- HTTPS warning due to self-signed certificate handled

## Result
- Docker environment verified successfully
- Portainer deployed and accessible via browser
- Container resources managed through GUI interface

## Conclusion
This practical demonstrated Docker container management and GUI-based orchestration using Portainer. It highlights how Portainer simplifies container operations and provides a visual interface for managing Docker environments efficiently.

