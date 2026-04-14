
# Docker Swarm and Advanced Networking

## Overview
This project demonstrates advanced Docker networking concepts and container orchestration using Docker Swarm. It includes bridge networks, overlay networks, service creation, scaling, and macvlan networking.

## Tools Used
- Docker Engine
- Docker CLI
- NGINX
- Alpine Linux

## Bridge Network
A custom bridge network was created to enable communication between containers.

Commands:
docker network create my_app_net
docker run -d --name web --network my_app_net nginx
docker run -d --name utils --network my_app_net alpine ping web
docker exec -it utils ping web

## Swarm Initialization
Docker Swarm mode was initialized to enable orchestration.

Command:
docker swarm init

## Overlay Network
An overlay network was created to simulate multi-host networking.

Commands:
docker network create -d overlay --attachable my_overlay
docker run -dit --name app1 --network my_overlay busybox sh
docker run -dit --name app2 --network my_overlay busybox sh
docker exec app1 ping app2

## Services and Scaling
A service was created and scaled.

Commands:
docker service create --name web -p 8080:80 nginx
docker service scale web=4
docker service ls
docker service ps web

## Production Overlay Network
docker network create -d overlay prod_net

## Macvlan Networking
Attempted macvlan setup:
docker network create -d macvlan --subnet=192.168.1.0/24 --gateway=192.168.1.1 -o parent=Ethernet my_macvlan

Observation:
Macvlan networking is not fully supported on Windows environments.

## Result
Successfully demonstrated Docker Swarm orchestration, container networking, and service scaling.

