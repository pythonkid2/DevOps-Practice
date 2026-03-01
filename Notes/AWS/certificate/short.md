
---

## 🧭 AWS Solutions Architect – Quick Revision Notes (Short Notes)

| **Topic**                             | **What it is**                             | **Why it’s used**                              | **Exam Keywords / Triggers**                                                      | **Related / Compare With**               |
| ------------------------------------- | ------------------------------------------ | ---------------------------------------------- | --------------------------------------------------------------------------------- | ---------------------------------------- |
| **VPC (Virtual Private Cloud)**       | Logical isolation of AWS network           | To control networking (CIDR, routing, subnets) | “isolation”, “private/public subnets”, “CIDR overlap”, “NACL vs SG”               | Subnets, Route Tables, NACL, SG, Peering |
| **Subnet Types**                      | Public (IGW route), Private (NAT route)    | To separate traffic & control access           | “public-facing”, “NAT”, “IGW”, “private backend”                                  | NAT Gateway, IGW                         |
| **Route Table**                       | Routing logic for subnet traffic           | To direct traffic to destinations              | “destination CIDR”, “target”, “local route”, “blackhole”                          | VPC Peering, TGW, IGW                    |
| **NACL (Network ACL)**                | Stateless layer for subnet                 | Control inbound/outbound rules                 | “stateless”, “rule order”, “deny by default”                                      | Security Group                           |
| **Security Group**                    | Stateful firewall at ENI level             | Allow specific inbound/outbound                | “stateful”, “instance level”, “default deny inbound”                              | NACL                                     |
| **VPC Peering**                       | Connect 2 VPCs privately                   | Cross-VPC communication                        | “non-transitive”, “CIDR overlap issue”, “same/diff region”                        | TGW, VPN                                 |
| **Transit Gateway (TGW)**             | Central hub for VPCs, VPNs                 | Scalable multi-VPC routing                     | “hub-and-spoke”, “transitive routing”, “cross-account”                            | Peering, PrivateLink                     |
| **PrivateLink / VPC Endpoint**        | Access AWS services privately              | Avoid IGW/public internet                      | “Interface endpoint”, “Gateway endpoint”, “S3, DynamoDB”, “no route table change” | NAT Gateway, TGW                         |
| **NAT Gateway / NAT Instance**        | Outbound internet for private subnets      | Allow updates/downloads                        | “EIP”, “one-way traffic”, “no inbound”                                            | IGW, PrivateLink                         |
| **S3**                                | Object storage                             | Backup, static websites, data lake             | “Durability 11 9s”, “region-level”, “versioning”, “lifecycle”                     | EBS, EFS, Glacier                        |
| **S3 Storage Classes**                | Standard, IA, 1Z-IA, Glacier, Deep Archive | Cost optimization                              | “access frequency”, “retrieval time”, “min duration”                              | Lifecycle rules                          |
| **S3 Versioning**                     | Keep old versions                          | Data protection                                | “delete marker”, “MFA delete”                                                     | Lifecycle, Replication                   |
| **S3 Replication**                    | Cross-region or same region copy           | DR / Compliance                                | “CRR”, “SRR”, “versioning required”                                               | EventBridge, Lambda                      |
| **S3 Object Lock**                    | WORM (Write Once Read Many)                | Compliance (SOC, HIPAA)                        | “Governance mode”, “Compliance mode”, “Legal hold”                                | Glacier Vault Lock                       |
| **S3 Transfer Acceleration**          | Upload via edge locations                  | Faster uploads globally                        | “edge-optimized”, “CloudFront backbone”                                           | Direct Connect, DataSync                 |
| **AWS Snow Family**                   | Physical data transfer devices             | Offline large data migration                   | “Snowcone (TBs)”, “Snowball (100TBs)”, “Snowmobile (Exabytes)”                    | DataSync, Transfer Acceleration          |
| **AWS DataSync**                      | Online sync from on-prem to AWS            | Automated transfer                             | “NFS/SMB”, “over internet/VPN”, “schedule sync”                                   | Snowball, DMS                            |
| **CloudFront**                        | CDN for global caching                     | Reduce latency                                 | “edge locations”, “TTL”, “origin access control”, “signed URL”                    | Global Accelerator                       |
| **Global Accelerator**                | TCP/UDP accelerator using Anycast          | Improve global performance                     | “static IP”, “Anycast”, “health checks”, “multi-region”                           | CloudFront                               |
| **ELB (Elastic Load Balancer)**       | Distribute traffic                         | High availability                              | “ALB (Layer 7)”, “NLB (Layer 4)”, “CLB (legacy)”                                  | Route 53, ASG                            |
| **Auto Scaling Group (ASG)**          | Scale EC2s automatically                   | Elasticity, fault tolerance                    | “desired capacity”, “cooldown”, “lifecycle hooks”                                 | ECS, Lambda concurrency                  |
| **EC2 Launch Template**               | EC2 configuration template                 | Version control, automation                    | “mixed instances policy”, “spot + on-demand”                                      | ASG                                      |
| **EBS (Elastic Block Store)**         | Block-level storage for EC2                | Persistent disks                               | “gp3”, “io1/io2”, “snapshot”, “AZ-bound”                                          | EFS, S3                                  |
| **EFS (Elastic File System)**         | Shared file storage                        | Multi-AZ, scalable                             | “POSIX”, “mount targets”, “NFSv4”, “burstable throughput”                         | FSx, S3                                  |
| **FSx**                               | Managed file systems                       | SMB/NFS for Windows/Lustre                     | “Windows FSx”, “Lustre for HPC”                                                   | EFS                                      |
| **RDS (Relational DB Service)**       | Managed SQL DB                             | Multi-AZ failover                              | “backup retention”, “read replica”, “storage autoscaling”                         | Aurora, DynamoDB                         |
| **Aurora**                            | Cloud-native RDS                           | High perf, 6-way storage                       | “Cluster endpoint”, “Reader endpoint”, “serverless v2”                            | RDS MySQL/PostgreSQL                     |
| **DynamoDB**                          | NoSQL key-value DB                         | Low-latency at scale                           | “RCU/WCU”, “DAX”, “streams”, “TTL”, “on-demand vs provisioned”                    | Aurora, S3                               |
| **Elasticache**                       | In-memory cache                            | Speed up reads                                 | “Redis vs Memcached”, “cluster mode”                                              | DAX, CloudFront                          |
| **Lambda**                            | Serverless compute                         | Event-driven workloads                         | “event source”, “timeout”, “cold start”, “concurrency limit”                      | ECS Fargate                              |
| **ECS (Elastic Container Service)**   | Container orchestration                    | Run containers easily                          | “EC2 or Fargate”, “task definition”, “service autoscaling”                        | EKS, Lambda                              |
| **EKS (Elastic Kubernetes Service)**  | Managed Kubernetes                         | Port existing workloads                        | “control plane managed”, “IAM roles for SA”                                       | ECS                                      |
| **SNS (Simple Notification Service)** | Pub/Sub messaging                          | Event-driven alerts                            | “topic”, “subscription”, “fan-out”, “SQS integration”                             | SQS, EventBridge                         |
| **SQS (Simple Queue Service)**        | Message queue                              | Decouple components                            | “visibility timeout”, “DLQ”, “FIFO ordering”                                      | SNS, Kinesis                             |
| **EventBridge**                       | Event bus for AWS services                 | Rule-based routing                             | “schema registry”, “cross-account bus”                                            | SNS, Step Functions                      |
| **Step Functions**                    | Workflow orchestration                     | Coordinate microservices                       | “state machine”, “retry policy”, “wait”, “parallel”                               | SWF, Lambda                              |
| **CloudWatch**                        | Monitoring & logs                          | Observability                                  | “metrics”, “alarms”, “logs insight”, “dashboard”                                  | X-Ray, CloudTrail                        |
| **CloudTrail**                        | API call logging                           | Governance/audit                               | “who did what”, “event history”, “management vs data events”                      | Config                                   |
| **Config**                            | Resource compliance                        | Detect drift                                   | “rules”, “recorders”, “conformance packs”                                         | CloudTrail                               |
| **IAM**                               | Access control                             | Secure AWS resources                           | “least privilege”, “policy evaluation logic”, “STS”, “assume role”                | Organizations, SCP                       |
| **Organizations & SCP**               | Multi-account mgmt                         | Central governance                             | “SCPs”, “OU”, “consolidated billing”                                              | IAM                                      |
| **KMS**                               | Encryption key mgmt                        | Data security                                  | “CMK”, “AWS managed vs customer managed”, “envelope encryption”                   | S3 SSE, Secrets Manager                  |
| **Secrets Manager**                   | Manage secrets rotation                    | Secure app secrets                             | “rotation lambda”, “cross-account”                                                | SSM Parameter Store                      |
| **Parameter Store**                   | Config mgmt                                | App settings storage                           | “Standard/Advanced”, “no auto rotation”                                           | Secrets Manager                          |
| **CloudFormation**                    | IaC (Infrastructure as Code)               | Repeatable provisioning                        | “stack”, “change set”, “drift detection”                                          | Terraform, CDK                           |
| **Elastic Beanstalk**                 | PaaS for web apps                          | Simplified deployment                          | “environment”, “blue/green”, “managed scaling”                                    | ECS Fargate                              |
| **Direct Connect**                    | Dedicated line to AWS                      | Low latency, private                           | “virtual interface”, “hybrid setup”                                               | VPN                                      |
| **VPN (Site-to-Site)**                | Encrypted tunnel                           | Hybrid connectivity                            | “IPSec”, “VGW”, “customer gateway”                                                | DX, TGW                                  |
| **Storage Gateway**                   | Hybrid storage (File, Volume, Tape)        | Integrate on-prem to AWS                       | “cached vs stored”, “tape gateway”                                                | DataSync                                 |
| **WAF**                               | Web Application Firewall                   | Protect against L7 attacks                     | “OWASP”, “SQLi/XSS”, “rate-based rules”                                           | Shield, GuardDuty                        |
| **Shield (Standard / Advanced)**      | DDoS protection                            | Protect ALB/CloudFront                         | “DDoS mitigation”, “24x7 support”                                                 | WAF                                      |
| **GuardDuty**                         | Threat detection                           | ML-based alerts                                | “malicious IPs”, “findings”, “cross-account enable”                               | Inspector, Macie                         |
| **Inspector**                         | Vulnerability scanning                     | EC2/ECR/Lambda CVEs                            | “CVE scan”, “CIS benchmark”                                                       | GuardDuty                                |
| **Macie**                             | Sensitive data discovery                   | PII detection                                  | “S3 data classification”, “GDPR”                                                  | GuardDuty, KMS                           |

---



## Amazon Guard duty 

**GuardDuty = Continuous Threat Detection**

* Monitors **AWS accounts, workloads, S3 data**
* Uses **CloudTrail, VPC Flow Logs, DNS Logs**
* Adds **threat intel, anomaly detection, ML**
* Finds **malicious activity & risks** automatically

**G-CANDy** 🍬 (think of it as “GuardDuty gives you Candy = Security Sweetness”)

**G-CANDy stands for:**

* **G** – Guard your **Accounts, Workloads, S3**
* **C** – **CloudTrail** events
* **A** – **Anomaly detection** (ML-powered)
* **N** – **Network logs** (VPC Flow Logs)
* **D** – **DNS logs**
* **y** – Threat **intel (malicious IPs)**


### 🕵️ **Macie** → **M-CLASS** 🎓

Focus: **Data Security for S3** (PII, sensitive data)

**M-CLASS:**

* **M** – Macie
* **C** – **Classifies** data (detects PII)
* **L** – **Logs** & alerts for findings
* **A** – **Analyzes** S3 buckets
* **S** – **Sensitive data protection**
* **S** – **Security compliance** (GDPR, HIPAA)

---

### 🧪 **Inspector** → **I-CVSS** 🔍

Focus: **Automated vulnerability management**

**I-CVSS:**

* **I** – Inspector
* **C** – **Continuous scanning** of EC2, ECR, Lambda
* **V** – **Vulnerability assessment**
* **S** – **Security findings** with CVSS scores
* **S** – **Seamless integration** (auto remediation with Security Hub)



Here’s a **crisp, exam-friendly note for Amazon RDS Custom** (perfect for quick revision):

---

## 📌 **Amazon RDS Custom – Exam Notes**

### 1️⃣ **What (Definition)**

Amazon **RDS Custom** = Managed database service for applications that require **custom OS/DB configuration** that standard RDS does not allow.
Think of it as: **"RDS + Root Access"** (but still managed by AWS).

---

### 2️⃣ **Why (Use Cases)**

* **Legacy/Custom apps** needing special OS configs, agents, or database patches.
* **Vendor apps** (ERP, CRM) that require custom DB settings.
* Need **SSH access** to database host for troubleshooting or installing software.
* Need to control DB and OS patching schedule but still want automated backups, monitoring.

---

### 3️⃣ **How (Configuration)**

* Choose **RDS Custom for Oracle or SQL Server** (supported engines as of now).
* AWS provisions an EC2 instance under the hood with DB pre-installed.
* You get **SSH access** + **OS-level customization** ability.
* Can still use:

  * Automated backups
  * Monitoring (CloudWatch)
  * Read replicas (where supported)
* Responsibility split:

  * **AWS**: infrastructure, automated backups, storage, failover.
  * **You**: OS-level changes, DB patching, security hardening.

---

### 4️⃣ **Common Pitfalls / Limits**

* More expensive than normal RDS (since you manage more control).
* Misconfigurations can break automation (backups, monitoring) – you are responsible.
* No full hands-off like RDS Standard.
* Supported only for **Oracle & SQL Server** (as of exam).
* Root access means you must be careful with changes — AWS automation can pause if instance is misconfigured.

---

### 5️⃣ **Exam Tips / Keywords**

* **"Need OS-level or DB-level customization" → RDS Custom**
* **"Need SSH access to DB host" → RDS Custom**
* **"Legacy apps requiring special agents / patches" → RDS Custom**
* **"Fully managed, no customization" → RDS (Standard)**

Think of it as **"Managed EC2 DB"** vs. "Fully-managed RDS".

---

Here’s a **crisp, exam-friendly note** for **Migrating RDS MySQL → Aurora MySQL + Aurora Replicas + Auto Scaling** (perfect for quick revision):

---

## 📌 **Amazon Aurora Migration & Replica Notes (Exam Focus)**

### 1️⃣ **Migration: RDS MySQL → Aurora MySQL**

* **Use AWS DMS (Database Migration Service)** or **Snapshot Restore**:

  * Take snapshot of RDS MySQL → Restore snapshot as Aurora MySQL cluster.
  * Minimal downtime migration (DMS for near-zero downtime).
* After migration, **update application endpoints** to point to Aurora cluster writer endpoint.

---

### 2️⃣ **Aurora Architecture & Benefits**

* **Distributed, fault-tolerant storage** (decoupled from compute).
* **Auto-scales storage** up to **128 TiB** per database.
* Data replicated across **3 AZs** (6 copies total).
* **Continuous backup to S3**, point-in-time recovery.
* **Faster failover** (30 seconds or less typically).
* **Higher throughput** vs MySQL (up to 5x faster).

---

### 3️⃣ **Aurora Replicas vs MySQL Read Replicas**

| Feature          | MySQL Read Replica          | Aurora Replica               |
| ---------------- | --------------------------- | ---------------------------- |
| Replication Type | Asynchronous                | Synchronous (shared storage) |
| Replica Lag      | Seconds (sometimes minutes) | \~10s of milliseconds        |
| Max Replicas     | 5                           | 15                           |
| Failover         | Manual or semi-auto         | Automated failover possible  |
| Storage          | Separate copy               | Shared storage volume        |

✅ **Exam Keyword:** "Need <1 second replication lag / near real-time reads" → **Aurora Replicas**

---

### 4️⃣ **Aurora Auto Scaling**

* **Aurora Replicas** can scale up/down automatically based on:

  * **CPU utilization**
  * **Connections**
  * **Average replica lag**
* **Aurora Auto Scaling = Add/Remove replicas automatically**
* Helps handle sudden read workload spikes cost-effectively.

---

### 5️⃣ **Exam Tips / Keywords**

* **"Minimal replica lag"** → Aurora Replica (shared storage).
* **"Auto scale read replicas"** → Aurora Auto Scaling.
* **"Cross-AZ replication + continuous backup + 15 replicas"** → Aurora.
* **"Migrate MySQL to Aurora with minimal downtime"** → DMS or snapshot restore.

---

### 🧠 **Memory Hook (For Exam)**

**AURORA = A-U-R-O-R-A**

* **A**uto-scaling
* **U**ltra-fast replication (ms lag)
* **R**eplicas up to 15
* **O**ptimized storage (128 TiB, 3 AZs)
* **R**ecovery (PITR + S3 backup)
* **A**vailability (HA, self-healing)

---
<img width="1024" height="1536" alt="image" src="https://github.com/user-attachments/assets/31091f5f-2332-4c5a-aa29-c51bfbd6fd3e" />



Here’s a **crisp, exam-focused note for AWS DataSync** for quick revision:

---

## 📌 **AWS DataSync – Exam Notes**

### 1️⃣ **What (Definition)**

AWS **DataSync** = **Online data transfer service** for moving large amounts of data quickly **to, from, and between** AWS storage services.

* Fully managed
* 10x faster than open-source tools (rsync)
* Secure, automated, scalable

---

### 2️⃣ **Why (Use Cases)**

* **Migrate on-premises data → AWS** (S3, EFS, FSx)
* **Replicate data between AWS storage services** (S3 <-> EFS, FSx <-> FSx)
* **Disaster recovery**: Continuous sync between on-prem and AWS
* **Big data processing**: Quickly load datasets into AWS

---

### 3️⃣ **How (Configuration)**

* Deploy a **DataSync Agent** on-premises (VMware, Hyper-V, KVM).
* Define **Source Location** (on-prem NFS/SMB, AWS service).
* Define **Destination Location** (S3, EFS, FSx, etc.).
* Create **Tasks** → schedule for one-time or recurring transfers.
* Supports **encryption (TLS), data integrity checks, and IAM** for permissions.

---

### 4️⃣ **Common Pitfalls / Limits**

* **Agent required** for on-premises sources (not needed for cloud-to-cloud).
* Transfers only **file data** (not block storage snapshots).
* Pricing based on **data transferred (per GB)**.

---

### 5️⃣ **Exam Tips / Keywords**

* **"Fast, secure, automated online data transfer" → DataSync**
* **"10x faster than open-source" → DataSync**
* **"Agent for on-prem" → DataSync**
* **"Move data between S3, EFS, FSx" → DataSync**
* **"Recurring scheduled sync" → DataSync**

---

### 🧠 **Memory Hook**

**DATASYNC = "DATA SPEED SYNC"**

* **D** – Data transfer
* **A** – Automated
* **T** – Task-based
* **A** – Agent (on-prem)
* **S** – Secure (TLS)
* **Y** – Your storage (S3/EFS/FSx)
* **N** – Near real-time sync
* **C** – Cloud migration

---

VPC Gateway Endpoint for S3 = creates a private route from your VPC to S3 over the AWS network (no NAT required, no public IPs required, no extra data processing charges)

App Runner → “I just want my container to run, scale, and serve traffic — no cluster headaches.”
EKS → “I need full control, multiple microservices, custom networking, CI/CD integration, service mesh, and Kubernetes portability.”
+++++++++
Inbound endpoint = allows on-prem DNS servers to send queries into Route 53 Resolver (so VPC names can be resolved by on-prem resolvers by forwarding queries to the inbound endpoint).

Outbound endpoint = lets Route 53 Resolver forward queries out to your on-prem DNS servers (so resources in the VPC can resolve on-prem names by conditional forwarding through the outbound endpoint).
++

**CloudFormation StackSets** -extends the functionality of stacks by enabling you to create, update, or delete stacks across multiple accounts and regions with a single operation.

<img width="739" height="414" alt="image" src="https://github.com/user-attachments/assets/a91f1edf-bf47-4186-afc6-3e661a77a05f" />

**AWS CloudFormation template** - JSON or YAML-format, text-based file that describes all the AWS resources you need to deploy to run your application.

- blueprint for a stack

 **CloudFormation stacks** stack is a set of AWS resources that are created and managed as a single unit when AWS CloudFormation instantiates a template
    -  A stack cannot be used to deploy the same template across AWS accounts and regions

**AWS Resource Access Manager (AWS RAM)** AWS Resource Access Manager (AWS RAM) is a service that enables you to easily and securely share AWS resources with any AWS account or within your AWS Organization.


 **Amazon Machine Image (AMI)**

 provides the information required to launch an instance.

contains - One or more Amazon EBS snapshots, or, for instance-store-backed AMIs, a template for the root volume of the instance.

You can copy an AMI within or across AWS Regions using the AWS Management Console, the AWS Command Line Interface or SDKs, or the Amazon EC2 API, all of which support the CopyImage action. You can copy both Amazon EBS-backed AMIs and instance-store-backed AMIs. You can copy AMIs with encrypted snapshots and also change encryption status during the copy process.


<img width="1428" height="928" alt="image" src="https://github.com/user-attachments/assets/44ae91f4-1a23-4780-b5d1-7a343577ff2b" />

Think resource performance monitoring, events, and alerts; think **Amazon CloudWatch**.

Think account-specific activity and audit; think **AWS CloudTrail**.

Think resource-specific history, audit, and compliance; think **AWS Config**.

Global users + low-latency + UDP/TCP traffic = **AWS Global Accelerator**

Single-region + UDP/TCP traffic = **NLB**

HTTP/HTTPS traffic with Layer 7 features = **ALB**


**Amazon API Gateway HTTP APIs support native JWT authorizers**

Here’s a **crisp, exam-focused note** for **AWS Storage Gateway** that’s easy to remember:

---

# 📝 **AWS Storage Gateway – Exam Notes**

## ✅ **What It Is**

* **Hybrid storage service** → connects **on-premises apps** to **AWS cloud storage**
* Provides **low-latency local cache** + **virtually unlimited storage in S3**

---

## 🛠 **Types of Gateways (Key for Exam)**

| **Gateway Type**   | **Use Case**                                     | **Key Points**                                                                                                                                                                   |
| ------------------ | ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **File Gateway**   | Store & access **files** as objects in S3        | NFS/SMB access, integrates with S3 bucket                                                                                                                                        |
| **Volume Gateway** | Store **block storage volumes** in AWS           | Two modes: <br>🔹 **Cached Volumes:** Store primary data in S3, cache frequently accessed data locally <br>🔹 **Stored Volumes:** Store primary data locally, async backup to S3 |
| **Tape Gateway**   | Replace physical tape backups with virtual tapes | VTL interface, backups stored in S3/Glacier                                                                                                                                      |

---

## 🧠 **Exam Triggers**

* **Low-latency access + on-prem + cloud storage** → Storage Gateway
* **Backup tapes to cloud** → Tape Gateway
* **Extend local file server to S3** → File Gateway
* **Block storage replication to S3** → Volume Gateway (Cached/Stored)

---

## 📌 **Memory Hook**

**FVT → File, Volume, Tape**

* **F = Files to S3**
* **V = Volumes (Cached/Stored)**
* **T = Tape backup to S3/Glacier**

---


<img width="1116" height="663" alt="image" src="https://github.com/user-attachments/assets/ae5707cb-5b9f-49f4-9c70-05094ef0437e" />


<img width="1798" height="346" alt="image" src="https://github.com/user-attachments/assets/4b69a1ed-57c0-45bb-8b4f-432ea1f48322" />

<img width="1191" height="631" alt="image" src="https://github.com/user-attachments/assets/a87f7b23-de58-4296-bfdc-6d2b217fa60b" />

Got it ✅ — you want a **clear, exam-friendly breakdown** of **when to use which Amazon S3 storage class** — with short, memorable tips.

Here’s the full guide:

---

# 📌 **Amazon S3 Storage Classes – Exam Cheat Sheet**

<img width="1399" height="572" alt="image" src="https://github.com/user-attachments/assets/259bc99c-a4e0-4fbe-a7f0-1eb7d15884c4" />



| **S3 Class**                                         | **When to Use (Ideal Scenario)**                                                                    | **Key Points / Keywords**                                                               |
| ---------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| **S3 Standard**                                      | 🔹 Frequently accessed data 🔹 Mission-critical workloads 🔹 Dynamic websites, content distribution | 🌟 **High durability (11 9s)**, low latency, multi-AZ, default choice                   |
| **S3 Standard-IA** (Infrequent Access)               | 🔹 Data accessed **< once per month** 🔹 Long-term backups, DR 🔹 Not mission critical              | ✅ Cheaper storage, **retrieval fee applies**, multi-AZ durability                       |
| **S3 One Zone-IA**                                   | 🔹 Data you can easily **recreate** 🔹 Secondary backups 🔹 Logs, temp data                         | 💰 \~20% cheaper than Standard-IA, **single AZ** (lower availability)                   |
| **S3 Intelligent-Tiering**                           | 🔹 **Unknown / unpredictable access patterns** 🔹 AI/ML datasets 🔹 Data lakes                      | 🤖 Auto-moves data between tiers (Frequent, Infrequent, Archive), no performance impact |
| **S3 Glacier Instant Retrieval**                     | 🔹 Archival data that must be accessed **within ms** 🔹 Medical images, media assets                | 💸 Cheaper than IA, instant retrieval                                                   |
| **S3 Glacier Flexible Retrieval** (formerly Glacier) | 🔹 Data rarely accessed 🔹 Backup/Archive 🔹 Retrieval within minutes–hours                         | 🕒 Bulk, Standard, Expedited retrieval options                                          |
| **S3 Glacier Deep Archive**                          | 🔹 Long-term archive 🔹 Regulatory compliance 🔹 Retain for 7-10+ years                             | 🕒 Lowest cost storage, retrieval in **hours**                                          |
| **S3 Reduced Redundancy (Deprecated)**               | ❌ Do **not** use unless for very specific legacy cases                                              | AWS recommends Standard instead                                                         |

---
<img width="2294" height="1108" alt="image" src="https://github.com/user-attachments/assets/fda6cd02-3b3c-4df3-840a-eebfab5386ec" />


## 🧠 **Exam Tips & Keywords**

* **"Frequently accessed, low latency" → S3 Standard**
* **"Infrequent but important, multi-AZ" → S3 Standard-IA**
* **"Infrequent, can be lost or recreated, cost-sensitive" → S3 One Zone-IA**
* **"Unknown access pattern, want automation" → S3 Intelligent-Tiering**
* **"Archival but quick restore needed" → Glacier Instant Retrieval**
* **"Archival, can wait minutes/hours" → Glacier Flexible Retrieval**
* **"Cheapest, long-term compliance storage" → Glacier Deep Archive**

---

## 📝 **Memory Hook**

🔑 **Hot → Warm → Cold → Frozen**
(Standard → IA → Glacier → Deep Archive)

Or use this mnemonic:
**"Some Important Objects Only Go Deep"**
(Standard, Intelligent-Tiering, One-Zone IA, Glacier, Deep Archive)

---


<img width="2538" height="1528" alt="image" src="https://github.com/user-attachments/assets/c7d7c8f5-514c-4fc0-8d7b-c0a1fde48dd9" />

You can't directly copy data from AWS Snowball Edge devices into Amazon S3 Glacier.

<img width="1058" height="413" alt="image" src="https://github.com/user-attachments/assets/3659ce58-d8f8-4bbf-8eea-2f2e7eea2023" />

<img width="2132" height="1200" alt="image" src="https://github.com/user-attachments/assets/92494fd6-5a8f-4c6c-bf05-5ca71d5a9adc" />

Perfect ✅ — this is another exam favorite. Let’s break down **Amazon EBS (Elastic Block Store) volume types**, their use cases, and when to choose each one.

---

# 📌 **Amazon EBS Volume Types – Exam Cheat Sheet**

EBS volumes are **block storage** for EC2 — persistent, resizable, and AZ-specific.

---

## 1️⃣ **General Purpose SSD (gp2 / gp3)**

* **gp2** – legacy, performance scales with size
* **gp3** – latest generation, performance configurable independent of size
* **Performance:**

  * gp3 baseline: **3,000 IOPS + 125 MB/s throughput** (configurable up to 16,000 IOPS & 1,000 MB/s)
  * gp2: 3 IOPS per GB (max 16,000 IOPS)
* **Use When:**

  * ✅ Boot volumes
  * ✅ Small to medium DBs
  * ✅ Dev/Test environments
  * ✅ General-purpose workloads

**Exam Keyword:** "Most workloads" → **gp3 (preferred)**

---

## 2️⃣ **Provisioned IOPS SSD (io1 / io2)**

* **Performance:**

  * io1/io2: Up to **64,000 IOPS** per volume
  * io2: Higher durability (99.999%)
* **Supports Multi-Attach** (attach to multiple EC2 instances at once, same AZ)
* **Use When:**

  * ✅ Mission-critical databases (Oracle, SQL, SAP HANA, etc.)
  * ✅ High-transaction, low-latency workloads
  * ✅ Need predictable performance regardless of size

**Exam Keyword:** "High-performance DB" → **io2**
**Exam Keyword:** "Multi-Attach required" → **io1/io2 only**

---

## 3️⃣ **Throughput Optimized HDD (st1)**

* **Performance:**

  * Throughput-based (not IOPS)
  * Max throughput: \~500 MB/s
* **Use When:**

  * ✅ Big data analytics
  * ✅ Streaming workloads
  * ✅ Log processing
  * ✅ Large sequential workloads

**Exam Keyword:** "Big data, large sequential I/O" → **st1**

---

## 4️⃣ **Cold HDD (sc1)**

* **Performance:**

  * Lowest cost
  * Max throughput: \~250 MB/s
* **Use When:**

  * ✅ Infrequently accessed data
  * ✅ Lowest-cost storage needed
  * ✅ Archive data you still want online

**Exam Keyword:** "Lowest cost magnetic, rarely accessed" → **sc1**

---

## 🧠 **Memory Hook**

Think of **EBS Volumes as Ladders of Performance vs Cost:**

🔼 **Cost ↑, Performance ↑**
`sc1 (cold) → st1 (throughput) → gp3 (general) → io2 (high IOPS)`

---

## ⚠️ **Common Pitfalls / Exam Gotchas**

* ❌ **gp2 performance scales with size** → gp3 allows you to decouple size and performance.
* ❌ HDD volumes (st1, sc1) **cannot be boot volumes**.
* ❌ Multi-Attach is **only supported for io1/io2**, not gp3.
* ❌ Choose io2 for **business-critical DBs** (better durability than io1).

---

Here’s a **clear, exam-ready comparison table** for all EBS volume types ✅

---

# 📌 **Amazon EBS Volume Types – Comparison Table**

| **Type**                             | **IOPS (Max)**                       | **Throughput (Max)** | **Cost**           | **Boot Volume?** | **Best Use Case**                                            | **Exam Keyword**                    |
| ------------------------------------ | ------------------------------------ | -------------------- | ------------------ | ---------------- | ------------------------------------------------------------ | ----------------------------------- |
| **gp3 (General Purpose SSD)**        | 16,000                               | 1,000 MB/s           | 💲💲 (balanced)    | ✅ Yes            | General workloads, boot volumes, dev/test, small DBs         | "Default choice", "General-purpose" |
| **gp2 (Legacy)**                     | 16,000 (scales with size: 3 IOPS/GB) | 250 MB/s             | 💲💲               | ✅ Yes            | Same as gp3 (but gp3 preferred now)                          | "Older generation"                  |
| **io1 / io2 (Provisioned IOPS SSD)** | 64,000 (single volume)               | 1,000 MB/s           | 💲💲💲💲 (highest) | ✅ Yes            | Mission-critical DBs, OLTP apps, latency-sensitive workloads | "High IOPS", "Multi-Attach"         |
| **st1 (Throughput Optimized HDD)**   | \~500 IOPS (burst)                   | 500 MB/s             | 💲 (low)           | ❌ No             | Big data, streaming, logs, large sequential I/O              | "Big data analytics", "Streaming"   |
| **sc1 (Cold HDD)**                   | \~250 IOPS (burst)                   | 250 MB/s             | 💲 (lowest)        | ❌ No             | Archival, rarely accessed data, lowest cost storage          | "Lowest cost magnetic storage"      |

---

## 🧠 **Memory Hook**

* **gp3 = Go-to volume (Default)**
* **io2 = IOPS King (Databases)**
* **st1 = Streaming / Sequential**
* **sc1 = Cold Storage**

---

## 📝 **Exam Quick Hits**

* ❌ **HDD volumes (st1, sc1) cannot be boot volumes.**
* ✅ **io1/io2 only** support Multi-Attach.
* ✅ Use **gp3** unless you have a clear need for higher IOPS/throughput or lower cost for sequential data.
* ✅ Choose **io2** for **critical DBs** because of its higher durability (99.999%).

---



<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/ddfc88f9-4b3a-471b-bc89-7721d73250e2" />

<img width="2658" height="1948" alt="image" src="https://github.com/user-attachments/assets/6265c1f5-8d02-4f69-8d3e-60fc601142a6" />

**AWS EBS Volume Types**

<img width="1972" height="1194" alt="image" src="https://github.com/user-attachments/assets/5ccaca49-0042-4f00-b069-d6e19004789c" />


Ah, good catch! 💡
Let’s add **“When to Use”** so you know which scenario fits which routing policy — this is VERY common in exams.

---

# 📑 **Route 53 Routing Policies – When to Use**

| **Policy**          | **When to Use (Scenario)**                                                                                           | **Key Notes / Exam Keywords**                            |
| ------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Failover** 🛑     | When you need **Active-Passive High Availability**. Route to secondary only if primary fails.                        | 📌 *Primary-Secondary*, Health Check required, **DR/HA** |
| **Simple** 🔑       | When you have **a single resource** (no special routing) or just want to return multiple values randomly.            | 📌 *Default*, No health check by default                 |
| **Weighted** ⚖️     | When you want to **split traffic by percentage** — A/B testing, gradual migration, canary deployment.                | 📌 *Traffic Split, Controlled Migration*                 |
| **Latency-based** ⚡ | When you want users to connect to **lowest latency endpoint** (multi-region setups).                                 | 📌 *Low Latency, Geo-Spread Workload*                    |
| **Geolocation** 🌍  | When you want to route based on **user’s country/continent** for compliance, language, or pricing reasons.           | 📌 *Country-Based Routing*                               |
| **Geoproximity** 📍 | When you want to route based on **geographic location AND bias traffic toward a specific region** (shift % traffic). | 📌 *Traffic Bias, Gradual Shift*                         |
| **Multi-Value** ✅   | When you want **DNS-based load balancing** — return multiple healthy records (simple + health checks).               | 📌 *DNS Load Balancing, Health Check*                    |

---

# 🎯 **Failover – When to Use**

* ✅ **Critical application** where downtime is not acceptable
* ✅ You have a **primary active site** and a **backup DR site** (warm/cold standby)
* ✅ You want **automatic switch** to backup on health check failure

---

# 📝 **Exam Quick Tip**

> ❗ **Remember:**
>
> * *Failover → Active/Passive HA*
> * *Weighted → % Traffic Split (Testing)*
> * *Latency → Performance*
> * *Geo/Geoproximity → Location-based control*
> * *Multi-Value → DNS-level LB + Health Check*

---

Great question! 👌
If you need to connect **on-premises network ↔ AWS**, Site-to-Site VPN is just **one option**.
Here’s a **complete list of connectivity options** with **when to use which** — very important for exam questions.

---

# 🌐 **AWS On-Prem to VPC Connectivity Options**

| **Option**                           | **What It Is**                                                              | **When to Use (Best Fit)**                                                                                   | **Pros**                                           | **Cons**                                                               |
| ------------------------------------ | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | -------------------------------------------------- | ---------------------------------------------------------------------- |
| **Site-to-Site VPN** 🔑              | IPSec VPN over the internet (VGW + CGW).                                    | Quick, low-cost, encrypted connection between on-prem and AWS. Good for small/medium workloads, testing, DR. | Fast to deploy, 2 tunnels for HA, managed by AWS.  | Internet-dependent (latency + jitter), bandwidth not guaranteed.       |
| **AWS Direct Connect (DX)** ⚡        | Dedicated physical fiber connection to AWS (1 Gbps / 10 Gbps link).         | High-throughput, low-latency workloads (e.g. financial apps, large data transfer).                           | Consistent network, private, reliable, SLAs.       | Setup time (weeks), higher cost.                                       |
| **Direct Connect + VPN (Hybrid)** 🔀 | DX for primary traffic + VPN as backup (failover).                          | Mission-critical workloads needing redundancy + compliance.                                                  | Combines reliability of DX with HA of VPN.         | Higher cost + more configuration.                                      |
| **Transit Gateway + VPN/DX** 🛜      | Hub-and-spoke network connecting multiple VPCs + on-prem sites.             | Large-scale multi-VPC + hybrid cloud architecture.                                                           | Centralized routing, scales to thousands of VPCs.  | More expensive than a single VGW.                                      |
| **VPC Peering** 🔗                   | Private connection between two VPCs (same/different accounts/regions).      | Connect VPCs when only a few are needed, no transitive routing needed.                                       | Simple, no bandwidth bottleneck, no VPN.           | No transitive routing (must peer each pair), no central mgmt.          |
| **AWS PrivateLink** 🔒               | Private connectivity to AWS services or third-party SaaS over AWS backbone. | Secure access to services without exposing them to the internet.                                             | No public IP, highly secure.                       | Only works for NLBs / interface endpoints (not full VPC connectivity). |
| **Client VPN** 👤                    | OpenVPN-based solution for individual users (not whole site).               | Secure access for remote workforce (laptops, WFH).                                                           | Managed, scales automatically, no hardware needed. | Not for site-to-site; per-user cost model.                             |

---

<img width="2182" height="1720" alt="image" src="https://github.com/user-attachments/assets/1d9aec35-2dd5-4941-88aa-d28ee520ae78" />


# 🎯 **When to Choose What (Exam Perspective)**

* ✅ **Low-cost, quick setup → Site-to-Site VPN**
* ✅ **Guaranteed bandwidth, low latency → Direct Connect**
* ✅ **Mission-critical HA → Direct Connect + VPN failover**
* ✅ **Multi-VPC hybrid architecture → Transit Gateway + VPN/DX**
* ✅ **Just connecting 2 VPCs → VPC Peering**
* ✅ **Access to specific service privately → PrivateLink**
* ✅ **Remote developers → Client VPN**

---

📌 **Exam Keyword Associations**

* **VPN → IPSec, quick setup, internet-based**
* **DX → Consistent, high bandwidth**
* **DX + VPN → Redundancy**
* **Transit Gateway → Scales, hub-and-spoke**
* **Peering → Simple 1:1 VPC connectivity**
* **PrivateLink → Interface endpoint, no peering**
* **Client VPN → Remote user access**

---
---

# 🧾 **AWS Site-to-Site VPN – Exam Notes**

## 1️⃣ **What**

AWS **Site-to-Site VPN** creates a **secure, encrypted IPsec tunnel** between your **on-premises network** (or another cloud) and your **Amazon VPC**.
It allows your on-prem servers to communicate privately with AWS resources as if they were in the same network.

---

## 2️⃣ **Why (Use Cases)**

✅ Extend your data center or office network securely into AWS
✅ Hybrid cloud architecture (on-prem + VPC)
✅ Backup/DR connectivity (with or without Direct Connect)
✅ Low-cost, quick setup compared to Direct Connect
✅ Temporary secure connection for migration

---

## 3️⃣ **How (Setup)**

1. **Create a Virtual Private Gateway (VGW)**

   * Attach it to your VPC (acts as AWS end of VPN).
2. **Create a Customer Gateway (CGW)**

   * Represents your on-prem router / firewall (public IP + ASN if BGP).
3. **Create the Site-to-Site VPN connection**

   * Select VGW + CGW, enable **static routing** or **BGP (dynamic routing)**.
4. **Download configuration**

   * Apply to your on-prem router/firewall (supports most vendors: Cisco, Juniper, Fortinet).
5. **Test connectivity**

   * Optionally create a **VPN CloudWatch alarm** for tunnel status.

---

## 4️⃣ **Common Pitfalls / Limits**

⚠️ **Single VGW limit** per VPC (use Transit Gateway for many VPNs).
⚠️ **2 VPN tunnels per connection** (for redundancy, always configure both).
⚠️ Bandwidth limited by internet and VPN encryption overhead (\~1.25 Gbps per tunnel, not guaranteed).
⚠️ Latency depends on public internet — not suitable for low-latency workloads.
⚠️ Customer router must support IPsec & IKEv1/IKEv2.

---

## 5️⃣ **Exam Tips / Keywords**

📌 **VGW** = AWS side endpoint
📌 **CGW** = On-prem side endpoint
📌 **BGP** = Recommended (dynamic routes, failover handled automatically)
📌 **2 tunnels** = HA by default
📌 **Transit Gateway + VPN** = Scale to many VPCs
📌 Often paired with **Direct Connect** for hybrid cloud redundancy (DX + VPN → **AWS Direct Connect + VPN failover** pattern)

---
<img width="1506" height="1270" alt="image" src="https://github.com/user-attachments/assets/d69d5d3c-4ba9-4904-baa0-f29b76ba69db" />

<img width="1200" height="661" alt="image" src="https://github.com/user-attachments/assets/c6756b91-a3be-43ff-a2d6-683fc2997ade" />

<img width="1087" height="411" alt="image" src="https://github.com/user-attachments/assets/58683d09-a6f0-4cbe-9b31-53ded81e6abd" />

---

# 📦 **Amazon S3 Storage Classes – Minimum Retention Periods**

Not all S3 classes have a minimum retention/charge duration. Here’s the breakdown:

---

### ✅ **No Minimum Retention Period**

* **S3 Standard**
* **S3 Intelligent-Tiering (frequent access tier)**
* **S3 Glacier Instant Retrieval**
  👉 You pay only for what you use, no penalties for deleting objects early.

---

### ⏱️ **Minimum Retention / Charge Period Applies**

* **S3 Standard-IA (Infrequent Access)** → **30 days**
* **S3 One Zone-IA** → **30 days**
* **S3 Intelligent-Tiering (infrequent + archive tiers)** → **30 days**
* **S3 Glacier Flexible Retrieval** → **90 days**
* **S3 Glacier Deep Archive** → **180 days**

---

### 📌 **Exam Tip**

* If you see **"delete object before X days → still charged"**, that’s **IA or Glacier classes**.
* **S3 Standard has *no* minimum retention period.**

---

✅ So, to your question:
**No, S3 Standard does not have a minimum retention period.**

---
Perfect 👍 here’s your **exam-focused S3 Storage Classes Cheat Sheet** – with **retention, retrieval, and when to use what**.

---

# 📦 **Amazon S3 Storage Classes – Exam Summary**

| **Storage Class**                                       | **Min Retention / Charge** | **Retrieval Time**                                  | **Use Case**                                  | **Exam Keywords**                                 |
| ------------------------------------------------------- | -------------------------- | --------------------------------------------------- | --------------------------------------------- | ------------------------------------------------- |
| **S3 Standard**                                         | ❌ None                     | Immediate                                           | Hot data, frequently accessed                 | “Mission-critical, low latency”                   |
| **S3 Intelligent-Tiering (Frequent)**                   | ❌ None                     | Immediate                                           | Data with unknown/variable access             | “Unknown access patterns”                         |
| **S3 Intelligent-Tiering (Infrequent + Archive Tiers)** | ✅ 30 days                  | Immediate (IA), minutes to hours (Archive)          | Optimized cost + auto tiering                 | “Automatic cost savings, unpredictable workloads” |
| **S3 Standard-IA**                                      | ✅ 30 days                  | Immediate                                           | Long-lived, infrequently accessed, resilient  | “Lower cost, but resilient across AZs”            |
| **S3 One Zone-IA**                                      | ✅ 30 days                  | Immediate                                           | Infrequent access, re-creatable, non-critical | “Single AZ, 20% cheaper than Standard-IA”         |
| **S3 Glacier Instant Retrieval**                        | ❌ None                     | Milliseconds                                        | Rarely accessed, needs ms retrieval           | “Archive but instant access”                      |
| **S3 Glacier Flexible Retrieval**                       | ✅ 90 days                  | Expedited: 1–5 min; Standard: 3–5 hr; Bulk: 5–12 hr | Archive, occasionally accessed                | “Formerly Glacier, cheap, flexible retrieval”     |
| **S3 Glacier Deep Archive**                             | ✅ 180 days                 | Standard: 12 hr; Bulk: 48 hr                        | Regulatory/long-term archival (7–10 years)    | “Cheapest storage, compliance, long-term backup”  |

---

# 📝 **Exam Shortcuts**

* **No min retention** → Standard, Intelligent-Tiering (frequent), Glacier Instant.
* **30-day min** → Standard-IA, One Zone-IA, Intelligent-Tiering (IA tiers).
* **90-day min** → Glacier Flexible Retrieval.
* **180-day min** → Glacier Deep Archive.
* **Single AZ storage** → One Zone-IA (NOT Standard).
* **Lowest latency archive** → Glacier Instant Retrieval.
* **Cheapest archival** → Glacier Deep Archive.

---

✅ This is the **exact pattern AWS exam questions use**:

* “Object deleted after 10 days but still charged” → IA (30 days).
* “Cheapest, long-term compliance storage” → Deep Archive (180 days).
* “Archive but need milliseconds retrieval” → Glacier Instant Retrieval.

---


<img width="1870" height="1266" alt="image" src="https://github.com/user-attachments/assets/4c5e2dac-9855-47b2-93e0-200e7df752f3" />
 - There are no S3 data transfer charges when data is transferred in from the internet. Also with S3TA, you pay only for transfers that are accelerated.

Great question 👌 This one trips up many people in **AWS Solution Architect exams**. Let’s carefully break it down.

---

## **The Scenario**

* You have an **AWS VPC** (with your web portal).
* You have **on-premises legacy systems** connected via **Site-to-Site VPN**.
* You want **apps inside the VPC** to resolve **private DNS names** hosted **on-premises**.
* You are using **Amazon Route 53 as DNS**.

---

## **How DNS Normally Works**

* In AWS, **EC2 instances in a VPC** by default use the **AmazonProvidedDNS** resolver (inside VPC).
* But that resolver **only knows about AWS-hosted domains** (public + Route 53 Private Hosted Zones).
* It **cannot resolve on-premises DNS records** (like `db.legacy.local`).

So we need a way to forward DNS queries from AWS → On-premises DNS servers.

---

## **Route 53 Resolver**

Think of it as a **DNS bridge** between AWS and on-prem DNS.
It has two types of endpoints:

1. **Outbound Endpoint**

   * Allows **DNS queries from VPC → On-prem DNS servers**.
   * You set **forwarding rules**:

     * Example: “If domain ends with `.corp.local`, send query to on-prem DNS server (IP 10.0.0.5)”.
   * This is what we need in your case.

2. **Inbound Endpoint**

   * Allows **on-premises servers → Resolve AWS private DNS zones**.
   * Used if your on-prem clients need to resolve AWS-hosted records.

---

## **Correct Answer Explanation**

> **Create a Route 53 Resolver outbound endpoint. Define a forwarding rule that routes DNS queries for on-premises domains to the on-premises DNS server. Associate the rule with the VPC.**

* Outbound endpoint = lets AWS VPC send queries **out** to on-prem.
* Forwarding rule = tells AWS resolver *which domains* should go to on-prem DNS.
* Association = attach the rule to your VPC so EC2s in that VPC benefit.

So when your AWS app queries `db.legacy.local`:

1. EC2 asks the VPC DNS.
2. Rule matches → forwards to outbound endpoint → sends to on-prem DNS via VPN.
3. On-prem DNS replies → back through the VPN → outbound endpoint → to your EC2.

✅ Secure (because it goes through VPN).
✅ Correct way to integrate AWS + on-prem DNS.

---

## **Why Other Options Are Wrong**

* **Inbound endpoint**: used when *on-prem* needs to resolve AWS, not the other way around.
* **Hybrid connectivity gateway**: not an AWS service for DNS.
* **Private hosted zone**: would require duplicating your on-prem DNS records in AWS → not scalable and not authoritative.

---

📌 **Exam Tip**:

* If **VPC → On-prem DNS** → **Outbound Endpoint**.
* If **On-prem → VPC DNS** → **Inbound Endpoint**.

---

<img width="1366" height="930" alt="image" src="https://github.com/user-attachments/assets/03fd545a-4c59-4f41-8f72-d6826080bfaa" />


Differences between Dedicated Hosts and Dedicated Instances: 



<img width="2182" height="1748" alt="image" src="https://github.com/user-attachments/assets/0a91f1db-da46-4601-88e7-f969ed47c4f3" />


Short answer: **No—DataSync isn’t only for NFS→EFS.** It’s the **managed way to move/sync files at scale** between on-prem and AWS, and also **within AWS**.

# DataSync — 60-sec Cheat Sheet

**What it moves (sources/dests):**

* **On-prem:** NFS, **SMB**, **HDFS**, S3-compatible object storage
* **AWS:** **S3**, **EFS**, **FSx** (Windows/SMB, Lustre, OpenZFS, NetApp ONTAP)

**Where it runs / network:**

* Agent runs on-prem VM/host (or EC2); transfers **over Internet, VPN, or Direct Connect**; can use **VPC endpoints/PrivateLink** to keep traffic private.

**Top use cases (beyond NFS→EFS):**

* **NFS/SMB → S3** (backups, analytics landing zone)
* **S3 ↔ FSx for Lustre** (HPC pipelines)
* **SMB ↔ FSx for Windows** (lift-and-shift Windows shares)
* **EFS ↔ EFS** (inter-Region/project migrations)
* **S3 ↔ S3** (cross-account/Region bulk copy with verification)
* **HDFS → S3** (off Hadoop → data lake)

**Why choose it (exam keywords):**

* **Managed, parallel, incremental**, **verification (checksum)**
* **Schedules**, include/exclude filters, **bandwidth throttle**
* Preserves file **metadata/permissions** (POSIX/SMB)
* **CloudWatch metrics** + **task reports**; retries & resumable

**When NOT to pick DataSync (pick these instead):**

* **Databases** → **AWS DMS**
* **Continuous low-latency hybrid access** → **Storage Gateway (File/Volume/Tape)**
* **End-user SFTP/FTPS/FTP** → **AWS Transfer Family**
* **S3→S3 ongoing object replication** → **S3 Replication**
* **Streaming events/logs** → **Kinesis / MSK**
* **Huge offline bulk (no network)** → **Snowball/Snowmobile**

**Memory hook:** **“M3V-S”** → **M**igrate **M**illions of files, **M**anaged, **V**erified, **V**PC-private, **S**cheduled.

<img width="2046" height="1480" alt="image" src="https://github.com/user-attachments/assets/bdc09d11-776d-4a41-bd70-b192a0973c36" />


<img width="800" height="658" alt="image" src="https://github.com/user-attachments/assets/920d676d-db31-4d70-b4f0-17d63affd220" />

<img width="2058" height="1462" alt="image" src="https://github.com/user-attachments/assets/d6655f66-e35a-4fa5-88aa-b953836aa826" />
Control tower
<img width="2370" height="1316" alt="image" src="https://github.com/user-attachments/assets/0630eb55-ad6d-4b4a-91b4-c75d2ecc6f26" />




Create and use a custom endpoint that targets the three high-capacity replicas: This is correct because Aurora custom endpoints allow you to define a subset of replicas for specific workloads. By creating a custom endpoint, the reporting queries can be automatically distributed across the three high-capacity replicas without involving the rest of the cluster.


Here are the main **serverless** choices on AWS for web apps, with a clear comparison and “when to use what.”

# Quick comparison

| Service                                      | What it is                                                                                                   | Deploy from                                            | Scaling & cold start                                                                             | Pricing model (high-level)                                                     | Best for                                                                                             | Not ideal when                                                                      |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| **AWS App Runner**                           | Fully managed **containers** for HTTP apps (no servers, no cluster)                                          | Source (Git) or container image (ECR/Docker Hub)       | Auto-scales by requests; optional **min instances** to avoid cold starts                         | vCPU/GB-RAM **per active instance-second** + requests + optional build minutes | Containerized web apps/APIs where you want “push and go” simplicity                                  | Non-HTTP protocols, complex daemon/background workers, or lots of custom networking |
| **AWS Lambda + Amazon API Gateway (or ALB)** | Event-driven **functions** behind a managed HTTP endpoint                                                    | Zip/container image; infra as code is common (SAM/CDK) | Scales to **zero** and up fast; **cold starts** possible (mitigate with provisioned concurrency) | **Per request + GB-seconds** compute                                           | Spiky/low traffic APIs, microservices, webhooks, backend jobs ≤15 min                                | Long-lived connections, heavy CPU/memory, workflows >15 min, large binaries         |
| **Amazon ECS on Fargate**                    | Serverless **container** runtime (no EC2). You still define tasks/services, LB, etc.                         | Container image (ECR)                                  | Scale by task count; startup in minutes; no “cold start,” but you pay while tasks run            | vCPU/GB-RAM **per running task-second** + LB/data transfer                     | More control: sidecars, custom networking, private subnets, non-HTTP protocols, queue workers        | If you want maximum simplicity and don’t want to think about tasks/services/LB      |
| **AWS Amplify Hosting**                      | Git-connected hosting with CI/CD for **front-ends** (SPA/SSR/ISR). Integrates with Amplify backend           | Repo (GitHub/GitLab/CodeCommit)                        | Global at edge (CloudFront); static has no cold start; SSR runs on demand                        | Build minutes + storage + data transfer + SSR/ISR invocations                  | Front-end teams shipping React/Next/Vue sites quickly; “full-stack” when paired with Amplify backend | Generic containerized backends or custom protocols                                  |
| **Amazon S3 + CloudFront**                   | Static site hosting at the edge (HTML/CSS/JS); optional **Lambda@Edge/CloudFront Functions** for light logic | Static assets build                                    | Instantly scalable; no cold start for static                                                     | S3 storage + CloudFront requests/transfer                                      | Pure static sites & SPAs (API lives elsewhere), marketing docs, docs portals                         | Server-side rendering, dynamic server logic (beyond light edge transforms)          |
| **AWS AppSync (GraphQL)**                    | Managed **GraphQL** API (subscriptions, caching); integrates with Lambda/DynamoDB                            | Schema-first; resolvers to data sources                | Scales automatically                                                                             | Requests + features (caching, real-time)                                       | GraphQL backends, real-time apps, mobile/web clients needing efficient data fetch                    | Traditional REST or containerized web servers                                       |

> Note: **Elastic Beanstalk** and **Lightsail** are *not* serverless—helpful abstractions, but you still pay for provisioned instances. You asked for serverless, so I’ve left them out of the main picks.

---

# When to use what (practical guide)

* **“I have a containerized web API and want zero infra management.”**
  → **AWS App Runner.** Easiest route for HTTP apps in a container, autoscaling + simple pricing.

* **“My traffic is spiky/low and my endpoints are short-lived logic.”**
  → **Lambda + API Gateway.** Cheapest at low volume, instant scale to zero, minimal ops.

* **“I need containers + custom networking/sidecars/queues or non-HTTP protocols.”**
  → **ECS on Fargate.** Still serverless compute, but with full container control.

* **“I’m deploying a React/Next/Vue front-end from Git with previews and CI built-in.”**
  → **Amplify Hosting.** Superb DX for front-end teams; pair with Amplify backend or your APIs.

* **“It’s a static SPA or marketing site; I just need it crazy fast worldwide.”**
  → **S3 + CloudFront** (optionally **CloudFront Functions/Lambda@Edge** for headers/rewrites/AB tests).

* **“Clients want GraphQL with real-time updates.”**
  → **AppSync** (+ Lambda/DynamoDB) to stay fully serverless end-to-end.

---

# A simple decision path

1. **Is it static only?**
   → **Yes** → **S3 + CloudFront** (or **Amplify Hosting** if you want Git-based CI/preview).
   → **No** (needs server runtime) → continue.

2. **Do you already have a container image / want a web server feel?**
   → **Yes** → Start with **App Runner** (simplest).
   → Need non-HTTP protocols, sidecars, or deep VPC control? → **ECS on Fargate**.
   → **No** → continue.

3. **Is your logic short-lived/stateless and fits in ≤15 minutes per request?**
   → **Yes** → **Lambda + API Gateway** (use provisioned concurrency if latency sensitive).
   → **No** → Prefer **App Runner** (containers), or **Fargate** for advanced needs.

---

# Cost and performance gotchas (quick tips)

* **Cold starts**: Lambda has them; mitigate with **provisioned concurrency**. App Runner avoids them with **min instance** set > 0 (you pay for that baseline).
* **Throughput**: Lambda scales fastest per-request; App Runner/Fargate scale by instances/tasks (warm-up matters).
* **Networking**: Private VPC access is easier with App Runner and Fargate. Lambda VPC is fine but can add init overhead if not tuned.
* **Binary/large deps**: Big runtimes and heavy ML libs are usually smoother in **containers** (App Runner/Fargate) than in Lambda.
* **Background/queue workers**: Prefer **Fargate** (long-running consumers) or **Lambda** (event-driven, short jobs). App Runner is best for HTTP services, not queue daemons.

---

## TL;DR recommendations

* **Most web apps/APIs, minimal ops** → **AWS App Runner**
* **Ultra-cheap, spiky traffic, function-style endpoints** → **Lambda + API Gateway**
* **Container control/custom networking/sidecars** → **ECS on Fargate**
* **Front-end–centric teams** → **Amplify Hosting** (with your API of choice)
* **Pure static** → **S3 + CloudFront**


<img width="1873" height="941" alt="image" src="https://github.com/user-attachments/assets/9d049d3e-4c63-4e93-9305-754c11d05117" />


AWS CloudHSM offers hardware security modules for cryptographic key management, meeting regulatory requirements for hardware-based key storage.

AWS Identity Center (formerly AWS Single Sign-On) allows employees to sign in to a central portal using existing corporate credentials, simplifying account management.

```


**When to choose Amazon DynamoDB and when to choose Amazon Aurora.**

Here is the **cleanest, fastest, exam-ready decision guide**.

---

# 🔥 **DynamoDB vs Aurora — Visual Memory (VERY IMPORTANT)**

![Image](https://miro.medium.com/v2/resize%3Afit%3A1400/1%2AgrD89zaAjSpi-Yl8ZPK5fA.png)

![Image](https://static.abhishek-tiwari.com/old-ghost/images/Amazon-Aurora-Architecture.png)

---

# 🔥 **WHEN TO USE DYNAMODB (NoSQL)**

### ✔ Use Amazon DynamoDB when:

1️⃣ **Massive scale** (millions of requests/sec)
2️⃣ **Unpredictable traffic** (spikes → On-Demand mode)
3️⃣ **Single-digit millisecond latency**
4️⃣ **Key-value or document model**
5️⃣ **Serverless, no maintenance**
6️⃣ **Global tables** for multi-region active-active
7️⃣ **High availability built-in**
8️⃣ **When you need horizontal scaling without effort**
9️⃣ **Microservices**
🔟 **Event-driven architecture**

---

## ⚡ Exam Triggers for DynamoDB:

* “Unpredictable traffic”
* “Scale to millions of requests”
* “Serverless”
* “No schema”
* “Key-value access”
* “Single-digit millisecond latency”
* “Performance at any scale”
* “Global multi-region writes”
* “High-write throughput”

---

# 🔥 **WHEN TO USE AURORA (SQL Relational Database)**

### ✔ Use Amazon Aurora when:

1️⃣ **You need SQL** (MySQL or PostgreSQL)
2️⃣ **Complex JOINs, relational models**
3️⃣ **Transactions (ACID)**
4️⃣ **Strong consistency**
5️⃣ **High write performance**
6️⃣ **Scaling reads using read replicas**
7️⃣ **Multi-region disaster recovery** with Aurora Global DB
8️⃣ **Application already uses MySQL/PostgreSQL**

Aurora is best when you need a **traditional database**, but faster and more scalable.

---

## ⚡ Exam Triggers for Aurora:

* “Relational”
* “SQL queries”
* “ACID transactions”
* “Foreign keys”
* “Complex queries”
* “Low-latency read replicas”
* “Writer/write scaling needed” → **Aurora Serverless v2**
* “Multi-region DR with RPO < 1s”
* “Compatible with MySQL/PostgreSQL”

---

# 🔥 **SUPER QUICK DECISION (MEMORIZE THIS)**

## ✔ If you need **SQL** → **AURORA**

## ✔ If you need **NoSQL** → **DYNAMODB**

---

# 🧠 **Difference Table (Exam Version)**

| Category    | DynamoDB                      | Aurora                          |
| ----------- | ----------------------------- | ------------------------------- |
| Model       | NoSQL                         | SQL                             |
| Schema      | Schema-less                   | Structured schema               |
| Scaling     | Automatic, infinite           | Reader replicas + Serverless v2 |
| Performance | Single-digit ms               | High performance SQL            |
| Writes      | Massive scale                 | Strong ACID transactions        |
| Global      | Global Tables (active-active) | Aurora Global DB (DR)           |
| Operations  | Fully serverless              | Managed DB (more ops)           |
| Cost        | Pay per request               | Pay per instance/storage        |

---

# 🧩 **Which to choose in common scenarios?**

### **Scenario 1 — E-commerce shopping cart**

👉 **DynamoDB** (key-value, high concurrency)

### **Scenario 2 — Banking transactions**

👉 **Aurora** (ACID required)

### **Scenario 3 — IoT millions of events**

👉 **DynamoDB** (massive write scale)

### **Scenario 4 — Analytics app with complex joins**

👉 **Aurora**

### **Scenario 5 — Multi-region global writes**

👉 **DynamoDB Global Tables**

### **Scenario 6 — Multi-region DR with low RPO (<1s)**

👉 **Aurora Global Database**

---

# 🧠 **Golden Rule for Exam**

If the question mentions:

✔ **ACID**
✔ **JOINS**
✔ **Transactions**
✔ **SQL**

→ **AURORA**

If the question mentions:

✔ **Massive scale**
✔ **Key-value**
✔ **Serverless**
✔ **Millions of writes/reads**
✔ **High performance at scale**

→ **DYNAMODB**



# 🔥 **1. Choosing the Right FSx — Protocol & Workload Cheat Sheet**

![Image](https://kodekloud.com/kk-media/image/upload/v1752865994/notes-assets/images/AWS-Solutions-Architect-Associate-Certification-FSx-for-WindowsLustreNetAppOpenZFS/fsx-services-comparison-table.jpg)

![Image](https://d2908q01vomqb2.cloudfront.net/e1822db470e60d090affd0956d743cb0e7cdf113/2025/02/12/FigureTwo_Ref_Arch_after_scalable_metadata.png)

AWS has **four** FSx types:

## ✔ **1. Amazon FSx for Windows File Server**

### **Use when you need:**

* **SMB (Server Message Block)** protocol
* **Windows applications**
* **Active Directory integration**
* NTFS ACLs
* SQL Server, IIS, .NET apps needing Windows FS

### **Key exam triggers:**

* “SMB”
* “Windows-based workloads”
* “Active Directory”
* “NTFS permissions”

---

## ✔ **2. Amazon FSx for Lustre**

### **Use when you need:**

* **Extreme performance**
* **High Throughput + Low Latency**
* **POSIX**
* Machine Learning (SageMaker)
* HPC workloads
* Media rendering
* Genomics

### **Key exam triggers:**

* “HPC”
* “ML training”
* “High throughput”
* “POSIX file system”
* “Backed by S3”

FSx for Lustre can link to S3 → automatically imports metadata.

---

## ✔ **3. Amazon FSx for NetApp ONTAP**

### **Use when you need:**

* **NFS + SMB + iSCSI** (multi-protocol)
* Snapshots / Clone
* Enterprise NAS replacement
* Hybrid workloads
* Storage efficiency (dedupe, compression)

### **Key exam triggers:**

* “Multiprotocol (SMB + NFS)”
* “Enterprise NAS”
* “iSCSI block storage”
* “ONTAP features like snapshots, cloning”

This is the most powerful multiprotocol FS.

---

## ✔ **4. Amazon FSx for OpenZFS**

### **Use when you need:**

* **NFS only**
* Low-latency Unix/Linux apps
* ZFS features (snapshots, clones, compression)
* Lift-and-shift freeBSD/ZFS workloads

### **Key exam triggers:**

* “ZFS”
* “NFS-only requirement”
* “Low latency file storage”
* “Unix/Linux POSIX workloads”

---

# 🧠 **FSx Quick Decision Table (MEMORIZE FOR EXAM)**

| FSx Type        | Protocol              | Use Case                                          |
| --------------- | --------------------- | ------------------------------------------------- |
| FSx for Windows | **SMB**               | AD, Windows apps, NTFS                            |
| FSx for Lustre  | **POSIX (Linux)**     | HPC, ML, Rendering, S3 integration                |
| FSx for ONTAP   | **NFS + SMB + iSCSI** | Enterprise NAS, multiprotocol, cloning, snapshots |
| FSx for OpenZFS | **NFS**               | Linux/Unix apps needing ZFS speed                 |

If you see **Windows / SMB** → FSx for Windows.
If you see **HPC / ML / S3-backed** → FSx for Lustre.
If you see **NFS+SMB+iSCSI** → FSx for ONTAP.
If you see **ZFS / NFS-only** → FSx for OpenZFS.

---

