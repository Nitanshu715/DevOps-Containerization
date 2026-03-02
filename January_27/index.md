# 🚀 Class Practical — 27 January
## Docker Volumes, Persistent Storage & Image Lifecycle Management (Windows Environment)

---

## 📌 Overview

This practical session focuses on understanding Docker persistent storage mechanisms and complete image lifecycle management.  
The lab demonstrates Docker volume creation, bind mounts, stateful container setup, container-to-image conversion, image backup, removal, restoration, and layer inspection using Docker Desktop on Windows.

---

## 🛠 Tools & Technologies Used

- Windows 11
- Docker Desktop
- Command Prompt (CMD)
- Ubuntu Docker Image
- OpenJDK 17
- Git & GitHub

---

# 🧱 PART A — Docker Volumes & Persistent Storage

---

## 🔹 Step 1: Create a Docker Volume

```cmd
docker volume create myvolume
docker volume ls
```

---

## 🔹 Step 2: Run Ubuntu Container with Volume

```cmd
docker run -it -v myvolume:/data ubuntu bash
```

Inside container:

```bash
cd /data
echo "Nitanshu DevOps Lab 27 Jan" > file.txt
cat file.txt
exit
```

---

## 🔹 Step 3: Verify Data Persistence

```cmd
docker run -it -v myvolume:/data ubuntu bash
```

Inside container:

```bash
cd /data
cat file.txt
exit
```

---

## 🔹 Step 4: Bind Mount Example (Host Directory)

```cmd
mkdir C:\dockerdata
docker run -it -v C:\dockerdata:/app ubuntu bash
```

Inside container:

```bash
cd /app
echo "Bind Mount Test" > bind.txt
exit
```

Host Verification:

```cmd
dir C:\dockerdata
```

---

# 🧊 PART B — Custom Image Creation & Lifecycle

---

## 🔹 Step 5: Run Ubuntu Container

```cmd
docker run -it --name java_container ubuntu bash
```

Inside container:

```bash
apt update
apt install openjdk-17-jdk -y
java -version
exit
```

---

## 🔹 Step 6: Commit Container into Image

```cmd
docker commit java_container myrepo/java-img
docker images
```

---

## 🔹 Step 7: Run Custom Image

```cmd
docker run -it myrepo/java-img bash
```

Inside container:

```bash
java -version
exit
```

---

## 🔹 Step 8: Save Image as Backup (.tar)

```cmd
docker save -o java-image-backup.tar myrepo/java-img
dir java-image-backup.tar
```

---

## 🔹 Step 9: Remove Docker Image

```cmd
docker rmi myrepo/java-img
docker images
```

---

## 🔹 Step 10: Restore Image

```cmd
docker load -i java-image-backup.tar
docker images
```

---

## 🔹 Step 11: Inspect Image History

```cmd
docker history myrepo/java-img
```

---

# 🔗 GitHub Version Control Setup

```cmd
cd DevOps-Lab-Assignments
mkdir "Class Practical 27 Jan"
cd "Class Practical 27 Jan"
notepad README.md
```

---

## 🚀 Initialize Git & Push to GitHub

```cmd
cd ..
git add .
git commit -m "Added Class Practical 27 Jan - Docker Volumes & Image Lifecycle"
git push
```

---

# ✅ Result

- Docker volume successfully created and verified.
- Persistent storage confirmed using volume mounts.
- Bind mount functionality validated.
- Java-installed container committed into reusable image.
- Docker image backup created using docker save.
- Image removed and restored successfully using docker load.
- Image layer history inspected.

---

# 🎯 Conclusion

This lab demonstrates stateful container management using Docker volumes and bind mounts, along with full Docker image lifecycle operations including commit, save, remove, load, and history inspection.  
It validates Docker’s capability to manage persistence, portability, and recovery in DevOps environments.

