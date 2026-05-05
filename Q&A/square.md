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

---

### Step 6 — Check CNI Plugin

In EKS:
- aws-node
- CoreDNS
- kube-proxy

must be healthy.

---

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



