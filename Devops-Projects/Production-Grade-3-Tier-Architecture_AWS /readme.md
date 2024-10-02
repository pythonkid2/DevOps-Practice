# Deploy a Production-Grade 3-Tier Architecture on AWS 

CloudFront, ALB, ASG, EC2, RDS, CloudWatch

![image](https://github.com/user-attachments/assets/a3247f68-3bc6-4020-b0d3-0f8b3b7c6098)

https://www.youtube.com/watch?v=6rsJlfpwnP4&t=123s
![image](https://github.com/user-attachments/assets/91aaabad-b4c2-49fd-83f0-01eb5e9c9f1a)


### Three-Tier Architecture Overview

This architecture is designed for **high availability**, **scalability**, and **fault tolerance**. The three tiers include a **Presentation Tier**, **Application Tier**, and **Data Tier**, all within an isolated AWS Virtual Private Cloud (VPC). 

#### 1. **AWS Cloud Environment**
- **VPC (Virtual Private Cloud)**: Provides network isolation and serves as the foundation of the architecture.
- **Availability Zones (AZ)**: Divided into two zones to enhance fault tolerance and availability. Each AZ contains:
  - **Public Subnet** (for Presentation Tier)
  - **Private Subnet** (for Application Tier)
  - **Private Subnet** (for Data Tier)

#### 2. **Data Tier**
- **Multi-Availability Zone RDS**:
  - **Primary Database**: Resides in one AZ's private subnet.
  - **Standby Database**: Synchronously replicates to another AZ's private subnet.
  - **Business Continuity**: If the primary instance fails, the standby instance automatically takes over.

#### 3. **Application Tier**
- **Auto Scaling Group (ASG)**:
  - Hosts **EC2 instances** running a **Node.js** application managed by **PM2**.
  - Automatically adjusts capacity based on demand, balancing the workload across availability zones to prevent bottlenecks.
  
- **Internal Application Load Balancer (ALB)**: 
  - Distributes traffic among **EC2 instances** within private subnets.

#### 4. **Presentation Tier**
- **Auto Scaling Group (ASG)**:
  - Distributes **EC2 instances** running **Nginx** as a web server, delivering the **React.js** application.
  - Ensures high availability and scalability across availability zones.

- **Internet-Facing Application Load Balancer (ALB)**:
  - Manages external traffic and distributes incoming requests across **presentation tier EC2 instances**.

- **Bastion Host**: 
  - Deployed outside the auto-scaling group to serve as a controlled entry point for secure access to private subnets.

#### 5. **Traffic Management**
- **Amazon Route 53**:
  - Manages DNS, mapping domain names to resources.

- **SSL Certificate**:
  - Procured from AWS Certificate Manager for **HTTPS** connections.
  - Integrated with **CloudFront** (CDN) to encrypt data and optimize content delivery.

#### 6. **Security and Performance**
- **HTTPS**: Ensures secure access to the application.
- **CloudFront**: Optimizes content delivery to users, integrating with SSL certificates.

#### 7. **Fault Tolerance and Failover**
- **RDS Synchronous Replication**: Provides high availability by replicating data between the primary and standby instances.
- **Automatic Failover**: In the event of primary database failure, the standby instance takes over with minimal downtime.

#### 8. **Monitoring and Scaling**
- **Amazon CloudWatch**:
  - Manages application logs and provides centralized access for troubleshooting and performance analysis.
  - **CloudWatch Alarms**: Trigger scaling actions within the auto-scaling groups based on demand.

- **Cost Efficiency**: By scaling out during peak periods and scaling in during low traffic periods, the system maintains cost efficiency while ensuring consistent performance.
