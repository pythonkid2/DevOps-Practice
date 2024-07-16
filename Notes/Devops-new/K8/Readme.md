# Kubernetes (K8s)

# Table of Contents

- [Overview](#Overview)
- [Architecture](#Architecture)
- [Components](#Components)
- [Taints & Tolerations](#Taints&Tolerations)
- [Section 4](#section-4)
- [Section 5](#section-5)
- [Conclusion](#conclusion)

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

![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/7aeb61e3-548f-4c44-ba3b-75759c414ac2)

## services

cluster ip (Basically using for internal communication)
node port (external to internal communication)
Load Balancer (load balancer service accessing directly pod, externally accessing with url, more safe)
Ingress (sending request to the service)

## Taints & Tolerations

In Kubernetes, taints and tolerations are mechanisms used to control which nodes a pod can be scheduled on. They are important for ensuring that certain pods are only deployed on specific nodes or types of nodes.

### Taints:

A taint is a key-value pair that is applied to a node. It prevents pods from being scheduled onto a node unless the pod has a corresponding toleration. Taints are typically used to mark nodes as unsuitable for certain types of workloads, such as reserving nodes for specific tasks or isolating nodes due to hardware limitations.

Here's an example of applying a taint to a node:

```bash
kubectl taint nodes <node-name> key=value:taint-effect
```

For example:

```bash
kubectl taint nodes node1 app=backend:NoSchedule
```

In this example, we're tainting `node1` with a key-value pair `app=backend` and the taint effect `NoSchedule`. This means that pods without a toleration for `app=backend` will not be scheduled on `node1`.

### Tolerations:

A toleration is a part of a pod's specification that allows the pod to be scheduled onto a node with a matching taint. It effectively tells the scheduler that the pod is "tolerant" of the taint on the node.

Here's an example of adding a toleration to a pod:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  containers:
  - name: my-container
    image: my-image
  tolerations:
  - key: "app"
    operator: "Equal"
    value: "backend"
    effect: "NoSchedule"
```

In this example, the pod has a toleration for the taint with key `app`, value `backend`, and taint effect `NoSchedule`. This means that the pod can be scheduled on a node with the taint `app=backend:NoSchedule`.

### Taint Effects:

There are three taint effects:

1. **NoSchedule**: The pod will not be scheduled on the tainted node.
2. **PreferNoSchedule**: The scheduler will try to avoid placing the pod on the tainted node, but it's not an absolute restriction.
3. **NoExecute**: If a pod is already running on a node when it gets tainted with `NoExecute`, the pod will be evicted from the node.


# EXAMPLE

Tainting a Node:
kubectl taint nodes <nodename> key=value:effect
kubectl taint nodes ip-172-31-36-109 app=backend:NoSchedule


```yaml
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: spring-boot-k8s-deployment
spec:
  selector:
    matchLabels:
      app: spring-boot-k8s
  replicas: 2
  template:
    metadata:
      labels:
        app: spring-boot-k8s
    spec:
      containers:
        - name: spring-boot-k8s
          image: adijaiswal/shopping-cart:latest
          imagePullPolicy: IfNotPresent
          ports:
            - containerPort: 8070
      tolerations:
        - key: app
          operator: Equal
          value: backend
          effect: NoSchedule
---
apiVersion: v1
kind: Service
metadata:
  name: springboot-k8ssvc
spec:
  selector:
    app: spring-boot-k8s
  ports:
    - protocol: TCP
      port: 8070
      targetPort: 8070
  type: NodePort
```

# Liveness & Readiness Probe

Liveness and readiness probes are crucial for Kubernetes to ensure the health and availability of your application. Here's a detailed explanation with examples:

## Liveness Probe:

A liveness probe determines if a container is still running and healthy. If the liveness probe fails, Kubernetes will restart the container.

### Example:

Let's say you have a web server container running on port 80. You can set up an HTTP liveness probe to check if the server is responsive:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  containers:
  - name: my-container
    image: my-web-server-image
    ports:
    - containerPort: 80
    livenessProbe:
      httpGet:
        path: /
        port: 80
      initialDelaySeconds: 15
      periodSeconds: 10
```

In this example:

- `httpGet`: Specifies that the probe should perform an HTTP GET request.
- `path`: The path of the request (in this case, `/` means the root path).
- `port`: The port to use for the request (in this case, 80).
- `initialDelaySeconds`: The number of seconds after the container has started before the first probe is performed.
- `periodSeconds`: How often (in seconds) to perform the probe.

## Readiness Probe:

A readiness probe determines if a container is ready to start accepting traffic. If the readiness probe fails, the container won't receive traffic from the service, but it will not be restarted.

### Example:

Suppose your application requires some time to warm up before it can handle requests. You can set up a readiness probe like this:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  containers:
  - name: my-container
    image: my-web-server-image
    ports:
    - containerPort: 80
    readinessProbe:
      httpGet:
        path: /ready
        port: 80
      initialDelaySeconds: 5
      periodSeconds: 3
```

In this example:

- `httpGet`: Specifies that the probe should perform an HTTP GET request.
- `path`: The path of the request (in this case, `/ready`).
- `port`: The port to use for the request (in this case, 80).
- `initialDelaySeconds`: The number of seconds after the container has started before the first probe is performed.
- `periodSeconds`: How often (in seconds) to perform the probe.

Using these probes, you can ensure that your application is always responsive and ready to handle traffic, and Kubernetes will take care of restarting or routing traffic accordingly.



