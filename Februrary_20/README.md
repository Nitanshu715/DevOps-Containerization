# Docker Swarm & Advanced Networking Lab

### Bridge Networking • Overlay Networks • Swarm Services • Service Scaling • Macvlan Networking

---

# Overview

This laboratory exercise explores Docker networking from foundational container networking to advanced orchestration networking using Docker Swarm.

The experiment demonstrates how containers communicate within custom networks, how distributed networking works using overlay networks, how services are deployed and scaled using Swarm orchestration, and how advanced networking drivers like macvlan function.

The lab also explores networking limitations within Docker Desktop environments and explains how Docker manages container networking internally.

---

# Objectives

- Understand Docker networking architecture
- Create and manage custom Docker bridge networks
- Enable container-to-container communication
- Demonstrate Docker's internal DNS resolution
- Initialize and configure Docker Swarm
- Deploy and manage overlay networks
- Create scalable Docker services
- Scale services dynamically using Swarm
- Understand production overlay networking
- Attempt advanced macvlan networking configuration
- Analyze networking driver behavior and limitations

---

# System Configuration

Operating System  
Windows 11

Docker Environment  
Docker Desktop (Linux backend VM)

Docker Engine Version  
29.x

Swarm Mode  
Enabled

Networking Drivers Used

- bridge
- overlay
- macvlan
- host

Container Images Used

- nginx
- alpine
- busybox

---

# Docker Networking Architecture

Docker provides multiple networking drivers which allow containers to communicate within different scopes and architectures.

Bridge networks provide isolated container communication on a single host.  
Overlay networks enable multi-host communication across Docker Swarm clusters.  
Macvlan networks allow containers to receive real LAN IP addresses.  
Host networking removes isolation and shares the host network stack.

Understanding these networking models is essential for modern DevOps infrastructure, distributed systems, and cloud-native applications.

---

# Part 1 — Creating a Custom Bridge Network

Create a user-defined bridge network which provides automatic DNS resolution and network isolation between containers.

```cmd
docker network create my_app_net
```

Verify network creation:

```cmd
docker network ls
```

Expected Result

A new bridge network named **my_app_net** appears in the list.

User-defined bridge networks provide:

- container isolation
- automatic DNS resolution
- service discovery
- simplified communication

---

# Part 2 — Running Containers Inside Custom Network

Deploy a web server container inside the custom network.

```cmd
docker run -d --name web --network my_app_net nginx
```

Deploy a utility container for testing network connectivity.

```cmd
docker run -d --name utils --network my_app_net alpine sleep 3600
```

Verify running containers:

```cmd
docker ps
```

Expected Output

Both containers should appear as running.

---

# Part 3 — Container-to-Container Communication

Verify that containers inside the same network can communicate using container names.

Ping nginx container from the alpine container.

```cmd
docker exec utils ping web
```

Expected Output

ICMP responses from the nginx container.

Test HTTP communication using wget.

```cmd
docker exec utils wget -qO- http://web
```

Expected Result

The nginx HTML welcome page should be returned.

This confirms that Docker's internal DNS successfully resolves the container name.

---

# Part 4 — Docker Swarm Initialization

Docker Swarm enables clustering and orchestration of containers.

Initialize swarm mode on the node.

```cmd
docker swarm init
```

Verify swarm node status.

```cmd
docker node ls
```

Expected Output

The current node should display:

- Status: Ready
- Manager Status: Leader

Swarm mode is now active.

---

# Part 5 — Creating an Overlay Network

Overlay networks enable communication between containers across multiple swarm nodes.

Create an attachable overlay network.

```cmd
docker network create -d overlay --attachable my_overlay
```

Verify overlay network.

```cmd
docker network ls
```

Overlay networks are essential for:

- distributed microservices
- scalable cloud applications
- multi-node container communication

---

# Part 6 — Deploying Containers in Overlay Network

Deploy two BusyBox containers inside the overlay network.

```cmd
docker run -dit --name app1 --network my_overlay busybox sh
```

```cmd
docker run -dit --name app2 --network my_overlay busybox sh
```

Verify communication between overlay containers.

```cmd
docker exec app1 ping app2
```

Expected Result

Containers communicate successfully using internal IP addresses.

---

# Part 7 — Creating a Docker Service

Docker services allow containers to be orchestrated and managed by the swarm scheduler.

Create a web service using nginx.

```cmd
docker service create --name web -p 8080:80 nginx
```

Verify services.

```cmd
docker service ls
```

Inspect service tasks.

```cmd
docker service ps web
```

Access service using browser.

http://localhost:8080

Expected Result

The nginx welcome page should be displayed.

---

# Part 8 — Scaling Docker Services

Docker Swarm automatically distributes service replicas across the cluster.

Scale the service to four replicas.

```cmd
docker service scale web=4
```

Verify service scaling.

```cmd
docker service ps web
```

Expected Output

Four running tasks representing four container replicas.

Swarm ensures the desired state is maintained automatically.

---

# Part 9 — Creating Production Overlay Network

Production environments often use separate networks for services.

Create a production overlay network.

```cmd
docker network create -d overlay prod_net
```

Verify network.

```cmd
docker network ls
```

This network can be used for large-scale service deployments.

---

# Part 10 — Macvlan Networking (Advanced)

Macvlan networks allow containers to receive real IP addresses from the LAN.

Attempt to create macvlan network.

```cmd
docker network create -d macvlan ^
--subnet=192.168.1.0/24 ^
--gateway=192.168.1.1 ^
-o parent=Ethernet ^
my_macvlan
```

Expected Behavior

On Docker Desktop environments this may return:

invalid subinterface vlan name Ethernet

Reason

Docker Desktop runs containers inside a Linux virtual machine.  
Macvlan requires direct access to the host network interface.

Since the VM abstracts the physical interface, macvlan networking cannot function normally in Docker Desktop.

Macvlan typically works only on native Linux installations.

---

# Docker Networking Driver Comparison

| Driver | Scope | Primary Purpose | Characteristics |
|------|------|------|------|
| Bridge | Local | Container networking on single host | Default Docker networking |
| Overlay | Swarm | Multi-host container communication | Used for distributed systems |
| Macvlan | Local | Direct LAN IP assignment | Requires physical interface |
| Host | Local | Host-level networking | No container isolation |

---

# Experimental Results

- Custom bridge network successfully created
- Containers communicated using Docker DNS
- HTTP requests between containers verified
- Docker Swarm initialized successfully
- Overlay network deployed
- Containers communicated across overlay network
- Docker service deployed successfully
- Service scaled to four replicas
- Production overlay network created
- Macvlan networking attempted and analyzed

---

# Key Observations

- User-defined bridge networks provide automatic DNS resolution.
- Overlay networks enable distributed container communication.
- Docker Swarm manages service orchestration and scaling.
- Services maintain desired replica counts automatically.
- Macvlan networking requires direct access to host interfaces.
- Docker Desktop limitations affect certain networking drivers.

---

# Conclusion

This lab demonstrated Docker networking concepts ranging from simple container communication to advanced orchestration networking.

Bridge networks provide isolated communication between containers, while overlay networks enable scalable distributed systems. Docker Swarm services introduce orchestration capabilities that allow applications to scale dynamically across cluster nodes.

Although macvlan networking could not be fully demonstrated due to Docker Desktop limitations, the experiment highlights how advanced networking drivers function in production environments.

This exercise provides a strong conceptual and practical foundation for DevOps engineers working with containerized infrastructure, microservices architectures, and cloud-native deployments.

