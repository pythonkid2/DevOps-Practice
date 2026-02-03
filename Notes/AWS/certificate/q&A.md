### What is cloud computing?
Cloud computing is the on-demand delivery of IT resources and applications through the internet with pay-as-you-go pricing.

### What is another name for on-premises deployment?
Private cloud deployment.

### How does the scale of cloud computing help you to save costs?
The aggregated cloud usage from a large number of customers results in lower pay-as-you-go prices.

### Which Amazon EC2 instance type is suitable for data warehousing applications?
Storage optimized.

### Which Amazon EC2 instance type balances compute, memory, and networking resources?
General purpose.

### Which Amazon EC2 instance type is ideal for high-performance databases?
Memory optimized.

### Which Amazon EC2 instance type offers high-performance processors?
Compute optimized.

### Which Amazon EC2 pricing option provides a discount when you specify a number of EC2 instances to run a specific OS, instance family, and size, and tenancy in one Region?
Standard Reserved Instances.

### Which Amazon EC2 pricing option provides a discount when you make an hourly spend commitment to an instance family and Region for a 1-year or 3-year term?
EC2 Instance Savings Plans.

### Which AWS service is the best choice for publishing messages to subscribers?
Amazon Simple Notification Service (Amazon SNS).

---

### A company needs to run some of its workloads on-premises to comply with regulatory guidelines, while also utilizing the cloud for other workloads. The company requires a consistent management experience across both on-premises and cloud environments. Which AWS service or feature should the company use to meet these requirements?

A. Dedicated Hosts  
B. AWS Outposts (correct answer)  
C. Availability Zones  
D. AWS Wavelength  

**Explanation:**  
AWS Outposts extends AWS infrastructure, services, APIs, and tools to on-premises environments, enabling a truly consistent hybrid experience. It allows companies to run applications on-premises while meeting regulatory requirements, leveraging the same AWS tools for both on-premises and cloud environments.

---

### What is the recommended use case for Amazon EC2 On-Demand Instances?

A. A steady-state workload that requires a specific EC2 instance configuration for an extended period  
B. A workload that can be interrupted and requires the lowest possible cost  
C. An unpredictable workload that does not require a long-term commitment (correct answer)  
D. A workload that is expected to run for more than 1 year  

**Explanation:**  
Amazon EC2 On-Demand Instances are ideal for workloads that vary in usage and require flexibility without upfront commitments or long-term contracts.

---

### A company needs an AWS networking solution that can serve as a centralized gateway to connect multiple VPCs and on-premises networks. Which AWS service or feature will meet this requirement?

A. Gateway VPC Endpoint  
B. AWS Direct Connect  
C. AWS Transit Gateway (correct answer)  
D. AWS PrivateLink  

**Explanation:**  
AWS Transit Gateway enables customers to connect multiple VPCs and on-premises networks through a central hub, simplifying network management and scaling.

### An administrator observed that multiple AWS resources were deleted yesterday. Which AWS service will help identify the cause and determine who deleted the resources?

A. AWS CloudTrail (correct answer)  
B. Amazon Inspector (for vulnerability scan) 
C. Amazon GuardDuty  (treat detector)
D. AWS Trusted Advisor  (helps to find best practices)

**Explanation:**  
AWS CloudTrail records account activity and API calls across your AWS infrastructure, providing detailed logs of all actions taken. It helps track who deleted resources and when.

### To assist companies with Payment Card Industry Data Security Standard (PCI DSS) compliance in the cloud, AWS provides:

A. physical inspections of data centers by appointment.  
B. required PCI compliance certifications for any application running on AWS.  
C. an AWS Attestation of Compliance (AOC) report for specific AWS services. (correct answer)  
D. professional PCI compliance services.  

**Explanation:**  
AWS provides an Attestation of Compliance (AOC) report for specific services that meet PCI DSS standards. This report verifies that these services have been validated for PCI DSS compliance, helping companies meet their own compliance requirements.

### In which situations should a company create an IAM user instead of an IAM role?

A. When an application that runs on Amazon EC2 instances requires access to other AWS services  
B. When the company creates AWS access credentials for individuals (correct answer)  
C. When the company creates an application that runs on a mobile phone that makes requests to AWS  
D. When the company needs to add users to IAM groups (correct answer)  
E. When users are authenticated in the corporate network and want to be able to use AWS without having to sign in a second time  

**Explanation:**  
IAM users are created when individual people need AWS access with their own credentials. This is different from an IAM role, which is typically used for granting temporary permissions to applications or services.

### A company hosts a web application on AWS and has improved the availability of its application by provisioning multiple Amazon EC2 instances. The company wants to distribute its traffic across the EC2 instances while providing a single point of contact to the web clients. Which AWS service can distribute the traffic to multiple EC2 instances as targets?

A. VPC endpoints  
B. Application Load Balancer (correct answer)  
C. NAT gateway  
D. Internet gateway  

**Explanation:**  
An **Application Load Balancer** is designed to distribute incoming application traffic across multiple targets, such as EC2 instances, in different Availability Zones. It provides a single point of contact for clients, improving availability and fault tolerance for web applications.

**Question:**  
A company stores data in an Amazon S3 bucket. Which task is the responsibility of AWS?

A. Configure an S3 Lifecycle policy  
B. Activate S3 Versioning  
C. Configure S3 bucket policies  
D. Protect the infrastructure that supports S3 storage

**Answer:**  
**D. Protect the infrastructure that supports S3 storage**

In the shared responsibility model, AWS is responsible for protecting the infrastructure that runs all services, including Amazon S3. The other options (A, B, and C) are responsibilities of the customer.



**Question:**  
A company wants to transfer a virtual Windows Server 2022 that is currently running in its own data center to AWS. The company wants to automatically convert the existing server to run directly on AWS infrastructure instead of virtualized hardware.  
Which AWS service will meet these requirements?

A. AWS DataSync  / used for tranfer data
B. AWS Database Migration Service (AWS DMS)   / database migration
C. AWS Application Discovery Service  /used for identifying dependencies 
D. AWS Application Migration Service

**Answer:**  
**D. AWS Application Migration Service**

AWS Application Migration Service (AWS MGN) allows companies to migrate applications from on-premises to AWS infrastructure with minimal changes. It converts servers to run natively on AWS infrastructure, enabling a smooth lift-and-shift migration.


**Question:**  
Which AWS service is a fully managed NoSQL database service?

A. Amazon RDS  
B. Amazon Redshift  
C. Amazon DynamoDB  
D. Amazon Aurora

**Answer:**  
**C. Amazon DynamoDB**

Amazon DynamoDB is a fully managed NoSQL database service that provides fast and flexible database performance for any scale. It is specifically designed for applications that require low-latency data access for a wide range of use cases.

https://youtu.be/o49CpjPKXug?si=Zj9ODFgxWNx63GuP&t=3086

<img width="1157" height="662" alt="image" src="https://github.com/user-attachments/assets/da7e451d-4f84-4b37-95c0-666cb8473fd7" />

Here is the **clean, precise, exam-ready explanation** of **ENA** and **EFA** — what they are, why they exist, and when to use each one.

---

# 🚀 **1. ENA – Elastic Network Adapter**

## **What is ENA?**

ENA is AWS’s **high-performance network interface** for EC2 instances that provides:

* **High throughput** (up to 100 Gbps)
* **Low latency**
* **Enhanced networking** using **SR-IOV** (single-root I/O virtualization)

It replaces the older Intel 82599/ixgbe model.

## **Why use ENA?**

To get **fast, consistent, and low-latency network performance** for workloads such as:

* High-traffic web applications
* Microservices talking over the network
* Big data processing
* Large-scale distributed systems
* Anything requiring fast east-west (VPC) traffic

ENA reduces noise, jitter, and CPU overhead, making network performance more stable.

## **When to use ENA?**

Use ENA when:

* Your instance type **supports enhanced networking**
* You need **high throughput** (10–100 Gbps)
* You run **general high-performance distributed workloads**
* You want improved performance **inside the VPC**

Typical examples:

* Application servers (Java, Node, Go)
* Database clusters (Aurora, MongoDB, Cassandra)
* EKS/ECS worker nodes
* Analytics workloads

> **ENA = default choice for any modern EC2 needing performance networking.**

---

# ⚡ 2. EFA – Elastic Fabric Adapter

## **What is EFA?**

EFA is a **specialized network interface** for **HPC (High-Performance Computing)** and **ML training** requiring:

* **Ultra-low latency**
* **High packet rate**
* **OS-bypass networking** (*libfabric*)
* **MPI communication acceleration**

EFA makes communication between nodes in HPC clusters **faster than ENA**.

## **Why use EFA?**

To run HPC applications that depend on:

* **MPI (Message Passing Interface)**
* **Parallel compute nodes**
* **Inter-node synchronization**
* **Distributed machine learning training**

EFA uses **OS bypass** to avoid kernel network stack overhead → massive performance improvement.

## **When to use EFA?**

When your workload needs **supercomputer-level interconnect**, such as:

* CFD (Computational fluid dynamics)
* Seismic analysis
* Weather simulations
* Molecular dynamics
* Large-scale distributed ML (TensorFlow, PyTorch Horovod)
* Parallel MPI clusters

> **EFA = HPC and ML training requiring ultra-low-latency inter-node communication.**

---

# 🎯 Quick Comparison (Exam Ready Summary)

| Feature        | **ENA**                             | **EFA**                                                 |
| -------------- | ----------------------------------- | ------------------------------------------------------- |
| Purpose        | General high-performance networking | HPC & ML training networking                            |
| Throughput     | Up to 100 Gbps                      | Up to 100 Gbps but lower latency                        |
| Latency        | Low                                 | **Ultra-low**                                           |
| MPI support    | ❌ Not optimized for MPI             | ✅ Yes (OS-bypass, libfabric)                            |
| Use case       | Web apps, microservices, DBs, EKS   | HPC, ML distributed training                            |
| OS bypass      | ❌ No                                | ✅ Yes                                                   |
| Instance types | Most modern EC2                     | Limited HPC-optimized instances (c5n, p4d, hpc6a, etc.) |

---

# 🧠 Memory Rule (Easy Trick)

* **ENA → Enhanced Networking for Applications** (general workloads)
* **EFA → Enhanced Fabric for Acceleration** (HPC/ML workloads)

---

# ✅ Final Recommendation

* Use **ENA** by default for any production EC2 with high network needs.
* Use **EFA** only for **specialized HPC/ML workloads** requiring **MPI** and **ultra-low latency**.


