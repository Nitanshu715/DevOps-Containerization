
# Kubernetes Deployment: Imperative vs Declarative Approach

## Overview
This document demonstrates the implementation of both Imperative and Declarative approaches in Kubernetes using an NGINX deployment. The objective is to understand how Kubernetes manages desired state through different operational methodologies and how declarative configurations enable reproducibility and scalability.

## Objective
To implement and compare Imperative and Declarative deployment approaches in Kubernetes by deploying an NGINX application, modifying configuration using YAML, and validating deployment behavior.

## Theory

Kubernetes operates on a declarative model where the user defines the desired state of the system. The Kubernetes control plane continuously monitors the actual state and reconciles it with the desired state.

### Imperative Approach
The imperative approach involves issuing direct commands to Kubernetes to create or manage resources.

Example:
kubectl create deployment web --image=nginx

Characteristics:
- Command-driven execution
- Immediate changes applied
- No persistent configuration
- Limited reproducibility
- Difficult to track changes over time

### Declarative Approach
The declarative approach uses configuration files (YAML or JSON) to define the desired system state.

Example:
kubectl apply -f deployment.yaml

Characteristics:
- Configuration-driven
- Reproducible and version-controlled
- Supports infrastructure as code practices
- Enables easy scaling and updates
- Industry-standard methodology

## Environment Setup
- Kubernetes cluster created using k3d
- kubectl CLI configured and connected to cluster
- Docker used as underlying container runtime

## Implementation Steps

### Step 1: Imperative Deployment
The NGINX deployment is created using a direct command:

kubectl create deployment web --image=nginx

### Step 2: Verification
Deployment and pod status are verified using:

kubectl get deployments
kubectl get pods

### Step 3: YAML Generation
A YAML configuration file is generated from the existing deployment:

kubectl create deployment web --image=nginx --dry-run=client -o yaml > deployment.yaml

### Step 4: Declarative Configuration
The generated YAML file is modified to include multiple replicas and structured metadata.

Configuration:
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
  labels:
    app: web
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
      - name: nginx
        image: nginx

### Step 5: Replace Deployment
The existing deployment is removed:

kubectl delete deployment web

### Step 6: Apply Declarative Configuration
The YAML configuration is applied:

kubectl apply -f deployment.yaml

### Step 7: Validation
Deployment status and pod replicas are verified:

kubectl get pods
kubectl describe deployment web

### Step 8: Application Access
The application is accessed using port forwarding:

kubectl port-forward deployment/web 8080:80

The application is available at:
http://localhost:8080

### Step 9: Scaling
The deployment is scaled dynamically:

kubectl scale deployment web --replicas=5

### Step 10: Cleanup
Resources are cleaned up:

kubectl delete deployment web

## Observations
- Imperative approach allows quick resource creation but lacks flexibility
- Declarative approach enables reproducible and scalable deployments
- Kubernetes automatically manages replicas through ReplicaSets
- Port forwarding provides direct access to services in local environments
- Scaling operations dynamically adjust pod count

## Result
- Deployment was successfully created using both approaches
- Pods were running and managed correctly
- Application was accessible through browser
- Scaling operation increased the number of pods successfully

## Conclusion
The declarative approach is preferred in Kubernetes environments as it provides a robust and scalable way to manage infrastructure. It aligns with modern DevOps practices by enabling version control, reproducibility, and automation. Kubernetes ensures system consistency through its reconciliation loop, maintaining the desired state at all times.

## Key Learnings
- Understanding of imperative vs declarative deployment models
- Importance of YAML-based configuration in Kubernetes
- Deployment architecture including Deployment, ReplicaSet, and Pods
- Scaling and managing applications in Kubernetes
- Practical exposure to Kubernetes CLI operations


