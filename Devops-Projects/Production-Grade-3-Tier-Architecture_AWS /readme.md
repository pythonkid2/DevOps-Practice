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

# Setting Up a Secure and Isolated VPC Environment

To establish a secure and isolated environment for the application, a **Virtual Private Cloud (VPC)** is essential. This configuration involves creating multiple subnets across two **Availability Zones** (AZs) for high availability, fault tolerance, and isolation between tiers.

---

#### 1. **VPC Architecture**
- Create a **Virtual Private Cloud (VPC)** to isolate the network for the application.
- Use **two Availability Zones (AZs)** to increase fault tolerance and availability.
- Each AZ will contain:
  - **One public subnet** for the **Presentation Tier** (Nginx/React.js).
  - **Two private subnets** for the **Application Tier** (Node.js) and **Data Tier** (RDS).

![image](https://github.com/user-attachments/assets/2f380498-23c5-42c5-a069-0b18807553d3)

---

#### 2. **NAT Gateway for Internet Access**
- Instances in **private subnets** need internet access to download updates and patches.
- Deploy a **NAT Gateway** in one of the public subnets to provide internet access to instances in the private subnets.
- This gateway allows outbound internet traffic while keeping the private instances inaccessible from outside.

---

#### 3. **Public Subnet for the Presentation Tier**
- The **public subnets** will host **EC2 instances** running the web server (**Nginx**) for the Presentation Tier.
- These instances need **public IP addresses** to receive traffic from the internet. Ensure that public IP assignment is enabled for instances launched in these subnets.

![image](https://github.com/user-attachments/assets/e61ff4a5-f1a1-42a9-8f47-effca1571300)

---

#### 4. **Private Subnets for Application and Data Tiers**
- **Private subnets** will host the **Application Tier** (Node.js on EC2) and **Data Tier** (RDS) to ensure they are not directly accessible from the internet.
  - The **Application Tier** instances will communicate with the **Presentation Tier** and handle the business logic.
  - The **Data Tier** will host the **RDS** database with replication across AZs for fault tolerance.

![image](https://github.com/user-attachments/assets/bbd8458e-6271-44c6-85ce-cef0b2eba02c)

---

#### 5. **Simplified IP Address Management**
- To simplify the management of the environment, enable **automatic assignment of public IP addresses** for EC2 instances in the **public subnets**. This ensures that instances in the public subnets can easily be reached from the internet.

![image](https://github.com/user-attachments/assets/6582dcef-42a0-4186-84fd-c9cae98d22ea)

---

This VPC setup ensures a **secure**, **scalable**, and **fault-tolerant** environment by isolating each tier in the appropriate subnet and enabling controlled internet access through the **NAT Gateway**.

### Setting Up Security Groups for the Three-Tier Application

To establish proper network security and manage traffic flow within the VPC, **Security Groups** will be configured for different components of the infrastructure. These security groups define the inbound and outbound rules, ensuring secure and organized communication between tiers.

---

#### 1. **Bastion Host Security Group**
- **Purpose**: Acts as a gateway to private resources in the VPC.
- **Inbound Rules**: Allow **SSH (port 22)** from any IP (for demo). In production, restrict to a specific IP range for security.

![bastion-host](https://github.com/user-attachments/assets/9b95ba5e-10a3-4d2a-9a35-635801cd223f)

---

#### 2. **Presentation Tier Load Balancer (ALB) Security Group**
- **Purpose**: Handle incoming traffic from the internet to the frontend.
- **Inbound Rules**: Allow **HTTP (port 80)** from any IP. HTTPS traffic is handled by CloudFront for security.

![presentation-tier-alb](https://github.com/user-attachments/assets/cd0ebd8c-d1ba-4a43-9613-952e1a5966e3)

---

#### 3. **Presentation Tier EC2 Instances Security Group**
- **Purpose**: Manage frontend instances (React/Nginx).
- **Inbound Rules**:
  - Allow **SSH (port 22)** from the **Bastion Host** for secure connections.
  - Allow **HTTP (port 80)** from the **Load Balancer** to forward web traffic.

![presentation-tier-EC2](https://github.com/user-attachments/assets/ccfb266d-aa76-432c-ab2c-28496d64a859)

---

#### 4. **Application Tier Load Balancer (ALB) Security Group**
- **Purpose**: Manage traffic from the frontend to the backend.
- **Inbound Rules**: Allow **HTTP (port 80)** from the **Presentation Tier EC2 Instances** for seamless frontend-backend communication.

![application-tier-alb](https://github.com/user-attachments/assets/0e2330c9-3bc4-412f-b122-ff2075a8a2f9)

---

#### 5. **Application Tier EC2 Instances Security Group**
- **Purpose**: Manage backend instances (Node.js).
- **Inbound Rules**:
  - Allow **SSH (port 22)** from the **Bastion Host** for secure access.
  - Allow **TCP (port 3200)** from the **Application Tier Load Balancer** for backend traffic routing.

![application-tier-ec2](https://github.com/user-attachments/assets/ce1e464c-fbbb-4a94-8f8c-0ab1eeebf8b8)

---

#### 6. **Data Tier Security Group**
- **Purpose**: Secure access to the database (RDS).
- **Inbound Rules**:
  - Allow **MySQL (port 3306)** from the **Bastion Host** and **Application Tier EC2 Instances** for database access and application queries.

![data-tier](https://github.com/user-attachments/assets/6dda7d84-627f-4432-a2ae-d643d630b1aa)

---

By carefully configuring the security groups for each component, this setup ensures a robust security posture while maintaining efficient communication between tiers in the architecture.

# launching the Bastion host
---

### 1. **Naming and Basic Configuration**
   - Name the instance as **Bastion Host** for clear identification within your environment.
   - Choose **basic free-tier eligible settings** to minimize costs.

   ![image](https://github.com/user-attachments/assets/f0f77694-a03f-40f9-b988-15689b6befb3)

---

### 2. **Key Pair Setup**
   - **Key Pair**: Select an existing key pair or create a new one if needed. This will allow secure SSH access to the Bastion Host.
   
   ![image](https://github.com/user-attachments/assets/e79b3e00-7ab0-4648-a483-35ccda8db389)

---

### 3. **VPC and Subnet Assignment**
   - Choose the appropriate **VPC** and the **public subnet** where the Bastion Host will be deployed.
   - This ensures the host is in the correct network zone for accessing your private resources.

   ![image](https://github.com/user-attachments/assets/f200482d-259b-404b-a8a7-286859106669)

---

### 4. **Security Group Association**
   - Assign the **Bastion Host** to the security group you created earlier. This controls what traffic can access the host, ensuring secure communication.

---

# Setting up Data Tier with RDS MySQL Instance
Create DB subnet group
![image](https://github.com/user-attachments/assets/1d0980cc-5d9b-4217-a51c-bd14173e6eeb)
![image](https://github.com/user-attachments/assets/f9fb7322-f3c3-4724-8ebe-83223fe785a7)


Create database 
![image](https://github.com/user-attachments/assets/f65141a0-2c26-4576-864b-35d163325a88)
![image](https://github.com/user-attachments/assets/979a749a-1725-4e87-80c1-824d72738d3e)
![image](https://github.com/user-attachments/assets/5af9d51d-2df0-40da-b16e-ce4b975650ef)
![image](https://github.com/user-attachments/assets/5a35f029-d256-493b-8055-ce202d20a3a6)
![image](https://github.com/user-attachments/assets/54dcddaf-92ab-47fb-8809-1171d6bea84e)
![image](https://github.com/user-attachments/assets/57ce0306-2b7f-45bb-9f66-18870363de1b)


Install MySQL
To download MySQL repository package:
wget https://dev.mysql.com/get/mysql80-community-release-el9-1.noarch.rpm
To verify the package download:
ls -lrt 
To install MySQL repository package:
sudo dnf install -y mysql80-community-release-el9-1.noarch.rpm 
![image](https://github.com/user-attachments/assets/d1494f96-6c11-452c-a3a2-12643e060aba)

To import GPG key:
sudo rpm --import https://repo.mysql.com/RPM-GPG-KEY-mysql-2023 
To update package index:
sudo dnf update –y 
To install MySQL server:
sudo dnf install -y mysql-community-server  
![image](https://github.com/user-attachments/assets/3707e7ae-fbc9-4376-a0a4-14f7e56ddd6a)

To start the mysql service:
sudo systemctl start mysqld
To enable mysql to start on boot:
sudo systemctl enable mysqld 
To secure the mysql installation:
sudo grep 'temporary password' /var/log/mysqld.log 

sudo mysql_secure_installation 
To create database and restore data, please refer SQL scripts on db.sql file.
