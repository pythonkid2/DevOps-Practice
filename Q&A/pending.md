
### 4. **Sample Jenkins Pipeline using Shared Library (Declarative and Scripted):**
   - **Declarative:**
     ```groovy
     pipeline {
       agent any
       libraries {
         lib 'my-shared-library@master'
       }
       stages {
         stage('Build') {
           steps {
             script {
               mySharedLibrary.someMethod()
             }
           }
         }
       }
     }
     ```
   - **Scripted:**
     ```groovy
     @Library('my-shared-library@master') _
     node {
       mySharedLibrary.someMethod()
     }
     ```

### 5. **Integrating Shared Library in Jenkins:**
   - Define the library in the Jenkins configuration under "Manage Jenkins" -> "Configure System" -> "Global Pipeline Libraries".

### 6. **Building and Running Pipeline with a Specific Version of a Build Tool:**
   - Use tools like `tool` directive in Jenkins declarative pipeline or specific Docker images containing the required version.

### 7. **Providing Authentication in Jenkins:**
   - Authentication can be provided using Jenkins user credentials, LDAP, or other authentication plugins.

### 8. **Managing Sensitive Credential Details and Tokens:**
   - Use Jenkins credentials store, environment variables, or third-party tools like HashiCorp Vault.

### 9. **Integrating with SonarQube:**
   - Use the `SonarQube Scanner` plugin in Jenkins and configure the necessary SonarQube server details in the Jenkins configuration.

### 10. **Sample Dockerfile for Python App:**
   ```Dockerfile
   FROM python:3.8-slim
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .
   CMD ["python", "app.py"]
   ```

### 11. **Building and Running the Dockerfile:**
   - Build: `docker build -t python-app .`
   - Run: `docker run -p 5000:5000 python-app`

### 12. **Deployment Strategy:**
   - Common strategies include Blue-Green, Canary, and Rolling deployments.

### 13. **Managing Blue-Green Deployments and Traffic Switching:**
   - Use load balancers or DNS to switch traffic between the blue (current) and green (new) environments.

### 14. **What is a Module in Terraform?**
   - A module is a container for multiple resources that are used together. Modules are the building blocks of Terraform.

### 15. **Managing and Deploying Infrastructure using Terraform:**
   - Use `.tf` configuration files to define the infrastructure, and use `terraform init`, `terraform plan`, and `terraform apply` to manage and deploy.

### 16. **Sample Terraform Script:**
   ```hcl
   provider "aws" {
     region = "us-west-2"
   }

   resource "aws_instance" "example" {
     ami           = "ami-0c55b159cbfafe1f0"
     instance_type = "t2.micro"
   }
   ```

### 17. **Components in Terraform Module:**
   - Variables, Resources, Outputs, and Data Sources.

### 18. **Migrating Existing Resources to Terraform:**
   - Use `terraform import` to import existing resources into Terraform state.

### 19. **Backing Up State File:**
   - Store state files in a remote backend like AWS S3, GCS, or a version control system.

### 20. **Difference Between Deployment and ReplicaSet YAML:**
   - **Deployment**: Manages a ReplicaSet and provides declarative updates to applications.
   - **ReplicaSet**: Ensures a specified number of pod replicas are running.

### 21. **Sample Deployment YAML for Python App:**
   ```yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: python-app
   spec:
     replicas: 2
     selector:
       matchLabels:
         app: python-app
     template:
       metadata:
         labels:
           app: python-app
       spec:
         containers:
         - name: python-app
           image: python-app:latest
           ports:
           - containerPort: 5000
   ```

### 22. **Managing Logs:**
   - Use centralized logging solutions like ELK Stack, Fluentd, or Loki.

### 23. **Viewing the Last 100 Logs from a Log File:**
   - Use `tail -n 100 logfile`.

### 24. **Running Parallel Configurations in Ansible:**
   - Use the `--forks` flag to set the number of parallel tasks.

### 25. **Using Ansible Tower:**
   - Ansible Tower provides a web-based interface, REST API, and task scheduling.

### 26. **What is an Ansible Role?**
   - An Ansible Role is a way to package and organize reusable Ansible content.

### 27. **Configuring a Windows Machine using Ansible:**
   - Use the `winrm` protocol and Ansible modules designed for Windows.

### 28. **Kubernetes Architecture:**
   - Consists of a master node (API Server, Controller Manager, Scheduler, etcd) and worker nodes (kubelet, kube-proxy, container runtime).

### 29. **What is Kubelet and its Role?**
   - The kubelet is an agent that runs on each node and ensures containers are running in a pod.

### 30. **Backing Up Kubernetes:**
   - Use tools like Velero to back up and restore Kubernetes cluster resources and persistent volumes.

### 31. **Using Kubelet Instead of Kubectl:**
   - No, kubelet is an agent that runs on nodes, while kubectl is a command-line tool for interacting with the Kubernetes API server.

### 32. **Scaling in Kubernetes:**
   - Use `kubectl scale` to adjust the number of replicas for a deployment or StatefulSet.

### 33. **Vertical and Horizontal Scaling:**
   - **Vertical Scaling**: Increase the resource capacity of a node.
   - **Horizontal Scaling**: Increase the number of pod replicas.

### 34. **What You See When Running `kubectl get no` in EKS:**
   - The list of worker nodes in the cluster. Master nodes are managed by AWS and are not visible.

### 35. **Why Master Node is Not Visible:**
   - In EKS, the control plane is managed by AWS and is abstracted from the user.

### 36. **What is a Namespace and Its Use:**
   - A namespace is a virtual cluster within a Kubernetes cluster, used to isolate resources and manage environments.

### 37. **Allocating Resources to a Namespace (Sample YAML):**
   ```yaml
   apiVersion: v1
   kind: ResourceQuota
   metadata:
     name: example
     namespace: dev
   spec:
     hard:
       requests.cpu: "1"
       requests.memory: "1Gi"
       limits.cpu: "2"
       limits.memory: "2Gi"
   ```

### 38. **Kubernetes Services:**
   - ClusterIP, NodePort, LoadBalancer, ExternalName.

These answers provide a good starting point, and you can expand on them based on the context of your experience and the specific requirements of the interviewer. If you need further elaboration on any specific question, feel free to ask!
