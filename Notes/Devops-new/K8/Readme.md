# Kubernetes (K8s)

## Overview

Kubernetes (K8s) is an open-source platform originally developed by Google and now maintained by the Cloud Native Computing Foundation (CNCF). It is designed to orchestrate containerized applications, automating deployment, scaling, and management.

Key Features:
- **Automatic Restart**: Stops and restarts pods as needed.
- **Probes**:
  - **Liveness Probe**: Ensures the application is running. For example, if set to 10 seconds, Kubernetes will check every 10 seconds.
  - **Readiness Probe**: Checks if the application is ready to accept requests.

![Kubernetes](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/7a522c01-24a9-41b9-9773-52727e3da74c)

- **Load Management**: Manages load across containers.
- **Automated Deployment**: Facilitates automated deployment processes.

## Architecture

![Kubernetes Architecture](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/ac93a0a6-0b6b-4b70-b93e-eb5e76001981)

### Master Components

1. **API Server**: Acts as the cluster gateway. All requests first go to the API server, which then decides the next steps.
2. **ETCD**: The cluster's brain, storing all information in a key-value format.
3. **Scheduler**: Makes decisions on where to create pods.
4. **Controller Manager**: Detects state changes (e.g., if a pod is down) and ensures the desired state of the cluster matches the actual state.

### Worker Components

1. **Kubelet**: Responsible for creating and monitoring pods based on specifications provided by the control plane.
2. **Kube-Proxy**: Manages networking rules and facilitates communication within and outside the cluster.
3. **Container Runtime**: Handles container creation and management (e.g., Docker, containerd).

## Workflow

1. **Request**: Sent to the API server.
2. **API Server**: Stores request information in ETCD.
3. **Scheduler**: Finds a suitable worker node and updates ETCD.
4. **Kubelet**: Creates the pod on the assigned node.
5. **Kube-Proxy**: Enables network rules for the pod.
6. **Controller**: Detects issues and informs the scheduler if something goes wrong.

## Components of Kubernetes

- **Pod**: The smallest deployable unit, consisting of one or more containers. Each pod runs on a node.
- **Node**: A worker machine in Kubernetes, either a virtual or physical machine.
- **Cluster**: A set of nodes grouped together, managed by the master components.
- **Service**: An abstraction which defines a logical set of Pods and a policy to access them. It provides stable IP addresses and DNS names to access the pods.
- **ConfigMap and Secret**: Mechanisms to handle configuration data. ConfigMaps store configuration information in key-value pairs, while Secrets are used to store sensitive information.
- **Deployment**: Manages the deployment of pods, ensuring the desired number of replicas and enabling updates.

Additional Components (for a more comprehensive understanding):

- **ReplicaSet**: Ensures a specified number of pod replicas are running at any given time.
- **DaemonSet**: Ensures that a copy of a pod is running across all or some nodes.
- **StatefulSet**: Manages the deployment and scaling of a set of pods, ensuring the order and uniqueness of these pods.
- **Ingress**: Manages external access to services within a cluster, typically HTTP.

