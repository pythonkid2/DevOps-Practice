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

# Configuring Route 53

To configure **Amazon Route 53** for the three-tier architecture project, follow the steps below. This process will ensure your domain routes traffic correctly to the **presentation tier** via the **Application Load Balancer (ALB)** and supports secure connections with **SSL**.

---

#### 1. **Navigate to Route 53**
- Go to **Route 53** in the AWS Management Console and select **Hosted Zones**.

![image](https://github.com/user-attachments/assets/4c7d2db0-516c-43a2-97da-3d2a309b2803)

---

#### 2. **Create a Hosted Zone**
- Click **Create Hosted Zone**.
- Enter your **domain name** (e.g., `example.com`) and choose **Public Hosted Zone**.

  ![image](https://github.com/user-attachments/assets/31d111fa-dc74-4aec-a2b7-865ec7ac0333)

---

#### 3. **Update Domain Name Server (NS) Records**
- After the hosted zone is created, Route 53 generates a set of **name servers (NS)**. Copy these NS records.
- Go to your domain registrar (e.g., GoDaddy, Namecheap) and update the **NS records** to use the ones from Route 53.

  ![image](https://github.com/user-attachments/assets/63ad9e5c-75c0-45ce-b5d0-ad70a631421a)

---

#### 4. **Create DNS Record Sets**
- Inside the hosted zone, create **A Records** to point to your **Application Load Balancer (ALB)**.
  - **Type**: A (IPv4 Address).
  - **Alias**: Yes.
  - **Alias Target**: Select your **Internet-Facing ALB**.
  - This will route traffic from your domain (e.g., `example.com`) to your presentation tier.

  ![image](https://github.com/user-attachments/assets/9704db38-d53b-4c3b-a115-43af5d6ce208)

---

# Requesting a Public SSL Certificate from AWS Certificate Manager (ACM)

Follow these steps to request and validate an **SSL certificate** for your domain to enable secure HTTPS communication for your application.

---

#### 1. **Navigate to AWS Certificate Manager (ACM)**
- In the AWS Management Console, search for **AWS Certificate Manager (ACM)** and open it.

![image](https://github.com/user-attachments/assets/2df8f4b6-e239-401f-b57b-3a48b023056f)

---

#### 2. **Request a Public Certificate**
- Click on **Request a Certificate**.
- Select **Request a public certificate**.

![image](https://github.com/user-attachments/assets/8481b897-b083-4c47-ae62-9bb0e10add12)

---

#### 3. **Enter Domain Name**
- Enter the **domain name** for which you need the SSL certificate (e.g., `example.com`).
- Add any necessary **subdomains** (e.g., `www.example.com`).

![image](https://github.com/user-attachments/assets/0c14db0a-8874-448d-8f71-861b995a4902)

---

#### 4. **Choose Validation Method**
- Select **DNS Validation** to prove ownership of the domain. This method will require you to add specific DNS records to your **Route 53 hosted zone**.

![image](https://github.com/user-attachments/assets/fa4df33a-5ea3-4e61-9046-58418d809b89)

---

#### 5. **Add DNS Records to Route 53**
- After requesting the certificate, ACM provides a **CNAME record** that needs to be added to your **Route 53 Hosted Zone** to validate domain ownership.
- Go to **Route 53**, open your hosted zone, and create a new **CNAME record** using the details provided by ACM.

---

#### 6. **Certificate Issuance**
- Once AWS verifies the DNS record, the certificate will be issued.
- You can now attach the SSL certificate to your **CloudFront distribution** or **Application Load Balancer (ALB)** to enable secure HTTPS communication.

---

# Creating a Virtual Private Cloud (VPC) and Subnets 

