## Class Test : Containerizing a Python SAP ID Verification Application
## Objective 
The objective of this practical is to:
- Use an official Docker base image
- Containerize a simple Python application
- Install dependencies inside container
- Build custom Docker image
- Run container interactively
- Verify application execution inside container

## Technologies Used
- Docker Desktop
- Docker CLI
- Python 3.10 Slim Image
- NumPy
- VS Code
- macOS Terminal

## Structure
Docker Codes 5 Feb/
│
├── app.py
├── Dockerfile
└── README.md

## Application Description
This Python application:
- Takes SAP ID input from user
- Compares with stored SAP ID
- Prints result

### Python Application (app.py)

import numpy as np

stored_sapid = "500125960"
user_sapid = input("Enter your SAP ID: ")

if user_sapid == stored_sapid:
    print("Matched")
else:
    print("Not Matched")

### Dockerfile

FROM python:3.10-slim

WORKDIR /app

COPY app.py .

RUN pip install numpy

CMD ["python", "app.py"]

## Steps
### Step 1: Build Docker Image
- docker build -t sapid-checker:500125960 .

### Step 2: Verify Image Creation
- docker images

Image created:
- sapid-checker:500125960

### Step 3: Run Container
- sudo docker run -it sapid-checker:500125960

### Step 4: Test Application
Correct SAP ID
- 500125960
Output:
- Matched

Incorrect SAP ID
- 500232323
Output:
- Not Matched

## Docker Concepts Demonstrated
- Base Image Usage
- Dependency Installation in Container
- Image Build Process
- Container Execution
- Interactive Input Handling
- Application Isolation

## Learning Outcomes
After completing this practical, I understood:
- How Dockerfile instructions work
- How Python apps are containerized
- Difference between image and container
- How dependencies are installed inside container
- How to run interactive containers


## Result
Successfully containerized a Python SAP ID verification application using Docker and executed it inside a container.

## Conclusion
- This practical demonstrated real-world containerization workflow using Docker.
- It validated how applications can be packaged with dependencies and run consistently across environments.

