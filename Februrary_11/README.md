# Docker Volume Management, Data Persistence, Backup & Restore

---

# DevOps Storage Practical

This practical demonstrates Docker storage architecture, persistent data management,
bind mounts, volume lifecycle, backup strategies, and disaster recovery workflows
using Docker named volumes and TAR-based archival mechanisms.

The workflow simulates how real DevOps systems handle container storage for
databases, application logs, and persistent application state.

This lab covers:

- Docker Engine Verification
- Docker Storage Architecture
- Named Volume Creation
- Persistent Container Storage
- Bind Mount Host ↔ Container Mapping
- Data Persistence Testing
- TAR Based Volume Backup
- Production Data Loss Simulation
- Volume Restoration from Backup
- Volume Metadata Inspection
- Storage Size Verification
- DevOps Storage Disaster Recovery Workflow

---

# Technologies Used

Docker Desktop  
Docker CLI  
Ubuntu Base Image  
Alpine Linux Image  
Linux TAR Utility  
Named Docker Volumes  
Bind Mounts  
Windows Command Prompt  
Git Version Control  
GitHub Repository Hosting  

---

# Key DevOps Concepts Covered

Docker Storage Drivers  
Container Writable Layer  
Named Volumes  
Bind Mounts  
Persistent Data Storage  
Container Lifecycle  
Temporary Containers (--rm)  
Volume Backup Strategy  
Volume Restore Strategy  
Container Storage Mountpoints  
Volume Metadata Inspection  
Container Storage Disaster Recovery  

---

# Repository Structure

```
DevOps-Lab-Assignments
│
├── Class Practical 11 Feb
│   │
│   ├── README.md
│   ├── screenshots
│   │   ├── docker-info.png
│   │   ├── volume-create.png
│   │   ├── container-write.png
│   │   ├── bind-mount.png
│   │   ├── backup.png
│   │   ├── restore.png
│   │   └── inspect.png
│   │
│   └── backup
│       └── volume_backup.tar.gz
```

---

# PART 1 — Docker Environment Verification

Verify Docker installation and runtime environment.

```
docker --version
docker info
docker images
docker volume ls
```

Expected Results

Docker Engine should be running successfully.

Docker images list should show available base images.

Volume list should display existing volumes.

---

# PART 2 — Create Named Docker Volume

Named volumes are managed by Docker and provide persistent storage
outside the container filesystem.

```
docker volume create devops_volume
```

Verify volume creation

```
docker volume ls
```

Expected output

```
local    devops_volume
```

---

# PART 3 — Run Container Using Named Volume

Run Ubuntu container and mount the named volume.

```
docker run -it --name volume_test -v devops_volume:/home/app ubuntu bash
```

Explanation

-it  
Interactive terminal session

-v devops_volume:/home/app  
Mount Docker volume into container directory

ubuntu  
Base Linux image

bash  
Launch interactive shell

---

# PART 4 — Write Data Inside Volume

Inside container

```
cd /home/app

echo "Nitanshu DevOps Volume Test" > file1.txt

echo "Docker Persistence Demonstration" > file2.txt

ls
```

Expected Output

```
file1.txt
file2.txt
```

---

# PART 5 — Exit Container and Remove It

```
exit
```

Remove container

```
docker rm volume_test
```

Important

The container is deleted but the Docker volume still exists.
This proves persistent storage independent from container lifecycle.

---

# PART 6 — Verify Data Persistence

Run container again using same volume

```
docker run -it --rm -v devops_volume:/home/app ubuntu bash
```

Inside container

```
cd /home/app

ls

cat file1.txt

cat file2.txt
```

Expected Output

```
Nitanshu DevOps Volume Test
Docker Persistence Demonstration
```

Exit container

```
exit
```

---

# PART 7 — Bind Mount Implementation

Bind mounts map a host directory directly to a container directory.

Create host directory

```
mkdir hostdata
```

Run container with bind mount

```
docker run -it --rm -v %cd%/hostdata:/home/app ubuntu bash
```

Inside container

```
cd /home/app

echo "Bind Mount Working Successfully" > bindfile.txt

exit
```

---

# Verify File On Host

Navigate to host folder

```
cd hostdata
```

Check file

```
type bindfile.txt
```

Expected Output

```
Bind Mount Working Successfully
```

This confirms real-time host ↔ container file sharing.

---

# PART 8 — Volume Backup Using TAR

Create backup directory

```
mkdir backup
```

Backup Docker volume using Alpine container

```
docker run --rm -v devops_volume:/volume -v %cd%/backup:/backup alpine tar czf /backup/volume_backup.tar.gz -C /volume .
```

Explanation

--rm  
Automatically remove temporary container

-v devops_volume:/volume  
Mount Docker volume

-v %cd%/backup:/backup  
Mount host backup directory

tar czf  
Create compressed archive

-C /volume  
Archive contents of volume

---

# Verify Backup File

```
dir backup
```

Expected Output

```
volume_backup.tar.gz
```

---

# PART 9 — Simulate Production Data Loss

Delete Docker volume

```
docker volume rm devops_volume
```

This simulates a production storage failure scenario.

---

# PART 10 — Recreate Docker Volume

```
docker volume create devops_volume
```

---

# PART 11 — Restore Volume From Backup

```
docker run --rm -v devops_volume:/volume -v %cd%/backup:/backup alpine tar xzf /backup/volume_backup.tar.gz -C /volume
```

Explanation

tar xzf  
Extract compressed archive

-C /volume  
Restore files into Docker volume

---

# PART 12 — Verify Restored Data

Run container again

```
docker run -it --rm -v devops_volume:/home/app ubuntu bash
```

Inside container

```
cd /home/app

ls

cat file1.txt

cat file2.txt
```

Expected Output

```
Nitanshu DevOps Volume Test
Docker Persistence Demonstration
```

Exit container

```
exit
```

---

# PART 13 — Inspect Docker Volume Metadata

Inspect volume configuration

```
docker volume inspect devops_volume
```

Important fields

```
Name
Driver
Mountpoint
Scope
```

Example

```
Mountpoint: /var/lib/docker/volumes/devops_volume/_data
Driver: local
Scope: local
```

---

# PART 14 — Check Backup Storage Size

```
docker run --rm -v %cd%:/data alpine du -h /data/backup
```

This command verifies storage consumption of the backup archive.

---

# DevOps Storage Workflow Simulation

This practical simulates real production DevOps storage lifecycle

```
Container
   ↓
Named Volume
   ↓
Write Data
   ↓
Backup Volume (TAR)
   ↓
Delete Volume (Failure Simulation)
   ↓
Recreate Volume
   ↓
Restore Data
   ↓
Verify Application Data
```

---

# Result

Docker environment verified successfully

Named volume created successfully

Persistent storage tested across container lifecycle

Bind mount host ↔ container file sharing verified

Volume backup created successfully

Volume deletion simulated storage failure

Backup archive restored successfully

Restored data verified inside container

Volume metadata inspected successfully

Backup storage size verified

---

# Learning Outcomes

Understanding Docker storage architecture

Difference between container writable layer and persistent storage

Implementation of named Docker volumes

Bind mount usage for development workflows

Container data persistence beyond container lifecycle

Backup strategies for Docker volumes

TAR based archival for container storage

Production storage disaster recovery techniques

Docker volume inspection and metadata debugging

---

# Conclusion

This practical demonstrates a complete DevOps container storage workflow including
persistent storage implementation, container data management, and disaster recovery
strategies using Docker named volumes and TAR based backups.

These techniques are widely used in production environments for:

Database backup  
Application state persistence  
Container migration  
Disaster recovery  
Cloud-native storage management  

