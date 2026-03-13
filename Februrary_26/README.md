# Scaling Services using Docker Compose

---

# 📘 Overview

This practical demonstrates how Docker Compose can be used to deploy and scale services in a multi-container environment.  
The experiment involves deploying a WordPress application backed by a MySQL database and then scaling the WordPress service using Docker Compose.

Docker Compose simplifies orchestration by allowing multiple services to be defined in a single configuration file.  
With the `--scale` option, developers can easily replicate containers to simulate distributed system behavior.

---

# 🎯 Objective

- Deploy a multi-container WordPress application
- Use Docker Compose for container orchestration
- Configure service dependencies
- Use persistent storage via Docker volumes
- Create a custom Docker network
- Scale WordPress containers using `--scale`
- Observe container replication and networking behavior

---

# 🧰 Technologies Used

- Docker Desktop
- Docker Compose
- WordPress Docker Image
- MySQL Docker Image
- Windows Command Prompt
- Git & GitHub

---

# 🖥️ System Configuration

| Component | Details |
|----------|--------|
| Operating System | Windows 11 |
| Docker Version | Latest |
| Container Runtime | Docker Engine |
| Orchestration Tool | Docker Compose |
| Architecture | Multi-container environment |

---

# 📁 Project Directory Structure

```
compose-scaling-26feb/
│
├── docker-compose.yml
├── README.md
└── screenshots/
```

---

# ⚙️ Step 1 — Create Project Directory

```cmd
mkdir DevOps-Labs
cd DevOps-Labs
mkdir compose-scaling-26feb
cd compose-scaling-26feb
```

---

# ⚙️ Step 2 — Create docker-compose.yml File

```cmd
notepad docker-compose.yml
```

Paste the following configuration:

```yaml
services:

  mysql:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: secret
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wpuser
      MYSQL_PASSWORD: wppass
    volumes:
      - mysql_data:/var/lib/mysql
    networks:
      - wordpress-network

  wordpress:
    image: wordpress:latest
    ports:
      - "8080:80"
    environment:
      WORDPRESS_DB_HOST: mysql
      WORDPRESS_DB_USER: wpuser
      WORDPRESS_DB_PASSWORD: wppass
      WORDPRESS_DB_NAME: wordpress
    volumes:
      - wp_content:/var/www/html/wp-content
    depends_on:
      - mysql
    networks:
      - wordpress-network

volumes:
  mysql_data:
  wp_content:

networks:
  wordpress-network:
```

---

# 🐳 Step 3 — Start the Containers

```cmd
docker compose up -d
```

This command:

- Pulls required images from Docker Hub
- Creates containers
- Creates network
- Creates volumes
- Runs containers in detached mode

---

# 🔍 Step 4 — Verify Running Containers

```cmd
docker ps
```

Expected output:

```
mysql
wordpress
```

This confirms both containers are running successfully.

---

# 🌐 Step 5 — Access WordPress Application

Open your browser and visit:

```
http://localhost:8080
```

This launches the WordPress setup page.

---

# 📈 Step 6 — Scale WordPress Containers

Docker Compose allows services to be replicated.

Run the following command:

```cmd
docker compose up -d --scale wordpress=3
```

This creates:

```
wordpress-1
wordpress-2
wordpress-3
```

All containers connect to the same MySQL database.

---

# 🔎 Step 7 — Verify Scaling

```cmd
docker ps
```

Example output:

```
compose-scaling-26feb-wordpress-1
compose-scaling-26feb-wordpress-2
compose-scaling-26feb-wordpress-3
mysql
```

This confirms that multiple WordPress instances are running.

---

# 🌐 Step 8 — Inspect Docker Networks

```cmd
docker network ls
```

Docker Compose automatically creates a bridge network for communication between containers.

Expected network:

```
compose-scaling-26feb_wordpress-network
```

---

# 💾 Step 9 — Inspect Docker Volumes

```cmd
docker volume ls
```

Expected volumes:

```
mysql_data
wp_content
```

Volumes ensure persistent storage even if containers are removed.

---

# 🛑 Step 10 — Stop and Remove Containers

```cmd
docker compose down
```

This command:

- Stops containers
- Removes containers
- Removes networks

Volumes remain unless manually deleted.

---

# 🔗 GitHub Version Control

Initialize Git repository:

```cmd
git init
```

Add files:

```cmd
git add .
```

Commit changes:

```cmd
git commit -m "Docker Compose WordPress Scaling Lab"
```

Connect to GitHub:

```cmd
git remote add origin https://github.com/YOUR_USERNAME/DevOps-Lab-Assignments.git
git branch -M main
git push -u origin main
```

---

# 📊 Observations

- Docker Compose created containers automatically
- Containers were connected using a custom bridge network
- Volumes ensured persistent storage
- Scaling worked using the `--scale` command
- Multiple WordPress containers shared a single MySQL database

---

# 🧠 Key Concepts Learned

- Multi-container architecture
- Docker Compose orchestration
- Container scaling
- Container networking
- Persistent volumes
- Service dependency management

---

# ✅ Result

The WordPress service was successfully deployed and scaled to multiple instances using Docker Compose.

Multiple containers were created and connected to the same MySQL database through a shared network.

---

# 🏁 Conclusion

This experiment demonstrated the power of Docker Compose in orchestrating multi-container applications.  
By using a single configuration file, developers can deploy complex application architectures and scale services efficiently.

Service scaling using Docker Compose forms the foundation for more advanced container orchestration platforms such as Kubernetes.

