# Docker Compose: Nginx + WordPress + MySQL

---

## 📌 Overview

This practical demonstrates how **Docker Compose** can be used to manage both **single‑container** and **multi‑container** applications in a structured way.  
Docker Compose allows developers to define an entire application stack using a single **YAML configuration file**, simplifying deployment, networking, and persistent storage management.

In this lab, we deploy:

• A **single container service** using Nginx  
• A **multi‑container stack** consisting of WordPress and MySQL  
• Persistent volumes for database and application data  
• A custom Docker network for inter‑container communication

This experiment demonstrates how real DevOps workflows deploy applications using container orchestration.

---

# 🧠 Learning Objectives

- Understand the concept of **Docker Compose**
- Deploy containers using a **compose YAML file**
- Run a **single‑container service (Nginx)**
- Deploy a **multi‑container stack (WordPress + MySQL)**
- Configure **Docker volumes for persistent storage**
- Configure **Docker networks for service communication**
- Use Docker Compose commands to manage container lifecycle

---

# 🛠 Technologies Used

| Tool | Purpose |
|-----|--------|
| Docker Desktop | Container runtime |
| Docker Compose | Multi‑container orchestration |
| Nginx (Alpine) | Lightweight web server |
| WordPress | Content management system |
| MySQL 8.0 | Relational database |
| Windows Command Prompt | Command execution |
| Git & GitHub | Version control and repository hosting |

---

# 📂 Project Directory Structure

```
Class Practical 25 Feb
│
├── docker-compose.yml
├── docker-compose-wordpress.yml
│
├── html
│   └── index.html
│
└── README.md
```

---

# 🌐 PART 1 — Running Nginx using Docker Compose

## docker-compose.yml

```yaml
services:
  nginx:
    image: nginx:alpine
    container_name: my-nginx
    ports:
      - "8080:80"
    volumes:
      - ./html:/usr/share/nginx/html
    environment:
      - NGINX_HOST=localhost
    restart: unless-stopped
```

---

## 📄 Create HTML Directory

```bash
mkdir html
notepad html/index.html
```

---

## index.html

```html
<!DOCTYPE html>
<html>

<head>
<title>Docker Compose DevOps Lab</title>
</head>

<body>

<h1>🚀 Docker Compose Nginx Server</h1>

<p>This webpage is served using an Nginx container managed by Docker Compose.</p>

<p>This demonstrates how containerized services can be deployed easily using a YAML configuration.</p>

</body>

</html>
```

---

## ▶️ Commands Used

### Start Nginx Container

```bash
docker compose up -d
```

### Verify Running Containers

```bash
docker ps
```

### View Container Logs

```bash
docker compose logs
```

### Stop and Remove Container

```bash
docker compose down
```

---

# 🧩 PART 2 — WordPress + MySQL Multi‑Container Setup

Docker Compose allows multiple services to run together with automatic networking and dependency management.

This stack contains:

• WordPress application container  
• MySQL database container  
• Persistent volumes  
• Custom Docker network

---

## docker-compose-wordpress.yml

```yaml
services:

  mysql:
    image: mysql:8.0
    container_name: mysql
    restart: always
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
    container_name: wordpress
    depends_on:
      - mysql
    ports:
      - "8081:80"
    restart: always
    environment:
      WORDPRESS_DB_HOST: mysql
      WORDPRESS_DB_USER: wpuser
      WORDPRESS_DB_PASSWORD: wppass
      WORDPRESS_DB_NAME: wordpress
    volumes:
      - wp_content:/var/www/html/wp-content
    networks:
      - wordpress-network

volumes:
  mysql_data:
  wp_content:

networks:
  wordpress-network:
```

---

# ⚙️ Docker Compose Commands

### Start WordPress Stack

```bash
docker compose -f docker-compose-wordpress.yml up -d
```

---

### Check Running Services

```bash
docker compose -f docker-compose-wordpress.yml ps
```

---

### List Docker Volumes

```bash
docker volume ls
```

---

### List Docker Networks

```bash
docker network ls
```

---

### Stop and Remove Containers

```bash
docker compose -f docker-compose-wordpress.yml down
```

---

# 🌍 Accessing the Application

Once the containers are running, open the browser:

```
http://localhost:8081
```

The WordPress installation screen will appear where the site configuration can be completed.

---

# 📊 Expected Output

• Nginx container successfully serves a webpage on port **8080**  
• WordPress container connects to MySQL database container  
• Persistent volumes store database and application data  
• Docker automatically creates an internal network between services  
• WordPress application becomes accessible through the browser

---

# 🧠 Concepts Demonstrated

## Docker Compose

Docker Compose allows defining multi‑container applications in a single configuration file.

---

## Container Networking

Docker automatically creates a bridge network allowing containers to communicate via service names.

Example:

```
wordpress → mysql
```

---

## Persistent Storage

Volumes allow container data to persist even after containers are removed.

```
mysql_data
wp_content
```

---

## Service Dependencies

The `depends_on` directive ensures WordPress starts after MySQL.

```yaml
depends_on:
  - mysql
```

---

# 📈 Architecture Diagram

```
        User Browser
              |
              v
        WordPress Container
              |
              v
        MySQL Database Container
              |
              v
         Docker Volumes
```

---

# ✅ Result

The Docker Compose environment successfully deployed:

- A single‑container Nginx web server
- A multi‑container WordPress + MySQL application stack
- Persistent storage using Docker volumes
- Automatic container networking
- Fully functioning WordPress website accessible through the browser

---

# 🏁 Conclusion

This experiment demonstrates how Docker Compose simplifies the deployment of both simple and complex containerized applications. By defining services in a YAML configuration file, developers can quickly deploy full application stacks with networking and storage already configured.

Docker Compose is widely used in modern DevOps pipelines to manage containerized environments efficiently.

