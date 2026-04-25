# Experiment 12: Container Orchestration using Kubernetes (k3d)

## 1. Introduction

Kubernetes is an advanced container orchestration platform used for automating deployment, scaling, and management of containerized applications. In this experiment, Kubernetes is implemented locally using k3d, a lightweight wrapper to run Kubernetes clusters inside Docker containers.

The experiment demonstrates real-world orchestration concepts including deployment, service exposure, scaling, and self-healing using a practical implementation.

---

## 2. Objectives

- To deploy an application using Kubernetes Deployment
- To expose the application using a NodePort Service
- To verify pod lifecycle management
- To demonstrate self-healing of pods
- To implement horizontal scaling
- To understand Kubernetes orchestration workflow

---

## 3. Prerequisites

- Docker Desktop installed and running
- k3d installed and configured
- kubectl installed
- Basic understanding of containers and Docker

---

## 4. System Configuration

- OS: Windows 11
- Kubernetes: k3d (k3s-based cluster)
- Runtime: Docker
- Cluster: Single-node Kubernetes cluster

---

## 5. Key Concepts

- Pod: Smallest unit in Kubernetes
- Deployment: Ensures desired state of pods
- ReplicaSet: Maintains replica count
- Service: Exposes application
- NodePort: External access method
- Self-Healing: Automatic pod recreation

---

## 6. Implementation

### Step 1: Create Cluster

```bash
k3d cluster create exp12cluster -p "30007:30007@loadbalancer"
```

### Step 2: Verify Cluster

```bash
kubectl get nodes
```

### Step 3: Create Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: webtest
spec:
  replicas: 2
  selector:
    matchLabels:
      app: webtest
  template:
    metadata:
      labels:
        app: webtest
    spec:
      containers:
      - name: webtest
        image: hashicorp/http-echo
        args:
          - "-text=Hello from Kubernetes"
        ports:
        - containerPort: 5678
```

### Step 4: Apply Deployment

```bash
kubectl apply -f nginx-deployment.yaml
```

### Step 5: Verify Pods

```bash
kubectl get pods
```

### Step 6: Create Service

```yaml
apiVersion: v1
kind: Service
metadata:
  name: webtest-service
spec:
  type: NodePort
  selector:
    app: webtest
  ports:
    - port: 5678
      targetPort: 5678
      nodePort: 30007
```

### Step 7: Apply Service

```bash
kubectl apply -f nginx-service.yaml
```

### Step 8: Access Application

Open browser:
http://localhost:30007

---

## 7. Self-Healing

```bash
kubectl delete pod <pod-name>
kubectl get pods
```

---

## 8. Scaling

```bash
kubectl scale deployment webtest --replicas=4
kubectl get pods
```

---

## 9. Observations

- Pods were created successfully
- Application was exposed via NodePort
- Scaling created additional pods dynamically
- Deleting a pod triggered automatic recreation

---

## 10. Results

- Kubernetes Deployment successful
- Service exposure validated
- Self-healing verified
- Scaling implemented

---

## 11. Conclusion

The experiment successfully demonstrated Kubernetes orchestration using k3d. Core features such as deployment, scaling, and self-healing were validated. The system maintained desired state automatically and ensured application availability.

