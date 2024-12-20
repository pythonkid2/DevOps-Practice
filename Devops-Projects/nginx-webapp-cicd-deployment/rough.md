To create a clear, structured guide for your task—setting up a scalable CI/CD pipeline using AWS, Jenkins, and CodeDeploy—I've reorganized and refined the steps to ensure a logical progression. Here is the revised version:

---

## **Automated CI/CD Pipeline for Scalable NGINX Web Application Deployment**

This guide will take you through the complete process of setting up a CI/CD pipeline using AWS, Jenkins, and CodeDeploy to deploy an NGINX web application. The solution is scalable through Auto Scaling, and new code pushes automatically trigger deployments.

---

### **Prerequisites**
 
Before starting, ensure the following resources are ready:
- **AWS Account** with full access permissions.
- **Jenkins Server** running on an EC2 instance or other host.
- **Git Repository** (GitHub or Bitbucket) to host the web application code.
- **AWS CodeDeploy** with a configured deployment group and IAM roles.

---

## **Step-by-Step Implementation**

---

### **Step 1: Set Up the Web Application**

1. Create a basic NGINX web server application locally:
   ```
   mkdir nginx-app
   cd nginx-app
   mkdir scripts
   touch index.html
   ```

2. Add a simple HTML page in `index.html`:
   ```
   <!DOCTYPE html>
   <html>
   <head>
       <title>Welcome to NGINX!</title>
   </head>
   <body>
       <h1>Deployed via CodeDeploy!</h1>
   </body>
   </html>
   ```

3. Create deployment scripts:
   - **scripts/install_nginx.sh** (installs NGINX):
     ```
     #!/bin/bash
     sudo apt update -y
     sudo apt install nginx -y
     ```

   - **scripts/start_nginx.sh** (starts NGINX service):
     ```
     #!/bin/bash
     sudo systemctl start nginx
     ```

   - **scripts/deploy.sh** (deploys the web page):
     ```
     #!/bin/bash
     sudo cp /home/ubuntu/nginx-app/index.html /var/www/html/index.html
     sudo systemctl restart nginx
     ```

4. Push this code to your Git repository (GitHub/Bitbucket).


To push your code to your GitHub repository, follow these steps:

### **1. Create a GitHub Repository**

If you don't already have a repository, you'll need to create one:

1. **Log in to GitHub**:
   - Go to [GitHub](https://github.com/) and log in with your credentials.

2. **Create a New Repository**:
   - Click on the **+** icon in the top-right corner and select **New repository**.
   - Fill in the repository details:
     - **Repository name**: e.g., `nginx-webapp-deployment`
     - **Description**: (Optional) Describe your repository.
     - **Public/Private**: Choose based on your preference.
   - Click **Create repository**.

### **2. Prepare Your Local Project**

Make sure your local project directory is set up correctly:

1. **Navigate to Your Project Directory**:
   ```
   cd /path/to/your/nginx-app
   ```

2. **Initialize Git**:
   If your project is not already a Git repository, initialize it:
   ```
   git init
   ```

3. **Add Your Files**:
   Add all the files in your project to the Git staging area:
   ```
   git add .
   ```

4. **Commit Your Changes**:
   Commit the files with a descriptive message:
   ```
   git commit -m "Initial commit of NGINX web application and deployment scripts"
   ```

### **3. Add Your GitHub Repository as a Remote**

1. **Copy the Repository URL**:
   - Go to your GitHub repository page.
   - Click on the **Code** button and copy the HTTPS URL (e.g., `https://github.com/pythonkid2/nginx-webapp-deployment.git`).

2. **Add Remote Origin**:
   ```
   git remote add origin https://github.com/pythonkid2/nginx-webapp-deployment.git
   ```

### **4. Push Your Code to GitHub**

1. **Push to the Remote Repository**:
   ```
   git push -u origin main
   ```
   - If you're using a different branch name (e.g., `master`), replace `main` with your branch name.

2. **Verify Your Push**:
   - Go to your GitHub repository page.
   - Refresh the page to ensure that your files have been pushed and are visible in the repository.

---

### **Step 2: Create AWS Infrastructure**

#### 2.1 Launch EC2 Instances for Auto Scaling

1. In the AWS Console, go to **EC2** and create a **Launch Template**:
   - Use a **Linux AMI** (Amazon Linux 2 or Ubuntu).
   - Add **User Data** to automatically install the CodeDeploy agent:
     ```
     #!/bin/bash
     sudo apt update -y
     sudo apt install ruby wget -y
     https://aws-codedeploy-us-east-2.s3.us-east-2.amazonaws.com/latest/install
     chmod +x ./install
     sudo ./install auto
     ```

2. Create an **Auto Scaling Group**:
   - Use the **Launch Template** you created.
   - Optionally, attach the Auto Scaling group to a **Load Balancer** for better scaling.

#### 2.2 Create S3 Bucket for Deployment Artifacts

1. Go to **S3** in AWS.
2. Create a new bucket (e.g., `nginx-deployments-bucket`) to store deployment artifacts.

---

### **Step 3: Set Up AWS CodeDeploy**

#### 3.1 Create CodeDeploy Application

1. In AWS, navigate to **CodeDeploy**.
2. Create an application (e.g., `nginx-webapp-deployment`).
3. Create a **Deployment Group** using either an **Auto Scaling Group** or specific EC2 instances.
4. Attach an **IAM Role** to the deployment group that has the following permissions:
   - **AWSCodeDeployRole**
   - **AmazonEC2RoleforAWSCodeDeploy**

#### 3.2 Configure the AppSpec File for Deployment

1. In your project root directory, create an `appspec.yml`:
   ```yaml
   version: 0.0
   os: linux
   files:
     - source: /
       destination: /home/ubuntu/nginx-app
   hooks:
     BeforeInstall:
       - location: scripts/install_nginx.sh
         timeout: 300
         runas: root
     AfterInstall:
       - location: scripts/deploy.sh
         timeout: 300
         runas: root
     ApplicationStart:
       - location: scripts/start_nginx.sh
         timeout: 300
         runas: root
   ```

---

### **Step 4: Set Up IAM Roles**

#### 4.1 Create IAM Role for EC2 Instances

1. In the **IAM Management Console**, create a new role for EC2 instances.
2. Attach the **AmazonEC2RoleforAWSCodeDeploy** policy to the role.
3. Attach this role to the EC2 instances.

#### 4.2 Create IAM Role for Jenkins

1. Create a new IAM role for Jenkins with the following policies:
   - **AmazonS3FullAccess**
   - **AWSCodeDeployFullAccess**
2. Attach this role to the EC2 instance running Jenkins.

---

### **Step 5: Install CodeDeploy Agent on EC2 Instances**

#### 5.1 Install CodeDeploy Agent

1. **For Amazon Linux 2**:
   ```
   sudo yum update -y
   sudo yum install ruby wget -y
   wget https://aws-codedeploy-us-east-1.s3.amazonaws.com/latest/install
   chmod +x ./install
   sudo ./install auto
   sudo service codedeploy-agent start
   ```

2. **For Ubuntu**:
   ```
   sudo apt-get update -y
   sudo apt-get install ruby wget -y
   wget https://aws-codedeploy-us-east-1.s3.amazonaws.com/latest/install
   chmod +x ./install
   sudo ./install auto
   sudo service codedeploy-agent start
   ```

3. Verify the installation:
   ```
   sudo service codedeploy-agent status
   ```

---

### **Step 6: Set Up Jenkins**

#### 6.1 Install Jenkins on EC2

1. Launch an **EC2 Instance** for Jenkins.
2. Install Jenkins following the official instructions.
3. Ensure Jenkins is accessible on port 8080.

#### 6.2 Install Jenkins Plugins

1. Go to **Manage Jenkins** > **Manage Plugins**.
2. Install the following plugins:
   - **AWS CodeDeploy Plugin**
   - **Git Plugin**
   - **Pipeline Plugin**

---

### **Step 7: Configure Jenkins Pipeline**

#### 7.1 Create a Jenkins Pipeline

1. In Jenkins, create a **New Item** and select **Pipeline**.
2. Add a **Jenkinsfile** to your project repository:
   ```groovy
   pipeline {
       agent any
       stages {
           stage('Clone Repository') {
               steps {
                   git branch: 'main', url: 'https://github.com/username/nginx-app.git'
               }
           }
           stage('Archive Artifacts') {
               steps {
                   sh 'zip -r nginx-app.zip .'
                   archiveArtifacts artifacts: 'nginx-app.zip', allowEmptyArchive: false
               }
           }
           stage('Upload to S3') {
               steps {
                   withAWS(credentials: 'aws-credentials') {
                       s3Upload(file: 'nginx-app.zip', bucket: 'nginx-deployments-bucket', path: 'nginx-app.zip')
                   }
               }
           }
           stage('Deploy via CodeDeploy') {
               steps {
                   step([$class: 'AWSCodeDeployPublisher',
                         applicationName: 'nginx-webapp-deployment',
                         deploymentGroupName: 'nginx-deployment-group',
                         deploymentConfig: 'CodeDeployDefault.AllAtOnce',
                         s3bucket: 'nginx-deployments-bucket',
                         s3prefix: '',
                         excludes: '',
                         awsRegion: 'us-east-1'])
               }
           }
       }
   }
   ```

#### 7.2 Add Credentials to Jenkins

1. Go to **Manage Jenkins** > **Configure System**.
2. Add AWS credentials (IAM User with CodeDeploy and S3 access).

---

### **Step 8: Testing and Deployment**

1. **Push Code Changes**: Make any changes to the code and push to the Git repository.
2. **Jenkins Pipeline**: Ensure Jenkins picks up the changes, runs the pipeline, uploads the artifact to S3, and triggers CodeDeploy.
3. **Access the Web Application**: Once the deployment is complete, access the web application via the public IP of the EC2 instances or the load balancer's DNS name.

---

### **Step 9: Configure Auto Scaling**

1. Set up scaling policies based on metrics like CPU utilization or request load.
2. Ensure that new EC2 instances in the Auto Scaling group automatically receive the latest CodeDeploy deployment.

---

This complete step-by-step guide will enable you to deploy a scalable web application using AWS, Jenkins, and CodeDeploy with a fully automated CI/CD pipeline.
