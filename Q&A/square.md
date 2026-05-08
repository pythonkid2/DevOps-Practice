# AWS / DevOps Scenario-Based Interview Questions & Answers


---

# 1. What is the difference between AWS WAF and AWS Shield, and where would you use them?

## Answer

AWS WAF protects applications from Layer 7 attacks like:

- SQL injection
- XSS
- Bad HTTP requests
- Rate limiting

It works with:

- ALB
- CloudFront
- API Gateway

AWS Shield protects against DDoS attacks.

- Shield Standard gives basic automatic protection
- Shield Advanced gives advanced DDoS protection and monitoring

Usually we use:

- Shield for network/volumetric attack protection
- WAF for application-level filtering

### Typical Architecture

```text
Users → CloudFront + WAF + Shield → ALB → Application
```

---

# 2. If GuardDuty detects suspicious activity from an EC2 instance, what steps would you take?

## Answer

First, I would check the GuardDuty finding details:

- affected EC2
- suspicious IP
- type of attack/activity

Then I would:

### 1. Isolate the EC2 instance

- remove from load balancer
- restrict security group if needed

### 2. Check logs

- CloudTrail logs
- VPC Flow Logs
- application/system logs

### 3. Verify suspicious activity

- unusual processes
- unauthorized access
- crypto mining activity
- suspicious outbound traffic

### 4. Rotate compromised credentials

If required.

### 5. Patch or rebuild the server

- use hardened AMI
- close unnecessary ports
- improve IAM/security rules
- add monitoring and alerts

---

# 3. How would you design a secure VPC architecture for a production application?

## Answer

I would design the VPC with multiple layers.

### Public Subnet

Contains:
- ALB
- NAT Gateway

### Private Subnet

Contains:
- application servers
- databases

### Security Approach

- Only ALB exposed to internet
- EC2 and DB remain private
- Restrictive Security Groups
- Least privilege access
- Use IAM roles instead of access keys

### Additional Security

- WAF + Shield for external protection
- GuardDuty + CloudTrail for monitoring
- Encryption using KMS
- Secrets stored in Secrets Manager

### Typical Architecture

```text
Internet
   ↓
CloudFront + WAF + Shield
   ↓
Public Subnet → ALB
   ↓
Private Subnet → App Servers
   ↓
Private DB Subnet → RDS
```

---

# 4. We have a 3-tier Java application currently running on a single EC2 instance. Due to increased traffic, we need better scalability and high availability without rewriting the application immediately. How would you redesign or migrate the architecture step by step?

## Answer

First, I would identify the main problems:

- single point of failure
- no scalability
- downtime during deployments

Instead of directly moving to microservices, I would improve the architecture gradually.

### Step 1 — Separate Layers Properly

- frontend
- backend
- database

### Step 2 — Move Database to RDS

Use:
- RDS Multi-AZ
- automated backups
- high availability

### Step 3 — Add Load Balancer and Auto Scaling

- Place ALB in front
- Create Auto Scaling Group
- Deploy EC2 instances across multiple AZs

### Architecture

```text
Users → ALB → Multiple App Servers → RDS
```

### Benefits

- high availability
- fault tolerance
- horizontal scaling

### Step 4 — Externalize State

- Sessions → Redis/ElastiCache
- Files → S3

### Step 5 — CI/CD

Implement:
- Jenkins or GitHub Actions
- automated deployments
- rolling deployments

### Step 6 — Containerization

- Dockerize application
- move to ECS or EKS later if required

### Why not microservices immediately?

Because microservices introduce:
- service communication complexity
- distributed tracing
- Kubernetes overhead
- monitoring complexity

A properly scaled monolith can still handle large traffic efficiently.

---

# 5. Your company has 30 VPCs across 4 AWS accounts that need to talk to each other and also connect to your on-premises data center. Would you use VPC Peering, Transit Gateway, or PrivateLink? Why?

## Answer

I would use Transit Gateway.

### Why not VPC Peering?

VPC Peering:
- is one-to-one
- not transitive
- difficult to manage at scale

For 30 VPCs:
- around 435 peering connections required
- route table management becomes complex

### Why not PrivateLink?

PrivateLink is mainly for:
- exposing specific services privately

Not for:
- full network connectivity

### Why Transit Gateway?

Transit Gateway acts as a central hub.

Benefits:
- each VPC attaches once
- centralized routing
- easier management
- scalable architecture

On-premises can connect using:
- Direct Connect
or
- VPN

TGW can also be shared across accounts using AWS RAM.

### Final Architecture

```text
On-Prem
   ↓
Direct Connect / VPN
   ↓
Transit Gateway
   ↓
Multiple VPCs across accounts
```

---

# 6. A team is running 200 EC2 instances 24/7 for a workload that's only busy 9am–6pm on weekdays. Walk through the options to cut cost.

## Answer

Main observation:

- workload is not busy full time
- major cost saving comes from reducing runtime first

### Step 1 — Scheduled Scaling

Use:
- Auto Scaling scheduled actions

Actions:
- scale up before office hours
- scale down after office hours
- reduce instances during weekends

This gives the biggest and fastest savings.

### Step 2 — Right Sizing

Use:
- CloudWatch metrics
- AWS Compute Optimizer

Check:
- CPU usage
- memory utilization
- oversized instances

### Step 3 — Savings Plans / Reserved Instances

Use for baseline always-running instances.

Options:
- Compute Savings Plans
- EC2 Savings Plans
- Reserved Instances

### Step 4 — Spot Instances

Use Spot for:
- stateless workloads
- batch jobs
- CI/CD runners

Avoid for:
- databases
- critical workloads

### Step 5 — Graviton Migration

Benefits:
- lower cost
- better performance

But test application compatibility first.

### Recommended Strategy

1. Scheduled scaling
2. Right sizing
3. Savings Plans
4. Spot Instances
5. Graviton optimization

Combined savings can reach 70–85%.

---
````md id="5bzk90"
# Kubernetes / EKS Scenario-Based Interview Questions & Answers

---

# 1. A production pod is stuck in CrashLoopBackOff. How would you troubleshoot it step by step?

## Answer

First, I would identify the reason for the crash.

### Step 1 — Check Pod Status

```bash
kubectl get pods
kubectl describe pod <pod-name>
```

Check:
- Events
- Last terminated reason
- Exit codes

---

### Step 2 — Check Logs

```bash
kubectl logs <pod-name>
kubectl logs <pod-name> --previous
```

`--previous` helps if container already restarted.

---

### Step 3 — Verify Common Issues

Check for:
- application startup failure
- wrong environment variables
- DB connectivity issues
- missing secrets/configmaps
- port conflicts
- insufficient memory causing OOMKilled

---

### Step 4 — Check Health Probes

Misconfigured:
- livenessProbe
- readinessProbe

can continuously restart containers.

---

### Step 5 — Verify Resources

Check:
```bash
kubectl top pod
```

Possible issues:
- CPU throttling
- memory exhaustion

---

### Step 6 — Node-Level Investigation

Check:
- node health
- disk pressure
- kubelet issues

---

# 2. A deployment has 5 replicas, but only 2 are running and others are Pending. How would you investigate?

## Answer

Pending means scheduler cannot place the pods.

### Step 1 — Describe Pod

```bash
kubectl describe pod <pod-name>
```

Check Events section carefully.

---

### Common Reasons

#### Insufficient Resources

- CPU shortage
- memory shortage

---

#### Node Selector / Taints

Pods may require:
- specific labels
- tolerations

---

#### PVC Issues

Pods waiting for:
- Persistent Volume
- storage class

---

#### Cluster Autoscaler Issues

New nodes may not be getting created.

---

### Step 2 — Check Nodes

```bash
kubectl get nodes
kubectl describe node <node-name>
```

Check:
- allocatable resources
- taints
- node conditions

---

### Step 3 — Check Autoscaler

In EKS:
- verify ASG scaling
- cluster autoscaler logs

---

# 3. A service is unable to connect to another service inside the cluster. How would you troubleshoot networking?

## Answer

### Step 1 — Verify Service

```bash
kubectl get svc
kubectl describe svc <service-name>
```

Check:
- selector labels
- endpoints

---

### Step 2 — Verify Endpoints

```bash
kubectl get endpoints
```

If endpoints are empty:
- labels may not match

---

### Step 3 — Test DNS Resolution

```bash
nslookup service-name
curl service-name
```

---

### Step 4 — Verify Network Policies

Check if traffic is blocked by:
- NetworkPolicy

---

### Step 5 — Check Pod Connectivity

Exec into pod:

```bash
kubectl exec -it <pod> -- sh
```

Test:
- ping
- curl
- telnet


### Step 6 — Check CNI Plugin

In EKS:
- aws-node
- CoreDNS
- kube-proxy

must be healthy.

## Interview Question

What is the difference between Cluster Autoscaler and Karpenter in EKS, and why would you choose one over the other?

## Sample Answer

Cluster Autoscaler and Karpenter are both used to automatically scale worker nodes in Kubernetes clusters, but they work differently.

Cluster Autoscaler works by scaling existing Auto Scaling Groups or EKS Managed Node Groups. If pods are pending, it increases the desired capacity of the node group. It depends on preconfigured instance types and node groups.

Karpenter is a newer Kubernetes-native autoscaler from AWS. Instead of scaling predefined node groups, it directly provisions EC2 instances based on pod requirements like CPU, memory, and pricing. It dynamically selects the most suitable instance type.

### Key Differences

* Cluster Autoscaler scales node groups.
* Karpenter dynamically provisions nodes.
* Karpenter provides faster scaling and better cost optimization.
* Karpenter supports better spot instance handling and bin packing.
* Cluster Autoscaler requires predefined ASGs, while Karpenter does not.

### When to Choose

* Use Cluster Autoscaler in simpler or legacy setups already using managed node groups.
* Use Karpenter for modern EKS environments where:

  * faster scaling is needed
  * spot optimization is important
  * workloads are dynamic
  * cost optimization matters

In most modern AWS EKS setups, Karpenter is generally preferred.

# 4. How will you upgrade Kubernetes version & how would you reduce downtime during EKS node upgrades?

## Answer

### EKS Upgrade Order

1. Upgrade EKS control plane
2. Upgrade managed node groups
3. Upgrade add-ons:
   - CoreDNS
   - kube-proxy
   - VPC CNI

---

### Reduce Downtime Strategy

#### Use Multiple Nodes

Applications should run:
- multiple replicas
- across multiple AZs

---

#### Configure PodDisruptionBudget

Ensures minimum pods remain available.

Example:

```yaml
minAvailable: 2
```

---

#### Rolling Node Upgrade

During upgrade:
- cordon node
- drain node
- move workloads safely

Commands:

```bash
kubectl cordon <node>
kubectl drain <node> --ignore-daemonsets
```

---

#### Use Readiness Probes

Traffic only goes to healthy pods.

---

#### Use Cluster Autoscaler

New nodes should become ready before old nodes terminate.

---

# 5. You need to deploy a stateful application like PostgreSQL or MongoDB on Kubernetes. What considerations are important?

## Answer

Stateful applications need persistent storage and stable identity.

### Important Considerations

#### Use StatefulSet

Provides:
- stable pod names
- ordered deployment
- stable storage

---

#### Persistent Volumes

Use:
- EBS
- EFS

with PersistentVolumeClaims.

---

#### Backup Strategy

Implement:
- automated backups
- snapshot strategy

---

#### High Availability

For MongoDB/PostgreSQL:
- replication
- multi-node setup

---

#### Resource Planning

Stateful apps require:
- guaranteed storage
- proper memory sizing
- CPU allocation

---

#### Anti-Affinity

Distribute replicas across nodes/AZs.

---

# 6. How would you securely expose a Kubernetes application to the internet?

## Answer

### Recommended Architecture

```text
Internet
   ↓
CloudFront + WAF
   ↓
ALB Ingress Controller
   ↓
Ingress
   ↓
Service
   ↓
Pods
```

---

### Security Best Practices

#### Use Ingress Instead of NodePort

Ingress gives:
- centralized routing
- TLS termination
- better security

---

#### Enable HTTPS

Use:
- ACM certificates
- TLS termination at ALB

---

#### Use WAF

Protect against:
- SQL injection
- XSS
- malicious requests

---

#### Restrict Security Groups

Only expose:
- ALB publicly

Nodes should remain private.

---

#### Use Network Policies

Restrict pod-to-pod communication.

---

# 7. How would you securely allow pods in EKS to access AWS services like S3 or DynamoDB?

## Answer

Best practice is using IAM Roles for Service Accounts (IRSA).

### Why IRSA?

Avoids:
- hardcoded AWS keys
- shared node IAM roles

---

### Flow

1. Create IAM policy
2. Create IAM role
3. Map role to Kubernetes service account
4. Attach service account to pod

Then pod gets temporary AWS credentials securely.

---

### Benefits

- least privilege access
- temporary credentials
- better auditing

---

# 8. Your EKS worker nodes are in private subnets. How do the nodes pull Docker images and communicate with AWS APIs?

## Answer

Private nodes do not have direct internet access.

### Common Solution

Use:
- NAT Gateway

for outbound internet access.

This allows:
- image pull from ECR
- AWS API communication

---

### Better Optimization

Use VPC Endpoints for:
- ECR API
- ECR DKR
- S3
- STS

This reduces:
- internet dependency
- NAT cost

---

### Recommended Architecture

```text
Private Nodes
   ↓
VPC Endpoints / NAT Gateway
   ↓
AWS Services
```

---

# 9. You are running multiple workloads in EKS and one noisy application is affecting others. How would you isolate workloads?

## Answer

This usually happens due to resource contention.

### Step 1 — Define Resource Requests & Limits

Example:

```yaml
resources:
  requests:
    cpu: "500m"
    memory: "1Gi"
  limits:
    cpu: "1"
    memory: "2Gi"
```

This prevents one app from consuming everything.

---

### Step 2 — Use Separate Node Groups

Critical workloads can run on:
- dedicated nodes

using:
- taints
- tolerations
- node selectors

---

### Step 3 — Use Namespaces & Quotas

Apply:
- ResourceQuota
- LimitRange

to control namespace resource usage.

---

### Step 4 — Priority Classes

Critical workloads get higher scheduling priority.

---

### Step 5 — Monitoring

Use:
- Prometheus
- Grafana
- CloudWatch

to identify noisy neighbors early.
````

````md id="75m4e6"
# CI/CD Scenario-Based Interview Questions & Answers

Good for evaluating DevOps engineers with 3–5 years experience.

---

# 1. Tell me about your pipeline stages.

## Answer

A typical CI/CD pipeline I use contains these stages:

### Stage 1 — Code Checkout

- Pull code from GitHub/GitLab
- Checkout specific branch/tag

---

### Stage 2 — Build

For Java:
- Maven / Gradle build

For Node.js:
- npm / yarn build

---

### Stage 3 — Unit Testing

Run:
- unit tests
- code quality checks

Optional:
- SonarQube scanning

---

### Stage 4 — Docker Build

- Build Docker image
- Tag image properly

Example:
```text
app:v1.0.25
app:git-commit-id
```

---

### Stage 5 — Security/Image Scan

Tools:
- Trivy
- Snyk

Check:
- vulnerabilities
- critical CVEs

---

### Stage 6 — Push Image

Push image to:
- ECR
- DockerHub
- Harbor

---

### Stage 7 — Update Deployment Files

Update:
- Helm values
or
- Kubernetes manifests

with latest image tag.

---

### Stage 8 — Deploy to Kubernetes

Deployment using:
- kubectl
- Helm
- ArgoCD GitOps

---

### Stage 9 — Verification

Verify:
- pod health
- rollout status
- smoke tests

Commands:
```bash
kubectl rollout status deployment/app
kubectl get pods
```

---

# 2. A Jenkins pipeline suddenly starts failing after working fine for months. How would you troubleshoot it?

## Answer

First, I would identify where exactly the failure happens.

### Step 1 — Check Jenkins Console Logs

Check:
- exact failed stage
- error message
- recent changes

---

### Step 2 — Verify Recent Changes

Possible causes:
- code changes
- plugin updates
- expired credentials
- infrastructure changes

---

### Step 3 — Check Jenkins Agent

Verify:
- disk space
- memory
- Docker daemon
- network connectivity

---

### Step 4 — Validate Credentials

Check:
- expired AWS tokens
- Kubernetes secrets
- Git credentials

---

### Step 5 — Verify External Dependencies

Check:
- GitHub availability
- Docker registry
- EKS/API connectivity

---

### Step 6 — Reproduce Locally

Try:
- Docker build locally
- kubectl commands manually

---

# 3. A deployment succeeded in Jenkins, but the application is not updated in Kubernetes. What would you check?

## Answer

First, I would verify whether Kubernetes actually pulled the new image.

### Step 1 — Check Deployment Image

```bash
kubectl describe deployment app
```

Verify image tag.

---

### Step 2 — Check Pods

```bash
kubectl get pods
kubectl describe pod <pod>
```

---

### Common Issue

Using:
```text
latest
```

tag repeatedly.

Kubernetes may reuse cached image.

---

### Step 3 — Verify Image Pull Policy

Should use:

```yaml
imagePullPolicy: Always
```

or preferably unique version tags.

Example:
```text
app:v1.0.21
```

---

### Step 4 — Verify ArgoCD Sync

Check:
- OutOfSync state
- Git repo updated or not

ArgoCD deploys based on Git changes, not Jenkins success.

---

### Step 5 — Check Rollout Status

```bash
kubectl rollout status deployment/app
```

---

# 4. A pipeline takes 45 minutes to complete and developers complain it's too slow. How would you optimize it?

## Answer

First, I would identify which stage consumes the most time.

### Common Optimizations

#### Parallel Stages

Run simultaneously:
- unit tests
- linting
- security scans

---

#### Docker Layer Caching

Reuse existing layers during builds.

---

#### Dependency Caching

Cache:
- Maven dependencies
- npm packages

---

#### Incremental Builds

Build only changed modules.

---

#### Better Jenkins Agents

Use:
- autoscaling agents
- Kubernetes agents

instead of overloaded static servers.

---

#### Reduce Unnecessary Steps

Avoid:
- duplicate builds
- repeated image scans

---

### Monitoring

Measure:
- per-stage execution time
- bottlenecks

before optimizing.

---

# 5. How would you deploy applications to Kubernetes using Jenkins?

## Answer

Typical flow:

### Step 1 — Checkout Code

Pull source from Git.

---

### Step 2 — Build Application

Example:
- Maven build
- npm build

---

### Step 3 — Build Docker Image

```bash
docker build -t app:v1.0.5 .
```

---

### Step 4 — Push Image

Push to:
- ECR
- DockerHub

---

### Step 5 — Update Kubernetes Manifests

Update:
- deployment.yaml
or
- Helm values

with latest image tag.

---

### Step 6 — Deploy

Using:
```bash
kubectl apply -f
```

or:
```bash
helm upgrade
```

or GitOps using ArgoCD.

---

### Step 7 — Verify Rollout

```bash
kubectl rollout status deployment/app
```

---

# 6. Your Jenkins server goes down frequently due to high load. How would you improve scalability and reliability?

## Answer

Main problem is usually:
- too many builds
- insufficient resources
- single point of failure

---

### Solution 1 — Distributed Jenkins Architecture

Use:
- Jenkins master/controller
- multiple agents

instead of running everything on one server.

---

### Solution 2 — Dynamic Agents

Use:
- Kubernetes agents
or
- EC2 auto-scaling agents

Agents are created only during builds.

---

### Solution 3 — Resource Optimization

Increase:
- CPU
- memory

and clean:
- old workspaces
- unused Docker images

---

### Solution 4 — High Availability

Store Jenkins data on:
- EFS
or
- persistent volumes

Regular backups:
- Jenkins home
- configuration
- plugins

---

### Solution 5 — Offload Heavy Work

Move:
- image scans
- large builds

to separate dedicated agents.

---

# 7. What happens if Jenkins pushes an image with the same latest tag every time? How will ArgoCD behave?

## Answer

This is a very common CI/CD issue.

### Problem

If Jenkins always pushes:

```text
app:latest
```

then Kubernetes may not detect any deployment change.

ArgoCD compares:
- Git manifests
- Kubernetes manifests

not Docker image contents.

So if deployment YAML still says:

```yaml
image: app:latest
```

ArgoCD sees no Git change and may not redeploy.

---

### Additional Problem

Even if pod restarts:
- node may use cached image
- old image may continue running

---

### Best Practice

Always use unique immutable tags.

Examples:

```text
app:v1.0.15
app:build-152
app:git-sha
```

Then Jenkins updates Git manifests with new tag.

Example:

```yaml
image: app:v1.0.15
```

ArgoCD detects Git change and syncs deployment properly.

---

# Additional Important CI/CD Questions

## 8. How would you implement zero-downtime deployment in Kubernetes?

Key points:
- rolling updates
- readiness probes
- multiple replicas
- PodDisruptionBudget
- blue/green or canary if needed

---

## 9. How would you securely manage secrets in Jenkins pipelines?

Key points:
- Jenkins credentials store
- AWS Secrets Manager
- Kubernetes secrets
- avoid hardcoded credentials
- IAM roles instead of static keys

---

## 10. How would you implement rollback during failed deployments?

Key points:
- kubectl rollout undo
- Helm rollback
- ArgoCD rollback
- previous stable image tags
- health checks before full rollout
````
# Monitoring / Observability Scenario-Based Interview Questions & Answers

---

# 1. A pod keeps restarting randomly every few hours. Which metrics and logs would you check?

## Answer

First, I would identify whether the restart is application-related, resource-related, or node-related.

### Step 1 — Check Pod Status

```bash
kubectl describe pod <pod-name>
```

Check:
- restart reason
- events
- exit codes
- OOMKilled messages

---

### Step 2 — Check Logs

```bash
kubectl logs <pod-name>
kubectl logs <pod-name> --previous
```

`--previous` helps if the container already restarted.

---

### Step 3 — Check Resource Metrics

Using:
- Prometheus
- Grafana
- kubectl top pod

Check:
- CPU spikes
- memory spikes
- throttling
- OOM events

---

### Step 4 — Verify Health Probes

Check:
- livenessProbe
- readinessProbe

Misconfigured probes can restart healthy applications.

---

### Step 5 — Node-Level Checks

Check:
- node pressure
- kubelet logs
- disk space
- network instability

---

# 2. How would you monitor Kubernetes cluster health proactively?

## Answer

I would monitor both:
- infrastructure health
- application health

---

### Cluster-Level Monitoring

Monitor:
- node status
- CPU/memory usage
- disk pressure
- pod failures
- API server health

---

### Workload Monitoring

Monitor:
- pod restart count
- CrashLoopBackOff
- pending pods
- deployment failures

---

### Tools

Use:
- Prometheus
- Grafana
- Alertmanager

In AWS:
- CloudWatch Container Insights

---

### Important Alerts

Create alerts for:
- high CPU/memory
- node NotReady
- pod restart spikes
- disk usage
- failed deployments

---

### Logging

Centralize logs using:
- EFK stack
or
- Loki + Grafana

---

# 3. How would you centralize logs from multiple Kubernetes pods and environments?

## Answer

Since pods are ephemeral, logs should not remain only inside containers.

### Common Architecture

```text
Pods
  ↓
FluentBit / Fluentd
  ↓
Elasticsearch / Loki / CloudWatch
  ↓
Grafana / Kibana
```

---

### Log Collection

Use:
- FluentBit
or
- Fluentd

as DaemonSets to collect logs from all nodes.

---

### Log Storage

Options:
- Elasticsearch
- Loki
- CloudWatch Logs

---

### Visualization

Use:
- Kibana
or
- Grafana

for searching and dashboards.

---

### Best Practices

Include:
- namespace
- pod name
- container name
- environment
- timestamps

for easier troubleshooting.

---

# 4. What is the difference between metrics, logs, and traces?

## Answer

### Metrics

Metrics are numeric values collected over time.

Examples:
- CPU usage
- memory usage
- request count
- latency

Used for:
- dashboards
- alerting
- trend analysis

Tools:
- Prometheus
- CloudWatch

---

### Logs

Logs are detailed event records generated by applications or systems.

Examples:
- errors
- exceptions
- application events

Used for:
- debugging
- root cause analysis

Tools:
- ELK
- Loki
- CloudWatch Logs

---

### Traces

Traces track a request flow across multiple services.

Useful in:
- microservices architecture

Helps identify:
- slow service calls
- bottlenecks

Tools:
- Jaeger
- Zipkin
- AWS X-Ray

---

### Simple Example

If application is slow:

- Metrics show high latency
- Logs show application error
- Trace shows which microservice caused delay

---

# 5. How would you investigate sudden spikes in AWS infrastructure cost?

## Answer

First, I would identify:
- which service increased cost
- when spike started

---

### Step 1 — Use Cost Explorer

Check:
- service-wise cost
- account-wise usage
- daily trends

---

### Step 2 — Identify Resource Changes

Possible causes:
- new EC2 instances
- scaling events
- high data transfer
- unused resources
- large EBS volumes

---

### Step 3 — Check Monitoring Data

Use:
- CloudWatch
- Auto Scaling history

Verify:
- unexpected scaling
- traffic spikes
- high API usage

---

### Step 4 — Check Kubernetes/EKS

Possible issues:
- too many pods
- oversized nodes
- resource requests too high
- runaway workloads

---

### Step 5 — Review Storage & Networking

Check:
- NAT Gateway cost
- cross-AZ traffic
- EBS snapshots
- S3 lifecycle policies

---

### Step 6 — Optimization

Use:
- Compute Optimizer
- Savings Plans
- Spot Instances
- rightsizing

---

### Preventive Measures

Implement:
- AWS Budgets
- billing alerts
- tagging strategy
- cost dashboards


# 1. Terraform State File Corruption / Missing State

## Question

A Terraform-managed EC2 instance is running in AWS, but the `terraform.tfstate` file was accidentally deleted. What happens now, and how would you recover?

## Expected Answer

* Terraform no longer knows the infrastructure exists.
* Next `terraform plan` may try to recreate resources.
* Recovery options:

  * Restore state from backup/S3 backend versioning
  * Use `terraform import` to bring existing resources back into state
* If remote backend is used:

  * recover from S3 versioning
  * DynamoDB lock table remains unaffected

Example:

```bash id="ikbq59"
terraform import aws_instance.web i-1234567890abcdef
```

---

# 2. Terraform Drift Detection

## Question

A developer manually changed the EC2 instance type in AWS from `t2.micro` to `t3.medium`, but Terraform code still says `t2.micro`. What happens during `terraform plan`?

## Expected Answer

Terraform detects infrastructure drift.

`terraform plan` will show:

```text id="i6lxsz"
~ instance_type = "t3.medium" -> "t2.micro"
```

Terraform will try to bring infra back to desired state defined in code.

Key concepts:

* Drift detection
* Desired state management
* Refresh during plan/apply

---

# 3. Multi-Environment Deployment Using Terraform

## Question

Your company has:

* Dev in `us-east-1`
* Prod in `us-west-1`

How would you manage this in Terraform without duplicating code?

## Expected Answer

Possible approaches:

* Terraform modules
* Workspaces
* Separate variable files
* Provider aliases

Example:

```hcl id="ryb74z"
provider "aws" {
  alias  = "dev"
  region = "us-east-1"
}

provider "aws" {
  alias  = "prod"
  region = "us-west-1"
}
```

Use:

```hcl id="1o0ps0"
provider = aws.prod
```

inside resources/modules.

---

# 4. Terraform State Locking Scenario

## Question

Two engineers ran `terraform apply` simultaneously on the same infrastructure. What problem can occur, and how is it prevented?

## Expected Answer

Possible issues:

* State corruption
* Resource conflicts
* Inconsistent infrastructure

Terraform prevents this using state locking.

Common setup:

* S3 backend for state storage
* DynamoDB table for locking

Example:

```hcl id="u2w9tv"
backend "s3" {
  bucket         = "terraform-state"
  key            = "prod/terraform.tfstate"
  region         = "us-east-1"
  dynamodb_table = "terraform-lock"
}
```

---

# 5. Terraform Module Reusability

## Question

Your team is repeatedly creating:

* VPCs
* Subnets
* Security Groups

across multiple projects. How would you avoid code duplication?

## Expected Answer

Use Terraform modules.

Benefits:

* Reusability
* Standardization
* Easier maintenance
* Environment consistency

Structure:

```text id="5j6txy"
modules/
  vpc/
    main.tf
    variables.tf
    outputs.tf
```

Call module:

```hcl id="jlwmqs"
module "vpc" {
  source     = "./modules/vpc"
  cidr_block = "10.0.0.0/16"
}
```

---

# Strong Interview Topics Covered

These scenarios evaluate:

* State management
* Drift detection
* Remote backend
* Locking
* Modules
* Multi-region architecture
* Real production troubleshooting
* Infrastructure lifecycle understanding


