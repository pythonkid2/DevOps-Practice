# Dozzle Installation Guide (Docker Swarm with Authentication)

## Overview

This document describes the steps required to install and configure Dozzle on a Docker Swarm server.

Dozzle provides a web interface for viewing Docker container logs, service status, and container resource utilization.

---

# Prerequisites

Verify Docker is installed:

```bash
docker version
```

Verify Docker Swarm is initialized:

```bash
docker node ls
```

Expected output:

```bash
ID                            HOSTNAME      STATUS  AVAILABILITY  MANAGER STATUS
xxxxxxxxxxxxxxxxxxxx *        hostname      Ready   Active        Leader
```

If Swarm is not initialized:

```bash
docker swarm init
```

---

# Create Directories

Create required directories:

```bash
sudo mkdir -p /opt/dozzle/data
```

Verify:

```bash
ls -ld /opt/dozzle
ls -ld /opt/dozzle/data
```

---

# Generate Authentication User

Generate a user configuration file:

```bash
docker run --rm amir20/dozzle generate admin \
  --password 'Welcome@123' \
  --email 'admin@example.com' \
  --name 'Administrator'
```

Example output:

```yaml
users:
    admin:
        email: admin@example.com
        name: Administrator
        password: $2a$11$xxxxxxxxxxxxxxxxxxxxxxxxxxxx
        filter: ""
        roles: ""
```

---

# Create users.yml

Create the authentication file:

```bash
sudo vi /opt/dozzle/data/users.yml
```

Paste the generated output:

```yaml
users:
    admin:
        email: admin@example.com
        name: Administrator
        password: $2a$11$xxxxxxxxxxxxxxxxxxxxxxxxxxxx
        filter: ""
        roles: ""
```

Verify:

```bash
sudo cat /opt/dozzle/data/users.yml
```

---

# Create Docker Stack File

Create:

```bash
sudo vi /opt/dozzle/dozzle-stack.yml
```

Contents:

```yaml
version: "3.8"

services:
  dozzle:
    image: amir20/dozzle:v10.6.3

    environment:
      - DOZZLE_MODE=swarm

    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - /opt/dozzle/data:/data

    ports:
      - "9999:8080"

    networks:
      - dozzle

    deploy:
      mode: global
      restart_policy:
        condition: any

networks:
  dozzle:
    driver: overlay
```

---

# Deploy Dozzle

Deploy the stack:

```bash
docker stack deploy -c /opt/dozzle/dozzle-stack.yml dozzle
```

---

# Verify Deployment

Check service:

```bash
docker stack services dozzle
```

Expected:

```bash
NAME            MODE      REPLICAS
dozzle_dozzle   global    1/1
```

Check task status:

```bash
docker service ps dozzle_dozzle
```

Expected:

```bash
Running
```

---

# Verify Logs

Check startup logs:

```bash
docker service logs dozzle_dozzle --tail 50
```

Expected:

```text
Dozzle version v10.6.3
Starting in swarm mode
Accepting connections on :8080
```

---

# Open Security Group

Allow inbound access:

| Protocol | Port |
| -------- | ---- |
| TCP      | 9999 |

Restrict access to office IPs or VPN users whenever possible.

---

# Access Dozzle

Open:

```text
http://<SERVER-IP>:9999
```

Example:

```text
http://13.x.x.x:9999
```

---

# Common Verification Commands

Check running containers:

```bash
docker ps
```

Check Dozzle service:

```bash
docker service inspect dozzle_dozzle --pretty
```

Check stack:

```bash
docker stack ls
```

Check logs:

```bash
docker service logs dozzle_dozzle --tail 100
```

Remove stack:

```bash
docker stack rm dozzle
```

---

# Features Available

After deployment, Dozzle provides:

* Real-time container logs
* Docker Swarm service grouping
* CPU utilization monitoring
* Memory utilization monitoring
* Container restart history
* Service health visibility
* Search and filter functionality

---

# Security Recommendations

* Restrict access through Security Groups.
* Avoid logging passwords, API keys, JWT tokens, and database credentials.
* Review application logging practices regularly.
* Keep Docker and Dozzle versions updated.

---

# Installed Components

| Component    | Version |
| ------------ | ------- |
| Docker       | 25.x    |
| Docker Swarm | Enabled |
| Dozzle       | v10.6.3 |

Installation Status: Successful
Purpose: Centralized Docker Log Monitoring and Troubleshooting
