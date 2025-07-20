# Table of Contents

- [Elastic Beanstalk](#ElasticBeanstalk)
- [Trusted Advisor](#Trusted-Advisor)
- [Section 2](#section-2)
- [Section 3](#section-3)
- [Section 4](#section-4)
- [Section 5](#section-5)
- [Conclusion](#conclusion)

## ElasticBeanstalk

## ✅ **Elastic Beanstalk (EB)**

### 1. **What**

> AWS Elastic Beanstalk is a **Platform as a Service (PaaS)** that lets you **deploy, manage, and scale web applications** and services without managing the underlying infrastructure (EC2, ALB, Auto Scaling, etc.).

---

### 2. **Why (Use Cases)**

* Quickly deploy **web apps** using languages like Java, .NET, PHP, Python, Node.js, Go, Ruby, or Docker.
* Ideal for teams that want **managed infrastructure** with minimal setup.
* Auto handles **scaling, load balancing, health monitoring**, and patching.
* Supports **zero-downtime deployments** and easy rollbacks.

---

### 3. **How (Configuration)**

* Package your app (ZIP or WAR).
* Go to **Elastic Beanstalk Console** or use **EB CLI**.
* Create an **Environment**:

  * Choose platform (e.g., Python, Node.js).
  * Choose **Web server environment** (for HTTP apps) or **Worker environment** (for background jobs).
* EB automatically provisions:

  * **EC2 instances**
  * **Auto Scaling Group**
  * **Elastic Load Balancer (ELB)**
  * **CloudWatch alarms**
  * Optional: **RDS** DB instances

> You can customize environments using:

* `.ebextensions/` for config files
* Saved configurations
* Custom AMIs

---

### 4. **Common Pitfalls / Limits**

* **Long boot time** if app installation is heavy → use **custom AMI** to preinstall.
* Limited control over low-level infrastructure (vs EC2 or ECS).
* Rolling deployments can **terminate old instances** → configure appropriately.
* No fine-grained IAM per container/app like in ECS/EKS.
* RDS lifecycle is **tied to environment** unless created separately.

---

### 5. **Exam Tips / Keywords**

* “**Quickly deploy web apps**” → Elastic Beanstalk
* “**Manage app without infra**” → EB
* “**Takes 45 mins to start, want 2 mins**” → Use **Custom AMI + Saved Configuration**
* Often compared with:

  * **OpsWorks** (Chef/Puppet config)
  * **CloudFormation** (infra as code)
  * **CodeDeploy** (custom deployments)
* “Fully managed service for deployment” → EB

## Trusted Advisor

## ✅ **AWS Trusted Advisor**

### 1. **What**

> AWS Trusted Advisor is an **online tool** that provides **real-time guidance** to help you **follow AWS best practices** in the areas of **cost optimization, performance, security, fault tolerance**, and **service limits**.

---

### 2. **Why (Use Cases)**

* **Optimize AWS costs** (e.g., detect idle EC2s, underutilized RIs).
* Improve **security posture** (e.g., check for open ports, MFA usage).
* Ensure **service limits** aren’t exceeded (e.g., EC2 instance limits).
* Improve **performance** and **availability** by identifying risks.
* Get proactive recommendations across your AWS resources.

---

### 3. **How (Configuration)**

* Go to **AWS Management Console** → Trusted Advisor.
* By default, **Core checks** are available to **all accounts**:

  * Service Limits
  * IAM Use
  * MFA on Root
  * Billing
* To access **full checks**, you need a support plan:

  * **Business or Enterprise support**
* Categories of checks:

  * **Cost Optimization**
  * **Performance**
  * **Security**
  * **Fault Tolerance**
  * **Service Limits**

You can also:

* **Export results to CSV**
* Use **AWS CLI** or **SDKs** to get check statuses
* Set up **notifications via CloudWatch + SNS**

---

### 4. **Common Pitfalls / Limits**

* Full Trusted Advisor checks require **Business or Enterprise support**.
* Recommendations are **guidance only**, not enforced actions.
* Some checks **do not update in real time** (may be daily/weekly).
* Trusted Advisor **does not fix issues automatically**—you must act.

---

### 5. **Exam Tips / Keywords**

* “**Best practices guidance**” → Trusted Advisor
* “**Cost savings, security, fault tolerance**” → Trusted Advisor
* Only **Core checks available with Basic/Developer support**
* “**Which AWS tool checks for unused resources and security gaps**” → Trusted Advisor
* **NOT** to be confused with **Config (compliance tracking)** or **Inspector (vulnerability scanning)**

---

## Section 2
This is section 2. You can provide detailed content related to this section here.

## Section 3
This is section 3. You can provide detailed content related to this section here.

## Section 4
This is section 4. You can provide detailed content related to this section here.

