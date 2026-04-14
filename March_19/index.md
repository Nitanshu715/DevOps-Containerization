# Kubernetes Deployment & Service Exposure using k3d

## Objective
To deploy an application on a Kubernetes cluster, manage pods, scale deployments, expose services, and verify outputs using kubectl commands.

## Tools Used
- Docker Desktop
- kubectl
- k3d
- Kubernetes (k3s)

## Cluster Verification
Commands:
k3d cluster list
kubectl get nodes

The Kubernetes cluster was already created and verified to be in Ready state.

## Deployment

### Create Deployment
kubectl create deployment web --image=nginx

### Verify Pods
kubectl get pods

The deployment automatically created pods which were observed in Running state.

## Scaling

### Scale Deployment
kubectl scale deployment web --replicas=3

### Verify Scaling
kubectl get pods

The deployment was successfully scaled to three replicas, demonstrating horizontal scaling capability.

## Service Exposure

### Expose Deployment
kubectl expose deployment web --port=80 --type=NodePort

### Verify Service
kubectl get svc

A NodePort service was created, enabling external communication to the application.

## Application Access

### Port Forwarding
kubectl port-forward service/web 8080:80

The application was accessed through:
http://localhost:8080

The NGINX welcome page was successfully displayed.

## Debugging and Verification

### Describe Deployment
kubectl describe deployment web

### Check Logs
kubectl get pods
kubectl logs <pod-name>

### View All Resources
kubectl get all

These commands were used to inspect deployment configuration, logs, and cluster resources.

## Errors and Fixes

Deployment already exists:
kubectl create deployment web --image=nginx
Error: deployment already exists

Service already exists:
kubectl expose deployment web --type=NodePort
Fix: kubectl delete svc web

Incorrect command:
kubectl nodes (invalid)
kubectl get nodes (correct)

Incorrect scaling command:
kubectl scale deployment web --image=nginx (invalid)
kubectl scale deployment web --replicas=3 (correct)

## Observations
- Kubernetes automatically manages pod lifecycle
- Scaling increases application availability
- Services enable communication with pods
- Port forwarding enables local access
- Logs provide runtime insights

## Result
The application was successfully deployed, scaled, and exposed using Kubernetes. The output was verified through browser access.

## Conclusion
This practical demonstrated deployment creation, pod management, scaling, service exposure, and debugging in Kubernetes.

