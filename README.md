# Containerization & DevOps Lab  
### *Master Repository for All Experiments*

---

<p align="center">
  <b>Course:</b> Containerization and DevOps<br/>
  <b>Focus:</b> Virtualization, Containers, CI/CD, Cloud-Native Systems<br/>
</p>

---
<p align="center">
  <b>Name:</b> Nitanshu Tak <br/>
  <b>SapID:</b> 500121943 <br/>
  <b>Course:</b> BTech. CSE (CCVT) <br/>
  <b>Batch:</b> 2 <br/>
</p>

## About This Repository

This repository serves as the **master lab repository** for the subject  
**Containerization and DevOps**.

Each experiment is organized in its **own folder**, containing:
- Experiment-specific source files
- Individual README documentation
- Commands, configurations, and outputs
- Observations and results

This structure reflects **real-world DevOps repositories**, where infrastructure,
automation, and documentation coexist in a clean, scalable manner.

---

## Why This Repository Exists

Modern software systems require:
- Fast deployment
- Scalability
- Automation
- Reproducibility

This lab repository demonstrates **hands-on implementation** of:
- Infrastructure as Code (IaC)
- Virtualization vs Containerization
- Linux system administration
- Docker-based application deployment
- DevOps best practices

---


## Lab Experiments Performed

### Experiment 1 — Virtual Machines vs Containers  
A DevOps-oriented comparison between Virtual Machines and Containers using:

- Ubuntu  
- VirtualBox  
- Vagrant  
- Docker  
- Nginx  

This experiment demonstrates:

- Infrastructure provisioning  
- VM-based deployment workflow  
- Containerized service execution  
- Architectural differences in isolation and performance  

Link: [Experiment 1 — Virtual Machines vs Containers](./Experiment-1/)

### Experiment 2 — Docker Installation & Container Lifecycle  
This experiment covers the fundamentals of Docker including:

- Pulling images  
- Running containers with port mapping  
- Verifying services in browser  
- Resolving port conflicts  
- Container start/stop/remove lifecycle commands  

Link: [Experiment 2 — Docker Installation & Container Lifecycle](./Experiment-2/)

### Experiment 3 — Custom Docker Images (Ubuntu & Alpine Based NGINX)
This experiment focuses on building custom Docker images using different Linux base images and deploying NGINX inside containers.
Base Images Used:
- Ubuntu 22.04
- Alpine Linux

This experiment demonstrates:
- Writing Dockerfiles for custom image creation
- Installing services inside containers (NGINX)
- Building Docker images using custom SAP-based tags
- Running multiple containers with different port mappings
- Comparing Ubuntu vs Alpine image size and performance
- Understanding lightweight container optimization

Key Implementation:
- Official NGINX container → Port 8080
- Ubuntu-based custom container → Port 8081
- Alpine-based custom container → Port 8082

Link: [Experiment 3 — Custom Docker Images (Ubuntu & Alpine Based NGINX)](./Experiment-3/)


### Experiment 4 - Containerization using Dockerfile, .dockerignore, Tagging & Publishing
The experiment was successfully completed by containerizing both a Python Flask application and a Node.js Express application using Docker. The following outcomes were achieved:

- Docker images were built successfully using custom Dockerfile.
- .dockerignore was implemented to optimize image size and security.
- Containers were executed with proper port mapping.
- Multi-stage build was implemented to optimize production image size.
- Docker images were successfully tagged and published to Docker Hub.
- The published image was pulled and executed successfully from Docker Hub.
- Both applications were accessible via browser:
- Flask App → http://localhost:5001
- Node App → http://localhost:3000
- The Docker workflow from build → run → tag → push → pull → run was validated successfully.

Link: [Experiment 4 - Docker Networking, Volumes & Environment Variables Lab](./Experiment-4/)

### Experiment 5 - Containerization using Dockerfile, .dockerignore, Tagging & Publishing
- All objectives of Experiment 5 were successfully completed.
The experiment demonstrated a practical understanding of:
- Docker networking architecture
- Persistent storage management
- Secure configuration handling using environment variables
- Runtime configuration override
- Container monitoring and debugging tools
- The implementation validates correct container orchestration principles and production-ready configuration practices.

Link: [Experiment 5 - Docker Networking, Volumes & Environment Variables Lab](./Experiment-5/)

---


## Class Practicals performed

### Class Practical — 21 January (DevOps Fundamentals & Setup)
A date-wise practical session focused on understanding and implementing core DevOps foundations through hands-on exercises using:
- Linux Environment
- Basic Shell Commands
- Docker Introduction
- Container Execution
- DevOps Workflow Setup

Link:
[Class Practical 21 Jan](./January_21/)

### Class Practical — 22 January (Docker Basics & Container Management)
A date-wise practical session focused on exploring Docker core concepts and managing containers through hands-on classroom implementation using:
- Docker CLI Commands
- Container Lifecycle Operations
- Image Pulling and Execution
- Basic Container Monitoring
- Practical DevOps Environment Setup

Link:
[Class Practical 22 Jan](./January_22/)

### Class Practical — 23 January (Docker Networking & Multi-Container Basics)
A date-wise practical session focused on understanding Docker networking concepts and working with multiple containers through hands-on classroom exercises using:
- Docker Network Commands
- Bridge Networking Mode
- Container-to-Container Communication
- Port Mapping and Exposure
- Multi-Service Deployment Basics

Link:
[Class Practical 23 Jan](./January_23/)

### Class Practical — 27 January (Docker Volumes & Persistent Storage)
A date-wise practical session focused on understanding Docker data persistence concepts and managing storage using hands-on classroom implementation through:
- Docker Volume Creation
- Persistent Data Handling
- Bind Mounts vs Volumes
- Container Storage Management
- Practical Stateful Container Setup

Link:
[Class Practical 27 Jan](./January_27/)

### Class Practical — 28 January (Docker Compose & Multi-Service Deployment)
A date-wise practical session focused on learning Docker Compose and deploying multi-container applications through structured classroom exercises using:
- Docker Compose YAML Configuration
- Multi-Container Service Setup
- Container Orchestration Basics
- Automated Service Deployment
- DevOps Application Structuring

Link:
[Class Practical 28 Jan](./January_28/)

### Class Practical — 30 January (Dockerfile Creation & Image Building)
A date-wise practical session focused on understanding Dockerfile instructions and building custom Docker images through hands-on classroom implementation using:
- Dockerfile Syntax and Commands
- Custom Image Creation
- Layer-Based Image Architecture
- Building and Running Containers from Images
- DevOps Application Packaging Workflow

Link:
[Class Practical 30 Jan](./January_30/)

### Class Practical — 3 Feb (Docker Installation Verification & Nginx Deployment)
A practical session focused on verifying Docker Desktop setup, testing Docker Engine connectivity through CLI and REST API, and deploying a production-ready Nginx container through hands-on implementation using:
- Docker Installation Verification (macOS Apple Silicon)
- Docker Engine & Daemon Connectivity Testing
- Docker CLI and REST API Container Inspection
- Unix Socket Communication with Docker Engine
- Nginx Container Pulling and Deployment
- Container Lifecycle Understanding (Create, Run, Inspect)
- DevOps Container Deployment Workflow

Link:
[Class Practical 3 Feb](./Februrary_03/)

### Class Practical — 4 Feb (Docker Engine Configuration & Remote API Access)
A hands-on practical session focused on configuring Docker Engine, enabling Remote API communication, and validating daemon connectivity through CLI and UNIX socket testing using:
- Docker Engine Configuration using daemon.json
- Docker Remote API Enablement (TCP + UNIX Socket)
- Docker Installation & Engine Status Verification
- Docker CLI and CURL-Based API Testing
- Docker Daemon Connectivity Validation
- Sample Container Deployment (hello-world)
- Docker Client–Server Architecture Understanding
- DevOps Engine-Level Configuration Workflow
  
Link:
[Class Practical 4 Feb](./Februrary_04/)

### Class Practical Test — 5 Feb (Containerizing Python SAP ID Verification Application)
A hands-on class test focused on containerizing a Python-based SAP ID verification application using Docker, demonstrating real-world application packaging and execution inside containers through implementation using:
- Official Docker Base Image (Python 3.10 Slim)
- Python Application Containerization Workflow
- Dependency Installation inside Container (NumPy)
- Custom Docker Image Building
- Interactive Container Execution
- Application Testing inside Container Environment
- Image vs Container Concept Understanding
- DevOps Application Packaging and Deployment Workflow

Link:
[Class Practical Test 5 Feb](./Februrary_05/)

### Class Practical — 6 Feb (Running Python Application Using Docker Volume Mount (Continuous Runtime))
A hands-on practical session focused on executing a containerized Python application using Docker volume mounting for dynamic runtime execution, demonstrating real-world development workflow through implementation using:
- Official Docker Base Image (Python 3.10 Slim)
- Docker Volume Mounting (Host ↔ Container File Sharing)
- Runtime File Injection without Image Rebuild
- Continuous Input Execution using While Loop
- Interactive Container Runtime Testing
- Runtime Error Debugging (Missing File Handling)
- COPY vs Volume Mount Concept Understanding
- Real-World Containerized Development Workflow
  
Link:
[Class Practical 6 Feb](./Februrary_06/)

### Class Practical — 6 Feb Assignment (Running C Application Using Docker Volume Mount (Runtime Compilation & Continuous Execution))
A hands-on practical session focused on compiling and running a containerized C application using Docker volume mounting for dynamic runtime execution, demonstrating multi-language container workflows through implementation using:
- Official Docker Base Image (GCC Latest)
- Containerized C Program Compilation and Execution
- Docker Volume Mounting (Host ↔ Container File Sharing)
- Runtime Source Code Injection without Image Rebuild
- Continuous Input Execution using Infinite Loop
- Interactive Container Runtime Testing
- Build-Time vs Runtime Compilation Understanding
- Multi-Language Containerized Development Workflow

Link:
[Class Practical 6 Feb Assignment](./Februrary_06/)

### Class Practical — 10 Feb (C Application Containerization & Optimization)
A hands-on practical series focused on building, running, and optimizing containerized C applications using Docker. This included runtime execution using volume mounts and production-level image optimization using multi-stage builds and minimal scratch runtime images. The practical demonstrated real-world container development workflows through implementation using:
- Official Docker Base Images (Ubuntu, GCC Toolchain)
- Containerized C Program Compilation and Execution
- Docker Volume Mounting (Host ↔ Container Runtime Source Injection)
- Runtime Compilation and Continuous Execution using Infinite Loop
- Interactive Container Testing using Terminal Input
- Build-Time vs Runtime Execution Understanding
- Multi-Stage Docker Build Optimization
- Static Binary Compilation for Minimal Containers
- Scratch-Based Ultra-Lightweight Production Images
- Multi-Language Containerized Development Workflow (Python + C)

Link:
[Class Practical 10 Feb](./Februrary_10/)

### Class Practical — 10 Feb Assignment (Multi-Stage Build for Java Application with Secure Runtime Container)
A hands-on practical session focused on implementing enterprise-grade Docker container build workflows using multi-stage builds for Java applications. This practical demonstrated real-world production container optimization by separating build and runtime environments, reducing image size, and improving container security using non-root user implementation through execution using:
- Docker Engine & Environment Verification (docker --version, docker ps, docker images)
- Java Project Structure Creation Using Maven Standards
- Java Application Compilation Using Maven Build Tool
- Multi-Stage Dockerfile Implementation (Builder Stage + Runtime Stage)
- Builder Environment Using Maven + OpenJDK for Application Compilation
- Runtime Environment Using Production-Ready Eclipse Temurin JRE Base Image
- Copying Only Compiled Application Artifacts (JAR) to Runtime Container
- Secure Container Execution Using Non-Root User Configuration
- Docker Image Build Using Multi-Stage Optimization
- Docker Image Size Verification and Runtime Optimization Comparison 
- Running Java Application Inside Optimized Runtime Container
- Docker Image Layer Analysis Using docker history Command
- Understanding Builder Layer Removal in Final Runtime Image
- BuildKit Layer Caching and Container Layer Optimization Understanding
- Production Container Security and Enterprise Container Design Workflow

Link:
[Class Practical 10 Feb Assignment](./Februrary_10/)


### Class Practical — 11 Feb (Docker Volume Management & Data Persistence)
A hands-on practical session focused on implementing Docker storage mechanisms using named volumes and bind mounts to enable persistent data management between host and container environments. This practical demonstrated real-world container storage workflows through implementation using:
- Docker Engine & Environment Verification (docker info, docker images)
- Docker Named Volume Creation and Management
- Docker Volume Listing and Inspection
- Running Containers with Named Volumes
- Container ↔ Volume Data Persistence Testing
- Writing and Reading Files Inside Container Storage
- Bind Mount Implementation (Host Directory ↔ Container Directory Mapping)
- Runtime File Creation and Host-Level Verification
- Temporary Container Execution using --rm
- Linux File System Navigation Inside Containers
- Container Data Lifecycle and Persistence Understanding
- Real-World DevOps Storage Workflow Implementation

Link:
[Class Practical 11 Feb](./Februrary_11/)


### Class Practical — 11 Feb Assignment (Volume Backup, Restore & Inspection Using TAR & Named Volumes)
A hands-on practical session focused on implementing advanced Docker storage management by performing volume data backup, restoration, and inspection using TAR-based archival and named Docker volumes. This practical demonstrated real-world container storage backup and disaster recovery workflows through implementation using:
- Docker Engine & Environment Verification (docker --version, docker info, docker volume ls)
- Docker Named Volume Creation and Management
- Running Containers with Named Volumes for Persistent Storage
- Writing and Verifying Data Inside Docker Volume Storage
- Volume Data Backup Using TAR Archive Utility
- Bind Mount Backup Directory Implementation (Host ↔ Container Mapping)
- Volume Deletion to Simulate Production Data Loss Scenario
- Volume Recreation and Data Restoration from Backup Archive
- Restored Data Verification Inside Container Environment
- Docker Volume Metadata Inspection Using docker volume inspect
- Backup Storage Size Verification Using Linux Disk Usage Commands
- Understanding Docker Volume Mountpoints and Storage Locations
- Container Storage Backup and Disaster Recovery Workflow Simulation
- Real-World DevOps Storage Backup and Recovery Implementation
  
Link:
[Class Practical 11 Feb Assignment](./Februrary_11/)

### Class Practical — 12 Feb (Docker Volumes, Bind Mounts, tmpfs & MySQL Persistence)
This class focused on understanding Docker storage mechanisms by working with named volumes, bind mounts, and tmpfs mounts, along with implementing persistent storage for a MySQL container.
- Verified Docker setup using docker info
- Created a named Docker volume (myvolume)
- Ran a MySQL container with volume-based persistent storage
- Stopped and removed the container to verify data persistence
- Re-ran MySQL using the same volume to confirm database recovery
- Inspected volume details using docker volume inspect
- Implemented Bind Mount with NGINX for live file sharing
- Demonstrated tmpfs mount for temporary in-memory storage
- Compared Volume vs Bind Mount vs tmpfs behavior


Link:
[Class Practical 12 Feb](./Februrary_12/)


### Class Practical — 18 Feb (Docker Networking — Bridge, Custom Network & Container Communicatione)
This class focused on understanding Docker networking concepts by working with default bridge networks, creating custom user-defined bridge networks, and enabling inter-container communication.
- Inspected default Docker networks (bridge, host, none)
- Analyzed network configuration using docker network inspect
- Created a custom bridge network (my_bridge)
- Launched multiple containers (nginx, busybox) inside the same network
- Verified container-to-container communication using ping
- Inspected container network settings and IP assignments
- Tested host network mode behavior
- Observed networking differences between default and user-defined bridge networks

Link:
[Class Practical 18 Feb](./Februrary_18/)

### Class Practical — 20 Feb (Docker Swarm & Advanced Networking Lab — Bridge, Overlay, Services & Macvlan)
This lab focused on understanding Docker networking from basic container communication to advanced Swarm-based networking, including overlay networks, service scaling, and macvlan configuration.
- Created a custom bridge network (my_app_net)
- Launched multiple containers (nginx, alpine) inside the same network
- Verified container-to-container communication using ping and wget
- Initialized Docker Swarm using docker swarm init
- Created an attachable overlay network (my_overlay)
- Deployed standalone containers inside overlay network and tested connectivity
- Created a Docker service (web) and exposed it on port 8080
- Scaled service to 4 replicas using docker service scale
- Inspected running services and tasks using docker service ls and docker service ps
- Created a production overlay network (prod_net)
- Configured a macvlan network with custom subnet and gateway
- Assigned a static IP to a container using macvlan
- Tested external connectivity using curl
- Troubleshot port conflicts and active endpoint issues
- Compared bridge, overlay, host, and macvlan networking behavior

Link:
[Class Practical 20 Feb](./Februrary_20/)

### Class Practical — 23 February (Docker Image Management & Container Lifecycle)
This class practical demonstrated the fundamental concepts of Docker image management and container lifecycle operations.
- Docker images can be pulled from Docker Hub repositories.
- Containers can be created and executed from Docker images.
- Running and stopped containers can be inspected using Docker CLI commands.
- Containers can be started, stopped, restarted, and removed easily.
- Docker images can be listed, inspected, and deleted when no longer required.
- Docker enables lightweight and isolated environments for application execution.
- The container lifecycle helps developers efficiently manage application environments.

Link:
[Class Practical 23 Feb](./Februrary_23/)

### Class Practical — 25 Feb (Docker Compose – Nginx & WordPress with MySQL)
This class practical successfully demonstrated the working of Docker Compose for both single-container and multi-container applications. Using Docker Compose:
- Multiple services can be managed using a single YAML file.
- Networking between containers is automatically handled.
- Persistent storage can be managed easily using volumes.
- Full application stack (WordPress + MySQL) can be deployed with a single command.
- Docker Compose makes container orchestration simple, structured, and efficient for real-world application deployment.

Link:
[Class Practical 25 Feb](./Februrary_25/)


### Class Practical — 26 Feb (Scaling Services using Docker Compose)
This experiment demonstrated how Docker Compose can scale services easily using the --scale flag.
- It also highlighted important practical constraints:
- Each container must have a unique name.
- Only one container can bind to a specific host port.
- Scaling backend services usually requires a load balancer.
- Docker Compose simplifies multi-container orchestration and service replication, making it useful for real-world distributed application deployment.

Link:
[Class Practical 26 Feb](./Februrary_26/)

### Class Practical — March 18 (Kubernetes Setup using k3d)

A practical session focused on setting up a local Kubernetes cluster using k3d and performing core orchestration tasks including deployment, service exposure, scaling, and verification.

Kubernetes cluster was successfully created locally using k3d
Cluster connectivity was configured and verified using kubectl
Node status was validated and confirmed in Ready state
Nginx application was deployed using a Kubernetes Deployment
Pods were automatically created and managed by the Deployment
Service was exposed using NodePort for external access
Application scaling was performed to run multiple replicas
Deployment state and configuration were verified using describe
Container logs were inspected for runtime validation
Port forwarding was used to enable browser access
Application output was successfully verified in browser

This practical demonstrates fundamental Kubernetes operations including cluster setup, deployment, scaling, service exposure, and debugging.

Link:
[Class Practical 18 Mar](./March_18/)

### Class Practical - March 19 (Kubernetes Deployment & Service Exposure)

A practical session focused on deploying an application in Kubernetes, managing pods, scaling deployments, exposing services, and verifying outputs using kubectl commands.

Application was deployed using Kubernetes Deployment resource
Pods were automatically created and managed by the Deployment controller
Deployment was scaled to multiple replicas demonstrating horizontal scaling
Service was exposed using NodePort for external communication
Application was accessed using port-forwarding in local environment
Deployment configuration and state were verified using describe command
Container logs were inspected for runtime validation
All cluster resources were validated using kubectl get all
Common errors were identified and resolved during execution

This practical demonstrates core Kubernetes concepts including deployment, scaling, service exposure, and debugging workflows.

Link:
[Class Practical 19 Mar](./March_19/)

### Class Practical - March 20 (Docker & Portainer Setup)

A practical session focused on Docker container management and deploying Portainer for GUI-based container orchestration.

Docker environment was verified using CLI commands  
Kubernetes context was checked and validated  
Portainer volume was created for persistent storage  
Portainer container was deployed and verified running  
Web interface was accessed securely via HTTPS  
Admin configuration and local Docker environment setup completed  
Containers, images, volumes, and networks were managed through GUI  
Real-time monitoring and container inspection were performed  
Minikube limitations were identified in certain environments  

This practical demonstrates Docker container management and GUI-based orchestration using Portainer.

Link:
[Class Practical 20 Mar](./March_20/)

### Class Practical - March 25 (Apache Web Application on Kubernetes)

A practical session focused on deploying and managing an Apache web server on Kubernetes, covering pod lifecycle, deployment management, service exposure, scaling, debugging, and live container modification.

Apache application was deployed using both Pod and Deployment approaches
Pod behavior and lifecycle were verified using Kubernetes CLI commands
Application was accessed locally using port-forwarding
Deployment was created to manage pods in a controlled and scalable manner
Service was exposed to enable network access to the application
Application scaling was performed to run multiple replicas
Failure scenario was simulated using incorrect image configuration
Deployment was debugged and restored to a healthy state
Live container content was modified using exec command
Self-healing capability was verified by deleting pods and observing automatic recreation

This practical demonstrates real-world Kubernetes capabilities including deployment control, scaling, debugging, and self-healing mechanisms.

Link:
[Class Practical 25 Mar](./March_25/)

### Class Practical - March 27 (Imperative vs Declarative Deployment)

A practical session focused on understanding and implementing imperative and declarative approaches in Kubernetes by deploying and managing an NGINX application.

Deployment was created using imperative command-based approach
Application resources were verified using kubectl commands
YAML configuration file was generated using dry-run method
Deployment configuration was modified using declarative YAML approach
Existing deployment was replaced using declarative configuration
Multiple replicas were created using replica configuration
Deployment state and behavior were verified using describe
Application was accessed using port forwarding
Scaling operation was performed to increase number of pods
Resources were cleaned up after execution

This practical demonstrates the difference between imperative and declarative models and highlights the importance of declarative configuration in Kubernetes for scalability, reproducibility, and version control.

Link:
[Class Practical 27 Mar](./March_27/)

### Class Practical — April 1 (Jenkins on Docker)

A practical session focused on deploying Jenkins using Docker and performing initial CI/CD server setup including configuration, persistence, and validation.

Jenkins server was successfully deployed using Docker Compose
Container was created and managed using Docker runtime
Port mapping was configured to expose Jenkins on localhost
Persistent storage was implemented using Docker volumes
Jenkins was accessed through browser and initial setup was completed
Admin password was retrieved from container for authentication
Plugins were installed to enable CI/CD functionality
User account was created and dashboard was configured
Container logs were verified to ensure proper execution

This practical demonstrates containerized CI/CD server setup, persistent storage handling, and basic Jenkins configuration using Docker.

Link:
[Class Practical 1 Apr](./April_1/)

### Class Practical — April 7 (Git & GitHub SSH Setup)

A practical session focused on configuring Git, setting up SSH authentication with GitHub, and performing version control operations including repository initialization, branching, and remote integration.

Git global configuration was set for user identity
SSH key pair was generated using ED25519 algorithm
Public key was added to GitHub for secure authentication
SSH connection to GitHub was successfully verified
Local repository was initialized and initial commit was created
Branching workflow was implemented using a feature branch
Files were staged, committed, and managed using Git
Remote repository was connected using SSH protocol
Code was successfully pushed to GitHub for both main and feature branch

This practical demonstrates secure GitHub authentication, efficient version control workflows, and branch-based development using Git.

Link:
[Class Practical 7 Apr](./April_7/)


### Class Practical — 10 Apr (FastAPI CI/CD Pipeline — Docker & GitHub Actions Integration)
This practical demonstrates the implementation of an end-to-end CI/CD pipeline by containerizing a FastAPI application and automating its build and deployment using GitHub Actions.
- Developed a FastAPI application and containerized it using Docker for consistent and portable deployment  
- Implemented a CI/CD pipeline using GitHub Actions to automate image build and push on every code update  
- Integrated Docker Hub as a container registry for storing and managing versioned images  
- Secured authentication using GitHub Secrets to handle Docker credentials safely  
- Designed a modular workflow that targets only the April_10 project within a multi-experiment repository  
- Validated deployment by running the containerized application and verifying output through browser access  

Link:
[Class Practical 10 Apr](./April_10/)

---

## Technologies & Tools Used

```text
Operating Systems:
- Ubuntu Linux
- Windows (Host)

Virtualization:
- Oracle VirtualBox
- Vagrant

Containerization:
- Docker Engine
- Docker CLI

Networking & Services:
- Nginx

DevOps Concepts:
- Infrastructure as Code (IaC)
- Automation
- CI/CD
- Cloud-Native Architecture
```

---

## Learning Outcomes

By completing all experiments in this repository, the learner will be able to:

- Understand differences between VMs and containers
- Deploy applications in isolated environments
- Automate infrastructure provisioning
- Use Docker for container-based deployment
- Follow DevOps-style repository organization
- Apply concepts used in real-world DevOps roles

---

## How to Use This Repository

```bash
# Clone repository
git clone https://github.com/<your-username>/containerization-and-devops-lab.git

# Navigate to an experiment
cd experiment-01-vm-vs-container

# Read experiment-specific documentation
cat README.md
```

---

## DevOps Mindset Demonstrated

This repository reflects:
- Modular design
- Clear documentation
- Automation-first thinking
- Scalability
- Industry-aligned practices

The structure and workflow mirror professional DevOps projects,
making this repository suitable for **academic evaluation** as well as **portfolio use**.

---

## Future Enhancements

- GitHub Actions CI pipelines
- Docker image versioning
- Kubernetes basics
- Cloud deployment (AWS / Azure / GCP)
- Monitoring & logging integration

---

## Author

**Name:** Nitanshu  
**Program:** B.Tech Computer Science Engineering  
**Specialization:** Cloud Computing & Virtualization Technology  
**Focus Areas:** DevOps · Cloud · Automation · Linux

---

## Final Note

This repository is not just a lab submission —  
it is a **foundation for real DevOps engineering practices**.

Build it. Improve it. Ship it. 
