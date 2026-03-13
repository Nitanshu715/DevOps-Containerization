
# Installing Java (OpenJDK) and Executing a Java Program inside Docker Ubuntu Container

---

# Experiment Title
Installing Java (OpenJDK) and Executing a Java Program inside Docker Ubuntu Container

---

# Aim of the Experiment

To understand how Docker containers can be used as lightweight development environments by launching an Ubuntu container, installing Java (OpenJDK 17), writing a Java program inside the container, and executing the program successfully.

---

# Learning Objectives

- Verify Docker installation and version details
- Understand Docker client and server architecture
- Launch an Ubuntu container using Docker
- Assign a custom name to the container
- Update package repositories inside the container
- Install Java Development Kit (OpenJDK 17)
- Install Nano editor to create source files
- Write a simple Java program inside the container
- Compile and run the Java program
- Demonstrate Docker as a lightweight development environment

---

# Tools and Technologies Used

| Component | Description |
|----------|-------------|
| Docker Desktop | Container runtime environment used to create and manage containers |
| Ubuntu Container | Linux-based environment running inside Docker |
| OpenJDK 17 | Java Development Kit used to compile and run Java programs |
| Nano Editor | Lightweight terminal-based text editor |
| Windows Command Prompt | Terminal interface used to execute Docker commands |
| Git & GitHub | Version control system used to store experiment documentation |

---

# Background Theory

Docker is a containerization platform that allows developers to package applications along with their dependencies into containers. 
Containers are lightweight and portable environments that run consistently across different machines.

Unlike traditional virtual machines, Docker containers share the host operating system kernel while still maintaining isolated environments.

In this experiment, Docker is used to run an Ubuntu Linux container inside a Windows system. Inside this container, the Java Development Kit is installed and used to create and execute a Java program.

This demonstrates how Docker can be used to quickly set up development environments without installing software directly on the host system.

---

# System Requirements

- Windows 10 / Windows 11
- Docker Desktop installed and running
- Internet connection for downloading Docker images
- Basic knowledge of command line operations

---

# Step-by-Step Execution

---

## Step 1: Verify Docker Installation

First, verify that Docker is properly installed and running on the system.

Command:

```cmd
docker version
```

This command displays:

- Docker Client version
- Docker Server version
- API compatibility details

Successful execution confirms that Docker is properly installed and operational.

---

## Step 2: Pull and Run Ubuntu Container with Custom Name

Next, launch an Ubuntu container and assign it a custom name.

Command:

```cmd
docker run -it --name Java ubuntu
```

Explanation:

- docker run → Creates and starts a new container
- -it → Interactive terminal mode
- --name Java → Assigns the container the name "Java"
- ubuntu → Specifies the Ubuntu image

If the Ubuntu image is not available locally, Docker will automatically download it from Docker Hub.

Once executed, the terminal prompt changes to:

```
root@containerID:/#
```

This indicates that the user is now operating inside the Ubuntu container.

---

## Step 3: Update Ubuntu Package Repositories

Before installing software inside Ubuntu, the package repositories must be updated.

Command:

```bash
apt update
```

Purpose:

- Refreshes package lists
- Fetches the latest versions of available software packages
- Ensures the system installs the newest versions

---

## Step 4: Install Java Development Kit (OpenJDK 17)

Install Java inside the Ubuntu container.

Command:

```bash
apt install -y openjdk-17-jdk
```

Explanation:

- apt install → Installs software packages
- -y → Automatically confirms installation prompts
- openjdk-17-jdk → Java Development Kit version 17

After installation, verify Java installation.

Command:

```bash
java -version
```

Example Output:

```
openjdk version "17.x.x"
OpenJDK Runtime Environment
OpenJDK 64-Bit Server VM
```

This confirms that Java has been successfully installed.

---

## Step 5: Install Nano Text Editor

Nano is a simple terminal-based text editor used to create and edit files.

Command:

```bash
apt install -y nano
```

Nano allows users to write source code directly inside the container environment.

---

## Step 6: Create a Java Program

Create a new Java source file using Nano.

Command:

```bash
nano HelloWorld.java
```

Write the following Java program:

```java
class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello World from Java in Docker!");
    }
}
```

Save the file using:

```
CTRL + X
Y
Enter
```

This creates and saves the Java source file.

---

## Step 7: Compile and Run the Java Program

Execute the Java program using the Java runtime.

Command:

```bash
java HelloWorld.java
```

Expected Output:

```
Hello World from Java in Docker!
```

This confirms that:

- Java is installed correctly
- The program compiled successfully
- Execution occurred inside the Docker container

---

# Screenshots

Screenshots of the following steps should be captured:

1. Docker version verification
2. Running Ubuntu container
3. Updating package repositories
4. Installing OpenJDK 17
5. Installing Nano editor
6. Writing the Java program
7. Running the Java program and displaying output

---

# Results

- Docker environment verified successfully
- Ubuntu container launched with a custom container name
- Package repositories updated successfully
- OpenJDK 17 installed correctly
- Nano editor installed successfully
- Java source file created inside the container
- Java program compiled and executed successfully
- Output displayed correctly from inside the container

---

# Conclusion

This experiment successfully demonstrated how Docker containers can be used as lightweight development environments.

Instead of installing software directly on the host operating system, developers can create isolated containers and configure them with required tools and dependencies.

By installing Java inside an Ubuntu container and executing a Java program, we verified that Docker can be used for:

- application development
- testing environments
- dependency isolation
- reproducible builds

Docker provides a portable and efficient way to create development environments without the overhead of full virtual machines.

