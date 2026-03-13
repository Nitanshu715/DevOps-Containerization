## DevOps Fundamentals & Setup (Windows Environment)

---

## Overview

This practical session focuses on understanding the foundational concepts of DevOps and containerization using Docker Desktop on Windows. The lab demonstrates Docker installation verification, container execution, Linux interaction inside Docker, and package management differences between Windows and Linux.

---

## Tools & Technologies Used

- Windows 11
- Docker Desktop
- Command Prompt (CMD)
- Ubuntu Docker Image
- Git & GitHub

---

## Step 1: Verify Docker Installation

```cmd
docker --version
docker info
```

---

## Step 2: Run Docker Test Container

```cmd
docker run hello-world
```

---

## Step 3: Windows Package Manager (Comparison)

```cmd
winget upgrade
```

---

## Step 4: Run Ubuntu Container Interactively

```cmd
docker run -it ubuntu bash
```

---

## Step 5: Update Packages Inside Ubuntu Container

```bash
apt update
apt upgrade -y
exit
```

---

## GitHub Version Control Setup

```cmd
mkdir DevOps-Lab-Assignments
cd DevOps-Lab-Assignments
mkdir "Class Practical 21 Jan"
cd "Class Practical 21 Jan"
notepad README.md
```

---

## Initialize Git & Push to GitHub

```cmd
cd ..
git init
git add .
git commit -m "Added Class Practical 21 Jan - DevOps Fundamentals"
git remote add origin https://github.com/YOUR_USERNAME/DevOps-Lab-Assignments.git
git branch -M main
git push -u origin main
```

---

## Result

- Docker successfully installed and verified.
- hello-world container executed successfully.
- Ubuntu container launched interactively.
- Linux package update performed inside Docker.
- Repository pushed to GitHub successfully.

---

## Conclusion

This lab establishes a strong foundation in Docker-based containerization and DevOps workflow setup using Windows. It demonstrates how Linux environments can be simulated inside Windows using Docker, enabling consistent development and deployment environments.

