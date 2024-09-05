# Automated CI/CD Pipeline for Scalable NGINX Web Application Deployment using AWS, Jenkins, and CodeDeploy

Here is a comprehensive guide to set up a CI/CD pipeline using AWS, Jenkins, and CodeDeploy to deploy a simple NGINX web application, ensuring scalability through Auto Scaling. This guide will address each requirement in the problem statement:

---

### **1. Prerequisites**

- **AWS Account**: Ensure you have an AWS account with appropriate permissions.
- **Jenkins Server**: Jenkins installed on a separate EC2 instance.
- **GitHub/Bitbucket**: A Git repository to host your code (HTML and deployment scripts).
- **CodeDeploy**: Set up on AWS with a properly configured service role.
- **IAM Roles**: Ensure you have IAM roles for EC2 instances (CodeDeploy permissions) and Jenkins to access S3 and CodeDeploy.

---

### **2. Web Application Setup**

#### Step 1: Set Up the Simple Web Application
We will deploy an NGINX web server with a basic HTML page.

- Create a directory structure in your local machine:
  ```bash
  mkdir nginx-app
  cd nginx-app
  mkdir scripts
  touch index.html
  ```

- Add the following simple HTML content in `index.html`:
  ```html
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

- **scripts/install_nginx.sh**:
  This script will install NGINX on the EC2 instance during deployment.
  ```bash
  #!/bin/bash
  sudo apt update -y
  sudo apt install nginx -y
  ```

- **scripts/start_nginx.sh**:
  This script will start the NGINX service after installation.
  ```bash
  #!/bin/bash
  sudo systemctl start nginx
  ```

- **scripts/deploy.sh**:
  This script will copy the HTML file to the appropriate directory and restart NGINX.
  ```bash
  #!/bin/bash
  sudo cp /home/ubuntu/nginx-app/index.html /var/www/html/index.html
  sudo systemctl restart nginx
  ```

---

### **3. CodeDeploy Setup**

#### Step 2: Create an S3 Bucket for Deployment Artifacts
- Log into AWS Console.
- Navigate to **S3** and create a new bucket (e.g., `nginx-deployments-bucket`).
  
#### Step 3: Create a CodeDeploy Application
1. Go to **AWS CodeDeploy**.
2. Create an application (e.g., `nginx-webapp-deployment`).
3. Create a deployment group and choose EC2/On-Premises.
4. Attach the appropriate IAM role to the deployment group (ensure it has access to EC2, S3, and CodeDeploy).

#### Step 4: AppSpec File for CodeDeploy
- Create an `appspec.yml` in the root of your project directory.
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

### **4. Jenkins Setup**

#### Step 5: Set Up Jenkins on a Separate EC2 Instance
1. Launch a new EC2 instance and install Jenkins.
2. Ensure security groups allow traffic on port 8080.
3. Install necessary plugins:
   - **AWS CodeDeploy Plugin**: Integrate Jenkins with CodeDeploy.
   - **Git Plugin**: For repository integration.

#### Step 6: Create Jenkins Pipeline
1. Set up a new pipeline in Jenkins.
2. Define the Jenkinsfile in your project repository. For example:
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
                         awsAccessKey: '',
                         awsSecretKey: '',
                         awsRegion: 'us-east-1'])
               }
           }
       }
   }
   ```

3. This pipeline performs the following:
   - Clones the repository.
   - Zips the project.
   - Uploads the artifact to S3.
   - Triggers the CodeDeploy deployment.

---

### **5. EC2 and Auto Scaling Setup**

#### Step 7: Launch EC2 Instances for Auto Scaling Group
1. Create a launch template with the following configuration:
   - **AMI**: Use a Linux AMI.
   - **User Data**: Add a script to install the CodeDeploy agent.
     ```bash
     #!/bin/bash
     sudo apt update -y
     sudo apt install -y ruby wget
     cd /home/ubuntu
     wget https://aws-codedeploy-us-east-1.s3.amazonaws.com/latest/install
     chmod +x ./install
     sudo ./install auto
     ```

2. Create an Auto Scaling Group:
   - Use the launch template created.
   - Attach it to a load balancer (optional but recommended for scaling).

#### Step 8: Configure Auto Scaling Policies
1. Set up scaling based on CPU utilization or HTTP request load on the load balancer.
2. Ensure that new instances are automatically updated with the latest deployment using CodeDeploy.

---

### **6. Testing and Validation**

#### Step 9: Push Code to Repository
- Make any changes to the HTML or scripts and push them to the GitHub/Bitbucket repository.
- This should automatically trigger the Jenkins pipeline, upload the new artifact to S3, and deploy it to the EC2 instances via CodeDeploy.

#### Step 10: Access the Web Application
- Access the web application by hitting the public IP of your EC2 instance or through the load balancer’s DNS name in a browser.

---

### **7. Troubleshooting**

#### Common Issues:
- **CodeDeploy Agent Installation**: Ensure the agent is correctly installed on all EC2 instances.
- **IAM Role Permissions**: Ensure that the EC2 instance roles have the correct permissions to interact with CodeDeploy and S3.
- **Pipeline Failures**: Review Jenkins logs and ensure all AWS credentials are configured correctly.

---

### **Why CodeDeploy?**
- **Automated Deployments**: CodeDeploy automates the deployment process, minimizing manual intervention.
- **Scalability**: It works seamlessly with Auto Scaling groups, ensuring new instances automatically receive the latest deployment.
- **Rollback**: It provides built-in rollback capabilities, which are essential for handling failed deployments.

---

This setup ensures a complete CI/CD pipeline with AWS, Jenkins, CodeDeploy, and scaling through Auto Scaling groups.
