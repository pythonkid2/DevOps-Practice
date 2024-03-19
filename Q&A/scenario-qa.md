- [Q1](#Q1)
how you can set up a Jenkins pipeline using Terraform to create an AWS load balancer and automatically destroy it after a day
- [Q2](#Q2)
Creating a real-time AWS project to host a website on an EC2 instance using a combination of AWS, Ansible, Terraform, Git, Jenkins, Docker, Kubernetes (K8s), Prometheus, and Grafana
- [Q3](#Q3)



## Q1

To create a pipeline using Jenkins and Terraform that automatically destroys AWS resources (in this case, a load balancer) after a day to avoid cost problems, you can follow these steps:

1. **Set Up Jenkins**:
   - Install Jenkins on a server or use a Jenkins instance.
   - Install necessary plugins like the Pipeline plugin for Jenkins.

2. **Set Up Terraform**:
   - Install Terraform on the machine where Jenkins is running.
   - Configure the AWS provider in Terraform with appropriate credentials.

3. **Create a Jenkins Pipeline**:
   - Create a new Jenkins pipeline job.
   - Define the pipeline script in the Jenkinsfile.

4. **Define the Terraform Configuration**:
   - Create Terraform configuration files to create the AWS resources, in this case, an AWS load balancer.
   - Include a resource that schedules the destruction of the load balancer after a day. This can be achieved using a `time_sleep` resource in Terraform.

5. **Pipeline Steps**:
   - The pipeline steps should include:
     - Checkout code from your version control system.
     - Initialize Terraform.
     - Plan and apply Terraform to create the load balancer.
     - Schedule the destruction of the load balancer after a day.
     - Commit the changes to the Terraform configuration back to the repository.

6. **Destroy Resources**:
   - Create a separate Jenkins job that runs daily to destroy the resources created by Terraform after a day.
   - This job should run a Terraform destroy command to remove the load balancer.

By following these steps, you can create a pipeline using Jenkins and Terraform that automatically destroys AWS resources, such as a load balancer, after a day to prevent cost problems. This approach helps in managing resources efficiently and avoiding unnecessary costs from running resources longer than needed.

---

Below is an example of how you can set up a Jenkins pipeline using Terraform to create an AWS load balancer and automatically destroy it after a day:

1. **Jenkins Pipeline Script (Jenkinsfile)**:
```groovy
pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/your-repo.git'
            }
        }
        
        stage('Terraform Apply') {
            steps {
                script {
                    sh 'terraform init'
                    sh 'terraform plan -out=tfplan'
                    sh 'terraform apply tfplan'
                }
            }
        }
    }
    
    post {
        always {
            script {
                sh 'echo "Destroying resources after a day"'
                sh 'terraform destroy -auto-approve'
            }
        }
    }
}
```

2. **Terraform Configuration**:
- Create a Terraform configuration file (e.g., `main.tf`) to define the AWS load balancer and schedule its destruction after a day.
- Here is an example of how you can use the `time_sleep` resource in Terraform to schedule the destruction after a day:
```hcl
resource "aws_lb" "example" {
  // AWS load balancer configuration
}

resource "time_sleep" "destroy_after_day" {
  depends_on = [aws_lb.example]
  duration   = "1d"
}
```

3. **Jenkins Job for Daily Destruction**:
- Create a separate Jenkins job that runs daily to destroy the resources created by Terraform after a day.
- This job should run a Terraform destroy command to remove the load balancer.

By setting up the Jenkins pipeline with Terraform and scheduling the destruction of resources after a day, you can automate the process of creating and destroying AWS resources to avoid unnecessary costs.

## Q2

Creating a real-time AWS project to host a website on an EC2 instance using a combination of AWS, Ansible, Terraform, Git, Jenkins, Docker, Kubernetes (K8s), Prometheus, and Grafana involves several steps. Below is an outline of the project along with the code and explanations for each component:

### Project Overview:
- **Objective**: Host a website on an AWS EC2 instance using automation tools and monitoring services.
- **Tools**: AWS, Ansible, Terraform, Git, Jenkins, Docker, Kubernetes (K8s), Prometheus, and Grafana.

### Steps to Implement the Project:

1. **Terraform Configuration**:
   - Use Terraform to provision an EC2 instance in AWS.
   - Define the necessary AWS resources in a Terraform configuration file (e.g., `main.tf`).

2. **Ansible Playbook**:
   - Create an Ansible playbook to configure the EC2 instance.
   - Install and configure the web server (e.g., Nginx) to host the website.
   - Use Ansible roles for better organization and reusability.

3. **Dockerize the Website**:
   - Containerize the website using Docker.
   - Create a Dockerfile to build the website image.

4. **Setting up Jenkins Pipeline**:
   - Create a Jenkins pipeline to automate the deployment process.
   - Include stages for checking out code, building Docker images, deploying to the EC2 instance, etc.

5. **Kubernetes Deployment**:
   - Deploy Kubernetes cluster using tools like kops or EKS.
   - Deploy the Dockerized website as a Kubernetes deployment.

6. **Monitoring with Prometheus and Grafana**:
   - Set up Prometheus to collect metrics from the website and services.
   - Configure Grafana for visualization and monitoring dashboards.

### Code Snippets and Explanations:

1. **Terraform Configuration (`main.tf`)**:
```hcl
provider "aws" {
  region = "us-west-2"
}

resource "aws_instance" "web_server" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  tags = {
    Name = "WebServerInstance"
  }
}
```

2. **Ansible Playbook (`webserver.yml`)**:
```yaml
---
- hosts: web_server
  become: true
  tasks:
    - name: Install Nginx
      apt:
        name: nginx
        state: present
```

3. **Jenkins Pipeline Script**:
```groovy
pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/your-repo.git'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t my-website .'
            }
        }
        
        stage('Deploy to EC2') {
            steps {
                sh 'docker run -d -p 80:80 my-website'
            }
        }
    }
}
```

4. **Kubernetes Deployment**:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: website-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: website
  template:
    metadata:
      labels:
        app: website
    spec:
      containers:
      - name: website
        image: my-website
        ports:
        - containerPort: 80
```

5. **Prometheus and Grafana Setup**:
   - Configure Prometheus to scrape metrics from the website.
   - Set up Grafana to visualize Prometheus metrics and create dashboards.

By following these steps and using the provided code snippets, you can create a comprehensive project to host a website on an AWS EC2 instance with automation, containerization, orchestration, and monitoring capabilities.

+++

## Q3

### For monitoring 20 VMs
For monitoring 20 VMs, you typically wouldn't install the monitoring tools (like Node Exporter and cAdvisor) directly on all the machines. Here's a more efficient approach:

**Monitoring Agent vs. Centralized Collection:**

* **Agent-based monitoring:** Installing individual monitoring agents on each VM can be cumbersome to manage and maintain for 20 machines. It might also consume resources on each VM.
* **Centralized collection:** A more scalable approach is to use a **monitoring server** with a central collection point. The monitoring tools like Node Exporter and cAdvisor would be installed on **each VM**, but they would then **expose their metrics** to the monitoring server.

**How it Works:**

1. **Monitoring Server:** You'll need to set up a dedicated monitoring server or use a hosted monitoring service. Popular options include Prometheus (open-source) or Datadog (commercial).
2. **Monitoring Agent (Lightweight):** Install a lightweight monitoring agent on each VM. These agents are designed to collect metrics and send them to the central monitoring server.  For Node Exporter and cAdvisor, no additional agent might be needed as they can expose metrics directly.
3. **Metric Collection:** The monitoring server periodically scrapes metrics from the agents or directly from tools like Node Exporter and cAdvisor running on each VM.
4. **Data Storage and Visualization:** The monitoring server stores the collected metrics in a time-series database and allows you to visualize them using dashboards and graphs.

**Benefits:**

* **Centralized Management:** Easier to manage and update the monitoring configuration from a single location (monitoring server).
* **Scalability:** This approach scales well as you add more VMs to your infrastructure.
* **Reduced Resource Consumption:** Lightweight agents on VMs minimize resource impact compared to full-fledged monitoring tools.

**Time to Set Up:**

The time to set up monitoring for 20 VMs depends on several factors:

* **Your technical expertise:** If you're familiar with monitoring tools and configuration, it could take a few hours to set up a basic monitoring system.
* **Complexity of your environment:** If you have a complex infrastructure with diverse VM configurations, it might take longer to configure the monitoring agents or tools on each VM.
* **Monitoring platform choice:** Setting up a self-hosted monitoring server like Prometheus might take longer initially compared to using a hosted monitoring service with a user-friendly interface.

Here's a rough estimate:

* **Basic Setup:** 2-4 hours for a familiar user with a straightforward environment and a hosted monitoring service.
* **Complex Setup:**  4-8 hours or more for a less familiar user with a complex environment and self-hosted monitoring.

**Additional Tips:**

* Start with a pilot on a few VMs to test your monitoring configuration before deploying to all 20 VMs.
* Use pre-built dashboards and templates offered by your monitoring platform to visualize common metrics quickly.
* Consider automation tools like Ansible or Chef to automate the deployment of monitoring agents on your VMs for faster and more consistent configuration.

By using a centralized monitoring approach, you can efficiently monitor the health and performance of all your 20 VMs from a single platform.


## Example: Routing Traffic with Ingress in Kubernetes

**Scenario:**

Let's say you have two web applications deployed as services in your Kubernetes cluster:

* **Service A:** Exposes a frontend application at port 8080.
* **Service B:** Exposes a backend API at port 9000.

You want to access these services through a single external IP address with proper routing:

* Requests to `/` should be routed to Service A (frontend).
* Requests to `/api/*` should be directed to Service B (backend API).

**Here's how you can achieve this using Ingress:**

**1. Define the Ingress Resource (ingress.yaml):**

```yaml
apiVersion: networking.k8s.io/v1beta1
kind: Ingress
metadata:
  name: my-ingress
spec:
  rules:
  - http:
      paths:
      - path: /
        backend:
          service:
            name: frontend-service
            port:
              number: 8080
      - path: /api/*
        backend:
          service:
            name: backend-api
            port:
              number: 9000
```

**Explanation:**

* This YAML file defines an Ingress named `my-ingress`.
* The `spec` section defines the desired routing rules.
* There's a single HTTP rule with two paths:
    * `/`: This path is routed to `frontend-service` on port 8080 (your frontend application).
    * `/api/*`: This path pattern (any path starting with `/api/`) is directed to `backend-api` on port 9000 (your backend API).

**2. Deploy the Ingress Resource:**

Use `kubectl apply -f ingress.yaml` to create the Ingress resource in your Kubernetes cluster.

**3. Ingress Controller Configuration (**Assumed, not required in YAML)

An Ingress controller running in your cluster will automatically pick up this Ingress resource and configure itself accordingly. The specific configuration depends on the chosen controller (e.g., Nginx Ingress Controller, Traefik).

**4. Accessing the Services:**

Assuming your Ingress controller assigns an external IP address (e.g., 10.10.0.1), you can now access your services through this IP:

* http://10.10.0.1/ will display the frontend application (Service A).
* http://10.10.0.1/api/your-api-endpoint will reach your backend API (Service B).

**Remember:**

* You'll need an Ingress controller deployed and configured in your cluster for this to work.
* This is a basic example. Ingress offers more advanced features like SSL termination and virtual hosting.

