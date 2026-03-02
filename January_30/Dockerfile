# Use Ubuntu as base image
FROM ubuntu:22.04

# Update packages and install Java
RUN apt update && apt install -y openjdk-17-jdk

# Set working directory
WORKDIR /app

# Copy Java file into container
COPY Hello.java .

# Compile Java file
RUN javac Hello.java

# Default command to run app
CMD ["java", "Hello"]