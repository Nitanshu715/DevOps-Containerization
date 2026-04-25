# Experiment 11 - Docker Swarm Orchestration with WordPress

## 1. Introduction

Docker Swarm is a native clustering and orchestration tool provided by Docker. It allows multiple Docker nodes to be grouped together to form a cluster, enabling the deployment and management of applications across multiple containers and machines. Unlike standalone Docker containers or Docker Compose, Docker Swarm introduces orchestration capabilities such as scaling, load balancing, and self-healing.

In this experiment, we implement a real-world multi-container application using Docker Swarm. The application consists of a WordPress service connected to a MySQL database. The WordPress service is deployed with multiple replicas to demonstrate scaling and load balancing, while the MySQL service provides persistent data storage.

This experiment highlights the transition from simple container execution to production-level orchestration concepts.

---

## 2. Objectives

The objectives of this experiment are:

- To understand Docker Swarm architecture and working
- To deploy a multi-container application using docker stack
- To compare Docker Compose and Docker Swarm
- To implement service scaling using replicas
- To demonstrate internal load balancing
- To test self-healing by manually terminating a container
- To observe automatic container recovery
- To understand service-based deployment in Swarm

---

## 3. Prerequisites

Before performing this experiment, the following requirements must be satisfied:

- Docker Desktop installed on Windows
- WSL2 backend enabled
- Basic understanding of Docker commands
- Familiarity with container concepts
- Internet connection for pulling images
- Command Prompt or PowerShell access

---

## 4. System Configuration

- Operating System: Windows with Docker Desktop
- Docker Version: 29.x
- Swarm Mode: Active
- Node Type: Manager
- Number of Nodes: 1
- CPU: 2 cores
- RAM: ~4 GB

---

## 5. Key Concepts

### 5.1 Docker Swarm
Docker Swarm is used to manage a cluster of Docker nodes. It introduces the concept of services instead of individual containers.

### 5.2 Service
A service defines how containers should run, including image, replicas, and networking.

### 5.3 Replica
Replicas represent the number of container instances running for a service.

### 5.4 Load Balancing
Swarm automatically distributes incoming requests across all replicas.

### 5.5 Self-Healing
If a container fails, Swarm automatically replaces it to maintain the desired state.

---

## 6. Architecture

The system consists of:

1. MySQL Service
   - Stores WordPress data
   - Runs as a single container
   - Uses persistent volume

2. WordPress Service
   - Runs as 3 replicas
   - Connects to MySQL
   - Exposed on port 8080

Swarm provides:
- Internal networking
- Service discovery
- Load balancing
- Fault tolerance

---

## 7. Implementation

### Step 1: Initialize Swarm

docker swarm init

---

### Step 2: Create docker-compose.yml

```yaml
version: "3.8"

services:
  db:
    image: mysql:5.7
    environment:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_DATABASE: wordpress
    volumes:
      - db_data:/var/lib/mysql

  wordpress:
    image: wordpress:latest
    ports:
      - "8080:80"
    environment:
      WORDPRESS_DB_HOST: db:3306
      WORDPRESS_DB_USER: root
      WORDPRESS_DB_PASSWORD: root
    deploy:
      replicas: 3

volumes:
  db_data:
```

---

### Step 3: Deploy Stack

docker stack deploy -c docker-compose.yml wpstack

---

### Step 4: Verify Services

docker service ls

---

### Step 5: Check Containers

docker ps

---

### Step 6: Access Application

Open browser:
http://localhost:8080

---

### Step 7: Self-Healing Test

docker kill <container_id>

docker service ps wpstack_wordpress

---

### Step 8: Cleanup

docker stack rm wpstack

---

## 8. Observations

- WordPress ran in 3 replicas
- MySQL ran in 1 replica
- Load balancing handled automatically
- Container recreated after failure
- Application remained accessible

---

## 9. Results

- Multi-container deployment successful
- Scaling verified
- Load balancing verified
- Self-healing verified

---

## 10. Advantages

- Easy orchestration
- Automatic scaling
- Fault tolerance
- Built-in load balancing

---

## 11. Limitations

- Less powerful than Kubernetes
- Limited features
- Not widely used in large-scale production

---

## 12. Conclusion

Docker Swarm provides an efficient and simple way to orchestrate containerized applications. Through this experiment, we demonstrated scaling, load balancing, and self-healing. This makes Docker Swarm suitable for learning orchestration and deploying small to medium applications.

