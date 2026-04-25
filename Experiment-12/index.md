# Experiment 12: Container Orchestration using Kubernetes (Minikube)

## Introduction

Kubernetes is an open-source container orchestration platform designed to automate deployment, scaling, and management of containerized applications. It provides a robust and flexible system for managing distributed systems and ensures high availability, fault tolerance, and scalability.

In this experiment, Kubernetes is implemented locally using Minikube. The goal is to deploy a multi-instance WordPress application, expose it externally, and demonstrate key orchestration features such as scaling, self-healing, and service abstraction.

---

## Objectives

- Understand Kubernetes architecture and workflow
- Deploy applications using Deployment resources
- Manage multiple replicas (scaling)
- Expose applications using Services
- Demonstrate self-healing capabilities
- Validate orchestration behavior

---

## Prerequisites

- Docker Desktop installed and running
- Minikube installed and configured
- kubectl CLI tool installed
- Windows system with sufficient disk space
- Basic knowledge of Docker and containers

---

## System Configuration

- OS: Windows 11
- Kubernetes: Minikube (local cluster)
- Container Runtime: Docker
- Node: Single node cluster
- Storage: D:\minikube

---

## Kubernetes Architecture

### Control Plane Components
- API Server: Handles REST requests
- Scheduler: Assigns pods to nodes
- Controller Manager: Maintains desired state
- etcd: Stores cluster data

### Worker Node Components
- Kubelet: Communicates with control plane
- Container Runtime: Runs containers
- Kube Proxy: Handles networking

---

## Key Concepts

- Pod: Smallest deployable unit
- Deployment: Manages pods and replicas
- ReplicaSet: Maintains replica count
- Service: Provides networking and exposure
- NodePort: External access mechanism
- Self-Healing: Automatic pod recovery

---

## Implementation Steps

### Step 1: Start Cluster
```bash
minikube start --driver=docker
```

### Step 2: Verify Cluster
```bash
kubectl get nodes
```

### Step 3: Create Deployment YAML
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: wordpress
spec:
  replicas: 2
  selector:
    matchLabels:
      app: wordpress
  template:
    metadata:
      labels:
        app: wordpress
    spec:
      containers:
      - name: wordpress
        image: wordpress:latest
        ports:
        - containerPort: 80
```

### Step 4: Apply Deployment
```bash
kubectl apply -f wordpress-deployment.yaml
```

### Step 5: Verify Pods
```bash
kubectl get pods
```

### Step 6: Create Service YAML
```yaml
apiVersion: v1
kind: Service
metadata:
  name: wordpress-service
spec:
  type: NodePort
  selector:
    app: wordpress
  ports:
    - port: 80
      targetPort: 80
      nodePort: 30007
```

### Step 7: Apply Service
```bash
kubectl apply -f wordpress-service.yaml
```

### Step 8: Verify Service
```bash
kubectl get svc
```

### Step 9: Access Application
```bash
minikube ip
```
Access via browser using NodePort.

### Step 10: Self-Healing
```bash
kubectl delete pod <pod-name>
kubectl get pods
```

### Step 11: Scaling
```bash
kubectl scale deployment wordpress --replicas=4
```

### Step 12: Cleanup
```bash
kubectl delete -f wordpress-deployment.yaml
kubectl delete -f wordpress-service.yaml
```

---

## Observations

- Pods created automatically
- Services exposed correctly
- Self-healing verified
- Scaling successful
- Application remained accessible

---

## Results

- Deployment successful
- Scaling validated
- Self-healing confirmed
- Service exposure working

---

## Advantages

- High scalability
- Automated recovery
- Declarative configuration
- Production-ready

---

## Limitations

- Complex setup
- Resource intensive
- Learning curve

---

## Conclusion

Kubernetes provides a powerful orchestration platform that automates deployment, scaling, and management of containerized applications. This experiment demonstrated key Kubernetes features including deployment, service exposure, scaling, and self-healing using a real-world application.

