## Caching

Caching is the process of storing a copy of data in a temporary or cache storage location so it can be accessed more quickly.

<img width="604" alt="image" src="https://github.com/pythonkid2/DevOps-Practice/assets/100591950/b0394b0b-59a0-42af-b885-aef22d3a3fa1">

The AWS infrastructure is built around Regions and Availability Zones (AZs). An AWS Region is a physical location in the world which has multiple Availability Zones ( AZs). These Availability Zones consist of one or more discrete data centers, each with redundant power, networking, and connectivity, housed in separate facilities. Each Region is completely independent. Each Availability Zone is isolated, but the Availability Zones in a region are connected through low-latency links.


Edge locations that are separate from Regions and are located at other locations. These Edge locations allow you to push your content near to your customers to give them a better experience on your platform.

# IAM

What is Identity and Access Management?

Identity and Access Management is a framework to ensure that the right people in your organization can access the right service or
as per their job.

IAM is a web service that helps you securely control access to AWS accounts and resources. The purpose of IAM is to control who is authenticated (signed in) and authorized (has permission) to use resources.

You can provide secure access to multiple users to AWS resources with IAM. An AWS account is created with a single identity that gives you full access to the AWS account and its resources.

This identity is called the AWS account root user, and you use the email address and password you used to create the account.

# S3

<img width="604" alt="image" src="https://github.com/pythonkid2/DevOps-Practice/assets/100591950/218b2357-06d5-40b3-9096-e4a9bfbedeee">

## Storage Class 

<img width="335" alt="image" src="https://github.com/pythonkid2/DevOps-Practice/assets/100591950/b107a582-e83e-4eb7-a9ee-9cb0ab11f5d2">

<img width="568" alt="image" src="https://github.com/pythonkid2/DevOps-Practice/assets/100591950/f498bdf1-a22b-4b1b-ad17-730474fbe9d4">

<img width="310" alt="image" src="https://github.com/pythonkid2/DevOps-Practice/assets/100591950/488badb9-2366-49c0-b9c4-be3f0fb5e808">

<img width="368" alt="image" src="https://github.com/pythonkid2/DevOps-Practice/assets/100591950/a2f4c865-bead-44b1-ba85-e29de46d9a9d">

<img width="379" alt="image" src="https://github.com/pythonkid2/DevOps-Practice/assets/100591950/7e0a32e3-396a-496a-b052-0902a17efd72">

<img width="607" alt="image" src="https://github.com/pythonkid2/DevOps-Practice/assets/100591950/05119b28-4885-4ce2-adfe-8dac33796659">

<img width="613" alt="image" src="https://github.com/pythonkid2/DevOps-Practice/assets/100591950/3470aaa5-f436-4b30-a7bf-2ab5769ff398">

<img width="357" alt="image" src="https://github.com/pythonkid2/DevOps-Practice/assets/100591950/15c9a922-1315-4801-8cbc-9cc323343e9d">

<img width="329" alt="image" src="https://github.com/pythonkid2/DevOps-Practice/assets/100591950/0a05c663-e200-4d79-a2aa-b1fa454dc8a7">

<img width="613" alt="image" src="https://github.com/pythonkid2/DevOps-Practice/assets/100591950/756ae999-2832-4f87-8056-8ffc51872a04">

# VPC



<img width="597" alt="image" src="https://github.com/pythonkid2/DevOps-Practice/assets/100591950/e1c1b107-571f-467a-bf10-1ff654d682c3">
<img width="388" alt="image" src="https://github.com/pythonkid2/DevOps-Practice/assets/100591950/fc1f41ea-e0f3-4954-88c6-c0cd4b70dda1">
<img width="563" alt="image" src="https://github.com/pythonkid2/DevOps-Practice/assets/100591950/064dc727-ea7b-43d6-83e8-dde1f79ca4b3">
<img width="598" alt="image" src="https://github.com/pythonkid2/DevOps-Practice/assets/100591950/7cfc6d58-33a8-4e8b-9c00-accc29ecc41d">
<img width="548" alt="image" src="https://github.com/pythonkid2/DevOps-Practice/assets/100591950/ca979919-ce8f-4ae6-a712-7538fe8981a0">
<img width="557" alt="image" src="https://github.com/pythonkid2/DevOps-Practice/assets/100591950/2ba94c99-c9cb-48d2-a66f-0e2bb26c337b">

<img width="545" alt="image" src="https://github.com/pythonkid2/DevOps-Practice/assets/100591950/a657c564-cdfa-4187-9977-96ec03daf797">
<img width="545" alt="image" src="https://github.com/pythonkid2/DevOps-Practice/assets/100591950/f96261cb-2db1-42ee-94a6-a72af790fcac">


## Amazon Virtual Private Cloud (VPC)

**What is a VPC?**

A Virtual Private Cloud (VPC) is a dedicated virtual network environment within the AWS Cloud. It provides logically isolated networking infrastructure for your AWS resources, offering granular control over IP address ranges, subnets, route tables, and network gateways.

**Key Features:**

* **Isolation:** VPCs are isolated from other virtual networks in the AWS Cloud, ensuring security and privacy for your resources.
* **Customization:** You have complete control over your VPC's network configuration, including IP address ranges, subnets, route tables, and network gateways.
* **Resource Hosting:** Launch diverse AWS resources within your VPC, such as Amazon EC2 instances, RDS databases, and more.
* **Geographic Scope:** A VPC spans across all Availability Zones (AZs) within your chosen region, promoting high availability and fault tolerance.

**Getting Started:**

1. **Name and CIDR Block:** When creating a VPC, assign a unique name and a CIDR block (e.g., 10.0.0.0/16) to define the available IP address range.
2. **Default VPC:** Each region comes with a pre-configured default VPC containing a subnet in each AZ. 

**Benefits:**

* **Enhanced Security:** Isolate sensitive resources within private subnets and control access through security groups.
* **Improved Availability:** Distribute resources across multiple subnets in different AZs for increased fault tolerance.
* **Optimized Resource Management:** Group resources based on function or application for easier management and scalability.

**Additional Notes:**

* Hyphens or asterisks can be used to create bullet points in Markdown format.
* Consider adding code blocks for the CIDR block example.
* For further details, explore the official AWS VPC documentation.

# EC2

<img width="559" alt="image" src="https://github.com/pythonkid2/DevOps-Practice/assets/100591950/33a0ca70-683c-4398-a9c2-f6ecbfd7149a">

<img width="310" alt="image" src="https://github.com/pythonkid2/DevOps-Practice/assets/100591950/36ed27f9-28ab-4463-ba59-150f9b26480b">

https://aws.amazon.com/products/compute/

<img width="555" alt="image" src="https://github.com/pythonkid2/DevOps-Practice/assets/100591950/2fac1edd-9739-4e1e-b0a5-0efb105b925c">

<img width="353" alt="image" src="https://github.com/pythonkid2/DevOps-Practice/assets/100591950/d22bd307-23d0-4b3d-ab8a-2fd9c34f6f1c">


General Purpose: Suitable for small to medium-sized databases, web servers, and development environments that require a balance of resources.

Compute Optimized: Ideal for applications that require high compute power, such as scientific simulations, rendering, and high-performance computing (HPC).

Memory Optimized: Well-suited for memory-intensive workloads like in-memory databases, big data processing, and analytics.

Storage Optimized: Best for data-intensive tasks like NoSQL databases, data warehousing, and high-capacity file servers.

Accelerated Computing: Designed for AI, machine learning, deep learning, and GPU-intensive workloads like video encoding and rendering.
2. Instance Naming Components:



Instance Family: The broad category indicating the general purpose of the instance, like "t2" or "m5".

Instance Type: The specific instance type within the family, often reflecting the resource balance or specialization, like "micro" or "large".

Generation: A version identifier for the instance type, denoted by a number (e.g., "2" in "m5.2xlarge").

Size: Refers to the size within the family and type, such as "2xlarge" or "4xlarge".

GPU or CPU Type: In instances with specialized hardware, the GPU or CPU model might be specified, like "g4" for GPU or "c5" for CPU.
3. The Right Instance:



Understand your workload's resource requirements (CPU, memory, storage, network) and identify any specialized needs (GPU, instance store, etc.).

Consider whether your workload is bursty, consistent, memory-intensive, compute-intensive, etc.

Use AWS's instance type comparison tool and cost calculator to help choose the most cost-effective option.

Monitor your application's performance and resource utilization and adjust instance types as needed.

<img width="355" alt="image" src="https://github.com/pythonkid2/DevOps-Practice/assets/100591950/e1affc73-0823-4748-90c2-05af77ed93a8">


D<img width="541" alt="image" src="https://github.com/pythonkid2/DevOps-Practice/assets/100591950/833be449-d577-4172-a3cd-03f70eed1245">

<img width="560" alt="image" src="https://github.com/pythonkid2/DevOps-Practice/assets/100591950/3ff2d2b4-0776-4612-9aaa-fcdda59fec19">










