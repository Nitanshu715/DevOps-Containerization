## Dockerfile Creation & Custom Image Building (Windows Environment)

---

## Overview

This practical session demonstrates the complete workflow of creating, building, managing, exporting, importing, and deploying a custom Docker image using a Dockerfile. The experiment focuses on understanding Dockerfile instructions, Docker image layering architecture, and application containerization using Java.

---

## Objectives

- Understand Dockerfile syntax and core instructions
- Create a custom Docker image using Ubuntu base
- Install Java inside container environment
- Compile and execute a Java application inside Docker
- Understand Docker’s layer-based architecture
- Export and import Docker images using TAR archives
- Push custom image to Docker Hub
- Implement DevOps packaging workflow

---

## Tools & Technologies Used

- Operating System: Windows 11
- Docker Desktop (Windows)
- Docker Engine
- Ubuntu 22.04 (Base Image)
- OpenJDK 17
- Git & GitHub
- Docker Hub

---

## Project Structure

Class Practical 30 Jan/
│
├── Hello.java
├── Dockerfile
├── java-app.tar
└── README.md

---

## Java Application Source Code

```java
public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello from Java inside Docker on Windows!");
    }
}
```

---

## Dockerfile Configuration

```dockerfile
# Base Image
FROM ubuntu:22.04

# Update system and install Java
RUN apt update && apt install -y openjdk-17-jdk

# Set working directory
WORKDIR /app

# Copy source code
COPY Hello.java .

# Compile Java program
RUN javac Hello.java

# Default container execution command
CMD ["java", "Hello"]
```

---

## Build Docker Image

```cmd
docker build -t java-app:1.0 .
```

Verify image:

```cmd
docker images
```

---

## Run Container from Image

```cmd
docker run java-app:1.0
```

Expected Output:

Hello from Java inside Docker on Windows!

---

## Manage Containers & Images

List containers:

```cmd
docker ps -a
```

Remove container:

```cmd
docker rm <container-id>
```

Remove image:

```cmd
docker rmi java-app:1.0
```

---

## Export Docker Image

```cmd
docker save -o java-app.tar java-app:1.0
```

---

## Load Docker Image

```cmd
docker load -i java-app.tar
```

---

## Push Image to Docker Hub

Login:

```cmd
docker login
```

Tag image:

```cmd
docker tag java-app:1.0 YOUR_DOCKERHUB_USERNAME/java-app:1.0
```

Push image:

```cmd
docker push YOUR_DOCKERHUB_USERNAME/java-app:1.0
```

---

## Understanding Docker Layer Architecture

- Each Dockerfile instruction creates a new immutable layer.
- Layers are cached for faster rebuilds.
- Changes in higher layers do not affect lower layers.
- Images are composed of stacked read-only layers.
- Containers add a writable layer on top of image layers.

---

## DevOps Application Packaging Workflow

1. Write application source code.
2. Define environment using Dockerfile.
3. Build Docker image.
4. Test application in container.
5. Version and tag image.
6. Export or push image to Docker Hub.
7. Deploy image in any environment consistently.

---

## Result

- Custom Docker image successfully built.
- Java application containerized and executed.
- Image exported and reloaded successfully.
- Image pushed to Docker Hub repository.
- Complete container lifecycle implemented.

---

## Conclusion

This experiment provided practical understanding of Dockerfile-based image creation, container execution, and DevOps application packaging workflows. It demonstrated how Docker ensures environment consistency, portability, and scalable deployment through containerization.

