# Stage 1: Builder
FROM maven:3.8-openjdk-11 AS builder

WORKDIR /app

COPY pom.xml .
COPY src ./src

RUN mvn clean package -DskipTests

# Stage 2: Runtime
FROM eclipse-temurin:11-jre-jammy

WORKDIR /app

COPY --from=builder /app/target/helloapp-1.0.jar app.jar

RUN useradd -m myuser
USER myuser

CMD ["java", "-jar", "app.jar"]