## Running C Application Using Docker Volume Mount (Continuous Runtime Execution)

---

# 📌 DevOps Practical Overview

This practical demonstrates how containerized applications can be executed dynamically using Docker volume mounting.  
Instead of rebuilding a Docker image every time the application code changes, the source code from the host machine is mounted directly inside the running container.

This allows developers to modify the application on their local system while the container accesses the latest version instantly.

This concept represents a **real-world DevOps development workflow**, where container environments are used for development, testing, and runtime execution without rebuilding images repeatedly.

---

# 🎯 Objectives

- Build a Docker image using the official **GCC base image**
- Execute a **C program inside a Docker container**
- Demonstrate **runtime compilation inside container**
- Implement **continuous runtime execution using infinite loop**
- Use **Docker Volume Mounting for Host ↔ Container file sharing**
- Demonstrate **runtime code injection without rebuilding image**
- Understand **COPY vs Volume Mount concepts**
- Execute interactive container runtime testing
- Demonstrate real-world **containerized development workflow**

---

# 🧰 Technologies Used

| Technology | Description |
|------------|-------------|
| Docker Desktop | Container runtime platform |
| Docker CLI | Command line interface for Docker |
| GCC Compiler | GNU C compiler used inside container |
| C Programming Language | Application code |
| Docker Volume Mount | Host and container file sharing |
| Windows Command Prompt | Command execution environment |
| Linux Runtime (Container) | Execution environment inside Docker |

---

# 📁 Project Directory Structure

```
Class Practical 6 Feb
│
├── app.c
└── Dockerfile
```

---

# 🧾 Application Description

This application asks the user to enter their SAP ID continuously.

The program contains:

• A stored SAP ID  
• A user input SAP ID  
• A comparison logic using `strcmp()`  
• A continuous `while(1)` loop for runtime interaction

The program continues running indefinitely until the container is manually stopped.

---

# 💻 C Application Source Code (app.c)

```c
#include <stdio.h>
#include <string.h>

int main() {

    char stored_sapid[] = "500125960";
    char user_sapid[50];

    while (1) {

        printf("Enter your SAP ID: ");
        scanf("%s", user_sapid);

        if (strcmp(user_sapid, stored_sapid) == 0) {
            printf("Matched\n");
        }
        else {
            printf("Not Matched\n");
        }

    }

    return 0;
}
```

---

# 🐳 Dockerfile Configuration

The Dockerfile defines how the container environment should be built.

In this case we use the **official GCC base image** so that the container has a C compiler available.

The program will be compiled and executed **inside the container runtime**.

```dockerfile
FROM gcc:latest

WORKDIR /app

CMD ["bash", "-c", "gcc app.c -o app && ./app"]
```

---

# 🔨 Step 1 — Build Docker Image

Navigate to the project directory and build the image.

```
docker build -t sapid-checker .
```

This command:

• Reads the Dockerfile  
• Pulls the GCC base image if not available  
• Creates a new Docker image called `sapid-checker`

---

# 🔍 Step 2 — Verify Docker Image

```
docker images
```

Expected Output:

```
REPOSITORY       TAG       IMAGE ID       CREATED         SIZE
sapid-checker    latest    XXXXXXXX       XX seconds ago  XXXMB
```

This confirms the Docker image was successfully built.

---

# 🔗 Step 3 — Run Container Using Volume Mount

Now we mount the host application file inside the container.

```
docker run -it -v "%cd%/app.c:/app/app.c" sapid-checker
```

Explanation:

```
-it
```

Interactive terminal mode

```
-v "%cd%/app.c:/app/app.c"
```

Maps the host file to container file

```
HOST FILE          CONTAINER FILE
app.c        →     /app/app.c
```

This means:

Any change to `app.c` on the host system will immediately reflect inside the container.

---

# ⚙️ Runtime Execution

Once the container starts, the following command runs automatically:

```
gcc app.c -o app && ./app
```

Steps performed inside container:

1. Compile C program
2. Create executable
3. Run program
4. Accept continuous user input

---

# 🧪 Program Execution Example

### Incorrect SAP ID

```
Enter your SAP ID: 123456
Not Matched
```

### Correct SAP ID

```
Enter your SAP ID: 500125960
Matched
```

The application continues running due to the infinite loop.

---

# 🛑 Stopping the Container

To stop execution:

```
CTRL + C
```

This terminates the container process.

---

# 📦 Docker Concepts Demonstrated

• Official Docker Base Image  
• Containerized Compilation  
• Runtime File Injection  
• Docker Volume Mounting  
• Host ↔ Container File Sharing  
• Interactive Containers  
• Continuous Runtime Execution  
• Development Without Image Rebuild  

---

# 🔁 Development Workflow Demonstrated

Traditional Workflow

```
Edit Code
Rebuild Image
Run Container
```

Docker Volume Workflow

```
Edit Code
Run Container
Changes Reflect Instantly
```

This significantly improves developer productivity.

---

# 🌍 Real‑World DevOps Relevance

This technique is commonly used in:

• Software development environments  
• Containerized testing pipelines  
• Continuous Integration systems  
• DevOps microservice development  
• Cloud native container workflows

Developers often mount source code directly inside containers to test applications without rebuilding Docker images repeatedly.

---

# ✅ Result

Successfully executed a C application inside a Docker container using volume mounting and continuous runtime execution.

The application compiled and ran inside the container while reading the source file directly from the host system.

---

# 📚 Conclusion

This practical demonstrated how Docker can be used to run and test applications dynamically using volume mounts.  
Instead of embedding the source code inside the container image, the program was executed using files mounted from the host system.

This approach enables rapid development, faster testing cycles, and efficient container-based workflows commonly used in modern DevOps environments.

