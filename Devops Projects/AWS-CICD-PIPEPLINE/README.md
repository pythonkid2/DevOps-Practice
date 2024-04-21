# Not completed 

### ci

![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/0adc7fdc-8a5e-43c2-91b4-20bfddf10aac)


Developer Tools  --  CodeBuild -- Build projects


  


### Continuous Integration & Continuous Deployment (CI/CD)

![CI/CD Pipeline](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/305c8812-2af5-46d1-a7bd-5c314e8a3a35)

#### Setting up CodeDeploy

1. **Create Application**: Navigate to Developer Tools -> CodeDeploy -> Application. Create a new application and select EC2 as the Compute platform.

2. **Install CodeDeploy Agent on EC2**:
   - Create a new EC2 instance and SSH into it.
   - [Install the CodeDeploy agent for Ubuntu Server](https://docs.aws.amazon.com/codedeploy/latest/userguide/codedeploy-agent-operations-install-ubuntu.html).
   
3. **Create IAM Role**:
   - While creating the IAM role, choose EC2 and proceed to the next step.
   - Attach the "CodeDeploy Full Access" policy to the role to grant necessary permissions.

![IAM Role Creation](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/dc999c2e-5d7a-4d20-895e-979e68cdfcbd)

4. **Assign Role to EC2 Instance**:
   - Navigate to EC2 -> Instances -> Actions -> Modify IAM role.
   - Attach the created role to the EC2 instance and update.

#### Creating Deployment Group

5. **Create Deployment Group**:
   - Go to Developer Tools -> CodeDeploy -> Applications -> Select your application (e.g., sample-dev-pythonflaskapp).
   - Create a deployment group.

#### Deploying Application

6. **Create Deployment**:
   - Navigate to Developer Tools -> CodeDeploy -> Applications -> Select your application (e.g., sample-dev-pythonflaskapp).
   - Create a deployment.

By following these steps, you'll set up a CI/CD pipeline using AWS CodeDeploy for deploying your application.




