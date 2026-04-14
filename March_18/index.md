
# Kubernetes Local Cluster Deployment using k3d

## Overview
This project demonstrates the setup and operation of a local Kubernetes environment using k3d, a lightweight wrapper to run k3s (Rancher Lab’s minimal Kubernetes distribution) in Docker. The objective is to simulate a production-like container orchestration environment locally and perform essential Kubernetes operations such as deployment, service exposure, scaling, and validation.

## Architecture
The setup uses Docker as the container runtime and k3d to create a Kubernetes cluster inside Docker containers. The cluster consists of:
- One control plane node
- A load balancer container
- Docker network for internal communication

## Tools and Technologies
- Kubernetes (k3s)
- k3d
- Docker Desktop
- kubectl CLI
- NGINX (as sample application)

## Cluster Setup
A Kubernetes cluster is created using k3d with explicit API port exposure and load balancer port mapping.

Command:
k3d cluster create mycluster --api-port 6550 -p "8081:80@loadbalancer"

This ensures that the Kubernetes API server is accessible and external traffic can be routed through the load balancer.

## Kubeconfig Configuration
Due to networking issues in certain environments, kubeconfig is manually adjusted to replace host.docker.internal with 127.0.0.1 to ensure proper connectivity between kubectl and the cluster API server.

## Deployment
An NGINX deployment is created using the kubectl CLI:

kubectl create deployment nginx --image=nginx

This creates a deployment object which manages replica sets and pods.

## Pod Management
Pods are verified using:
kubectl get pods

The deployment ensures that the desired number of pod replicas are maintained automatically.

## Service Exposure
The deployment is exposed using a NodePort service:

kubectl expose deployment nginx --type=NodePort --port=80

This creates a service that maps the internal container port to an external port.

## Scaling
The deployment is scaled to multiple replicas:

kubectl scale deployment nginx --replicas=3

Kubernetes ensures high availability by maintaining the desired number of replicas.

## Verification
System state is verified using:

kubectl get nodes
kubectl get pods
kubectl get svc
kubectl describe deployment nginx

Logs are accessed using:
kubectl logs <pod-name>

## Port Forwarding
Due to Docker networking constraints in k3d, port forwarding is used:

kubectl port-forward service/nginx 8080:80

The application becomes accessible at:
http://localhost:8080

## Observations
- Kubernetes cluster was successfully initialized using k3d
- Pods were dynamically created and managed by the deployment
- Service exposure allowed external access to the application
- Scaling ensured multiple instances for reliability
- Port forwarding enabled seamless access despite networking constraints

## Conclusion
This implementation demonstrates the fundamental workflow of Kubernetes including cluster setup, deployment, service exposure, scaling, and validation. It provides a strong foundation for understanding container orchestration in real-world DevOps environments.

