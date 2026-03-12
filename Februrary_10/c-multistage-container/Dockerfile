# Stage 1: Builder
FROM ubuntu:22.04 AS builder

RUN apt-get update && apt-get install -y gcc

WORKDIR /app
COPY hello.c .

RUN gcc -static -o hello hello.c

# Stage 2: Minimal Runtime
FROM scratch

COPY --from=builder /app/hello /hello

CMD ["/hello"]