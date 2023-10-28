
29/8

**Load Balancing** - Is the capability to distribute the traffic among multiple instances according to some algorithms (e.g., round robin).

**Service Discovery** - 
- Whenever a new instance comes up, the system should be aware of it and connect to it.
- Whenever an existing system crashes, the system should be informed to stop forwarding requests to it.


# Kubernetes

- Automatic Failover: Kubernetes provides automated failover mechanisms to ensure high availability and minimize downtime in case of node failures.

- Communication between two containers (across different machines):
  - Service Discovery, Load Balancing: 
- Automatic Bin Packing and Scheduling: Kubernetes automatically schedules containers based on resource requirements and constraints, ensuring efficient resource utilization and optimal performance.

- Automatic Scaling:
  - Scale-out/Scale-in: Kubernetes enables automatic scaling of applications based on predefined metrics, allowing for seamless horizontal scaling by adding or removing instances to meet the demands of the workload dynamically.

**pause container**

In Kubernetes, a "pause container" is a small, behind-the-scenes container that helps other containers in the same group communicate and share resources easily.

**Kubernetes YAML configuration that defines a basic pod**

```
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - image: nginx
    name: nginx
    ports:
    - containerPort: 80
      name: http
```

- `apiVersion: v1`: This specifies the Kubernetes API version being used, with "v1" representing the core version of the Kubernetes API.

- `kind: Pod`: This indicates that the YAML defines a Kubernetes pod. Pods are the smallest deployable units in Kubernetes and can contain one or more containers.

- `metadata`: This section contains metadata about the pod, including its name. In this case, the name of the pod is set as "nginx".

- `spec`: The "spec" section describes the desired state of the pod and its contents, such as the containers running within it.

- `containers`: This section lists the containers within the pod. In this case, there is one container defined.

- `image: nginx`: This specifies the Docker image to be used for the container. Here, it indicates the use of the Nginx web server image.

- `name: nginx`: This provides a name for the container, which is set as "nginx" to match the name of the Nginx image.

- `ports`: This section defines the ports to be used by the container.

- `containerPort: 80`: This sets the container's port to 80, which is the default port for the HTTP protocol.

- `name: http`: This provides a name for the port, which is set as "http" to specify that it is for handling HTTP traffic.




![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/0ba7a510-a2d8-4300-8f98-636c2ee00e02)
