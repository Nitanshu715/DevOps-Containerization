
# Experiment - 6 - Docker Run vs Docker Compose - Detailed Practical Implementation

## Introduction

This experiment focuses on understanding two fundamental approaches to container deployment in Docker: the imperative approach using Docker Run commands and the declarative approach using Docker Compose. The practical demonstrates how both methods can be used to deploy single-container and multi-container applications, highlighting their differences, advantages, and real-world usage.

## Objective

The primary objective of this experiment is to:
- Understand the difference between imperative and declarative container management
- Deploy containers using Docker Run
- Deploy equivalent configurations using Docker Compose
- Implement multi-container applications
- Work with volumes, networks, and dependencies
- Understand how Docker simplifies application deployment

## Prerequisites

- Docker Desktop installed and running
- Basic knowledge of containers
- Command Prompt environment (Windows)
- Internet connectivity for pulling images

## Understanding Docker Run

Docker Run is an imperative way of managing containers where each configuration is specified directly in the command line. It requires users to define ports, environment variables, volumes, and container names explicitly.

Example:
docker run -d -p 8081:80 nginx

## Understanding Docker Compose

Docker Compose uses a declarative YAML-based configuration file to define services. Instead of specifying everything in a command, the desired state is written in a file and executed with a single command.

Example:
docker compose up -d

## Key Differences

Docker Run:
- Imperative
- Command-line based
- Less reusable
- Difficult for multi-container setups

Docker Compose:
- Declarative
- YAML configuration
- Highly reusable
- Ideal for multi-container applications

## Part A - Single Container Deployment

### Using Docker Run

docker run -d --name nginx-container -p 8090:80 nginx:alpine

docker ps

http://localhost:8090

### Using Docker Compose

services:
  nginx:
    image: nginx:alpine
    container_name: nginx-compose
    ports:
      - "8091:80"

docker compose up -d

http://localhost:8091

## Part B - Multi Container Deployment

services:
  db:
    image: mysql:5.7
    container_name: mysql-db
    environment:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_DATABASE: wordpress

  wordpress:
    image: wordpress:latest
    container_name: wordpress-app
    ports:
      - "8092:80"
    environment:
      WORDPRESS_DB_HOST: db
      WORDPRESS_DB_USER: root
      WORDPRESS_DB_PASSWORD: root
    depends_on:
      - db

docker compose up -d

http://localhost:8092

## Volume Management

docker volume ls

## Container Lifecycle

docker compose down

docker stop <container>

docker rm <container>

## Dockerfile

FROM node:18-alpine
WORKDIR /app
CMD ["node", "-e", "console.log('Hello from container')"]

## Conclusion

Docker Compose provides a structured and scalable approach compared to Docker Run and simplifies multi-container deployment significantly.

## Learning Outcomes

- Understood Docker Run vs Compose
- Implemented container deployments
- Worked with multi-container applications
- Learned container orchestration basics


