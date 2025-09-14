
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




