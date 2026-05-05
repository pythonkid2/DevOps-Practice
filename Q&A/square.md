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

