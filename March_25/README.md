# Kubernetes Apache Web Application Practical

## Overview
This practical demonstrates the deployment, management, scaling, debugging, and modification of a containerized Apache web server using Kubernetes. The entire workflow is executed using CLI-based operations, providing hands-on experience with real-world container orchestration practices.

## Objective
- Deploy an Apache HTTP server using Kubernetes
- Verify application accessibility through browser
- Convert a standalone Pod into a managed Deployment
- Expose the application using a Service
- Perform horizontal scaling of the application
- Simulate failure scenarios and debug issues
- Modify live container content
- Validate Kubernetes self-healing capabilities

## Tools and Technologies
- Kubernetes (k3d cluster)
- Docker
- kubectl CLI
- Apache HTTP Server (httpd image)

## Implementation Steps

### Pod Creation
kubectl run apache-pod --image=httpd

### Pod Verification
kubectl get pods
kubectl describe pod apache-pod

### Access Application
kubectl port-forward pod/apache-pod 8081:80

### Delete Pod
kubectl delete pod apache-pod

### Deployment Creation
kubectl create deployment apache --image=httpd

### Deployment Verification
kubectl get deployments
kubectl get pods

### Service Exposure
kubectl expose deployment apache --port=80 --type=NodePort
kubectl get svc

### Access via Service
kubectl port-forward service/apache 8082:80

### Scaling
kubectl scale deployment apache --replicas=2
kubectl get pods

### Failure Simulation
kubectl set image deployment/apache httpd=wrongimage
kubectl get pods

### Fix Deployment
kubectl set image deployment/apache httpd=httpd
kubectl get pods

### Modify Container Content
kubectl exec -it <pod-name> -- /bin/sh
echo Hello from Kubernetes > /usr/local/apache2/htdocs/index.html
exit

### Self-Healing Test
kubectl delete pod <pod-name>
kubectl get pods

### Cleanup
kubectl delete deployment apache
kubectl delete service apache

## Observations
- Kubernetes successfully managed application lifecycle
- Deployment ensured automatic pod management and scaling
- Service abstraction enabled network access to application
- Kubernetes handled failures and recreated pods automatically
- Live container modification reflected in real-time output

## Conclusion
This practical demonstrates key Kubernetes capabilities including deployment management, service exposure, scaling, debugging, and self-healing. It provides a strong foundation for understanding real-world container orchestration workflows and operational control over distributed applications.

