
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
***
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

- `kind: Pod`: This indicates that the YAML defines a Kubernetes pod. **Pods are the smallest deployable units in Kubernetes and can contain one or more containers**.

- `metadata`: This section contains metadata about the pod, including its name. In this case, the name of the pod is set as "nginx".

- `spec`: The "spec" section describes the desired state of the pod and its contents, such as the containers running within it.

- `containers`: This section lists the containers within the pod. In this case, there is one container defined.

- `image: nginx`: This specifies the Docker image to be used for the container. Here, it indicates the use of the Nginx web server image.

- `name: nginx`: This provides a name for the container, which is set as "nginx" to match the name of the Nginx image.

- `ports`: This section defines the ports to be used by the container.

- `containerPort: 80`: This sets the container's port to 80, which is the default port for the HTTP protocol.

- `name: http`: This provides a name for the port, which is set as "http" to specify that it is for handling HTTP traffic.

## Kubernetes Architechure

![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/0ba7a510-a2d8-4300-8f98-636c2ee00e02)


#### Master Node:

- **API Server:**
  - Acts as the front-end for the Kubernetes control plane.
  - Responsible for:
    - Authentication
    - Authorization
    - Validation
    - Communicates with etcd

- **Scheduler:** Assigns workloads to nodes based on resource availability and constraints.
- **Controller Manager:** Manages different types of controllers.
- **etcd:** A distributed key-value store that stores the cluster's configuration data.(nosql database)
  - Stores the infrastructure configuration.
  - Used for persisting Kubernetes cluster state, including Pod status.

#### Worker Nodes:

- **Kubelet:** Acts as the primary node agent that communicates with the master node.
- **Kube-Proxy:** Manages network communication between different services and components.
- **Container Runtime:** Responsible for running containers, such as Docker or containerd.

#### Pods:

- A Pod is the basic building block of Kubernetes representing a single instance of a running process.

#### Labels and Selectors:

- **Labels:** Key-value pairs attached to objects for logical groupings.
- **Selectors:** Identify a set of objects sharing common labels.

#### Services:

- Provide a way to abstract and expose an application running on a set of Pods as a network service.

#### Volumes:

- Provide a way for containers to store and access data.

#### Namespaces:

- Virtual clusters within a physical cluster used to divide resources between multiple users or projects.

***
**Replica Set**

Replicas in Kubernetes refer to the copies of a pod that ensure high availability. ReplicaSets manage these copies, ensuring a specified number of replicas run continuously. They help maintain application reliability and facilitate easy scaling. They work alongside Deployments for advanced deployment strategies like rolling updates and rollbacks.
  -cant do update and roll back

**Deployment**
Deployment is an object that helps manage the rollout and updates of application instances. Deployments allow you to declaratively define the desired state of your application and handle updates seamlessly, ensuring that the application remains available during the update process. They enable features such as rolling updates, rollbacks, and scaling, making them a crucial tool for managing the lifecycle of applications in a Kubernetes cluster.
    -internally create replica set
  
-rolling update
-roll back
-load balancing (clisterip)
-node port - talk to the ip of node machine
-labels
- get pod ---show-labels
- 

**Kubernetes Service**




***
### Important Kubernetes Commands

**Managing Resources**

* To create or update resources based on a configuration file:
    ```
    kubectl apply -f <filename>
    ```
* To view Kubernetes resources such as pods, services, and deployments:
    ```
    kubectl get <resource>
    ```
* To view detailed information about a specific resource:
    ```
    kubectl describe <resource> <resource-name>
    ```
* To delete resources by filename or resource type and name:
    ```
    kubectl delete -f <filename>
    kubectl delete <resource> <resource-name>
    ```

**Inspecting and Managing Pods and Containers**

* To execute a command on a container within a pod:
    ```
    kubectl exec -it <pod-name> -- <command>
    ```
* To access logs from a container within a pod:
    ```
    kubectl logs <pod-name>
    ```

**Scaling Deployments**

* To scale the number of replicas in a deployment:
    ```
    kubectl scale --replicas=<number> deployment/<deployment-name>
    ```

 **Exposing Resources**

* To expose a deployment, service, or pod as a new Kubernetes service:
    ```
    kubectl expose <resource> <name> --type=NodePort --port=<port>
    ```

**Creating and Updating Deployments**

* To create a Kubernetes deployment:
    ```
    kubectl create deployment <name> --image=<image-name>
    ```
* To update the image of a container in a deployment:
    ```
    kubectl set image deployment/<deployment-name> <container-name> = <new-image>
    ```

**Checking the Cluster Status**

* To check the status of the cluster and its components:
    ```
    kubectl cluster-info
    kubectl get componentstatuses
    ```

**Managing Nodes**

* **kubectl get nodes** - List all of the nodes in the cluster.
* **kubectl describe node <node-name>** - Get detailed information about a specific node.
* **kubectl delete node <node-name>** - Delete a node from the cluster.

**Managing Services**

* **kubectl create service <service-name> --type=LoadBalancer --port=<port>** - Create a new LoadBalancer service.

**Port Forwarding**

* **kubectl port-forward <pod-name> <local-port>:<container-port>** - Forward a local port to a container port on a pod.

**Monitoring**

* **kubectl top pod** - Display the resource usage of all pods in the cluster.
* **kubectl top node** - Display the resource usage of all nodes in the cluster.

**Resource Documentation**

* **kubectl explain <resource-type>** - Get a detailed explanation of a Kubernetes resource type. 

### Ingress:

- Manages external access to services within a cluster.

