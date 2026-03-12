# Containerizing a Python SAP ID Verification Application using Docker

---

# 🧠 Project Overview

This practical demonstrates how a Python-based application can be containerized using Docker.
The application verifies a user's SAP ID by comparing it with a predefined SAP ID stored inside the program.

The goal of this exercise is to demonstrate a complete DevOps-style workflow including:

• Application development  
• Dependency management  
• Docker container creation  
• Image building  
• Container execution  
• Interactive user input handling  
• Application testing inside a container  

This practical uses an official lightweight Python Docker base image and installs required dependencies
inside the container before executing the application.

---

# 🎯 Objectives

- Use an official Docker base image
- Containerize a Python application
- Install dependencies inside a Docker container
- Build a custom Docker image
- Run a container interactively
- Verify application execution inside a container
- Understand Docker image vs container concept
- Demonstrate a basic DevOps packaging workflow

---

# 🛠 Technologies Used

Docker Desktop  
Docker CLI  
Python 3.10 Slim Base Image  
NumPy Library  
Windows Command Prompt  
Git & GitHub  

---

# 🏗 DevOps Workflow Demonstrated

Application Development
        ↓
Dockerfile Creation
        ↓
Docker Image Build
        ↓
Container Execution
        ↓
Application Testing

---

# 📁 Project Structure

Class-Test-5-Feb-SAPID/
│
├── app.py
├── Dockerfile
└── README.md

---

# 🧾 Python Application Code (app.py)

```python
import numpy as np

stored_sapid = "500121943"

user_sapid = input("Enter your SAP ID: ")

if user_sapid == stored_sapid:
    print("Matched")
else:
    print("Not Matched")
```

---

# 🐳 Dockerfile

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY app.py .

RUN pip install numpy

CMD ["python", "app.py"]
```

---

# 📦 Dockerfile Instruction Explanation

FROM python:3.10-slim  
→ Uses the official lightweight Python 3.10 base image.

WORKDIR /app  
→ Creates and sets the working directory inside the container.

COPY app.py .  
→ Copies the Python application file from the host system into the container.

RUN pip install numpy  
→ Installs the NumPy dependency inside the container.

CMD ["python", "app.py"]  
→ Defines the command executed when the container starts.

---

# ⚙️ Step‑by‑Step Execution

# Step 1 — Navigate to Project Directory

```bash
cd DevOps-Lab-Assignments
cd Class-Test-5-Feb-SAPID
```

---

# Step 2 — Build Docker Image

```bash
docker build -t sapid-checker:500121943 .
```

Explanation

docker build → builds Docker image  
-t → assigns image name and tag  
sapid-checker → image name  
500121943 → image tag (SAP ID)  
. → current directory containing Dockerfile  

---

# Step 3 — Verify Image Creation

```bash
docker images
```

Example Output

REPOSITORY        TAG         IMAGE ID
sapid-checker     500121943   xxxxxxxxx

---

# Step 4 — Run Docker Container

```bash
docker run -it sapid-checker:500121943
```

Explanation

docker run → starts container  
-it → interactive terminal mode  
sapid-checker → image name  

---

# Step 5 — Application Execution

The container will prompt the user:

Enter your SAP ID:

---

# Correct SAP ID Test

Input

500121943

Output

Matched

---

# Incorrect SAP ID Test

Input

123456

Output

Not Matched

---

# 📊 Docker Concepts Demonstrated

Docker Base Image Usage  
Dependency Installation Inside Container  
Custom Docker Image Creation  
Container Execution Workflow  
Interactive Container Input Handling  
Application Isolation Using Containers  

---

# 📈 Advantages of Docker Containerization

Consistent runtime environment  
Application portability  
Lightweight virtualization  
Fast deployment and startup  
Dependency isolation  
Simplified DevOps workflows  

---

# 🧪 DevOps Application Packaging Flow

Developer writes Python application  
        ↓
Dockerfile defines environment setup  
        ↓
Docker builds custom image  
        ↓
Image stored locally  
        ↓
Container launched from image  
        ↓
Application executed inside isolated environment  

---

# 📷 Suggested Screenshots

Dockerfile Code  
Python Application Code  
Docker Image Build Logs  
Docker Images List  
Container Execution Output  

---

# ✅ Result

The Python SAP ID verification application was successfully containerized using Docker.
A custom Docker image was created using the official Python base image and executed
inside a container environment where the application was tested interactively.

---

# 🏁 Conclusion

This practical demonstrates how Docker can be used to package applications along
with their dependencies into portable containers. Containerization ensures that
applications run consistently across different environments, making Docker a
fundamental tool in modern DevOps, cloud computing, and microservices architectures.

