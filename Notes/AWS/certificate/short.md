
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

