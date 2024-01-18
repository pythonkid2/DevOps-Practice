# AWS DevOps

AWS DevOps involves leveraging Amazon Web Services (AWS) to implement and enhance DevOps practices, enabling organizations to streamline their software development and deployment processes. Key components of AWS DevOps include:

- **Continuous Integration and Continuous Delivery (CI/CD):** AWS offers services such as AWS CodePipeline, AWS CodeBuild, and AWS CodeDeploy, which enable the automation of the build, testing, and deployment of applications.

- **Infrastructure as Code (IaC):** AWS CloudFormation and AWS CDK (Cloud Development Kit) allow teams to define and provision infrastructure and AWS resources in a declarative manner, promoting consistency and scalability.

- **Monitoring and Logging:** AWS provides services like Amazon CloudWatch and AWS CloudTrail, which enable monitoring, logging, and the collection of operational data for applications and infrastructure.

- **Containerization and Orchestration:** AWS supports Docker-based containerization through Amazon Elastic Container Service (ECS) and Amazon Elastic Kubernetes Service (EKS), facilitating the management and scaling of containerized applications.

- **Security and Compliance:** AWS offers a range of security services and features, including AWS Identity and Access Management (IAM), AWS Key Management Service (KMS), and AWS Security Hub, which help ensure the security and compliance of applications and data on the AWS platform.

By leveraging AWS DevOps services and tools, organizations can achieve increased automation, faster delivery, improved scalability, enhanced security, and streamlined management of their applications and infrastructure in the cloud.

***
https://github.com/vilasvarghese/aws/blob/master/AWSTOCNotes.txt
practical -line 8605

***

# AWS CI/CD Pipeline

The following is a simplified representation of an AWS CI/CD pipeline:

1. **Git:** Version control system for managing source code.

2. **AWS CodeCommit:** Secure, scalable, managed source control service to host private Git repositories.

3. **AWS CodeBuild:** Fully managed build service that compiles source code, runs tests, and produces software packages.

4. **Docker Container:** A standardized unit of software that packages up code and all its dependencies so the application runs quickly and reliably.

5. **AWS CodeDeploy:** Automated deployment service that deploys applications to EC2 instances, Lambda functions, or ECS services.

6. **CodePipeline:** Fully managed continuous delivery service that helps automate the release pipelines for fast and reliable application and infrastructure updates.

The workflow typically involves fetching code from Git repositories in CodeCommit, triggering a build process using CodeBuild, and deploying the built artifacts with CodeDeploy. CodePipeline orchestrates and integrates these steps, creating an end-to-end delivery process from source code to deployment.

***

**IAM**

<img width="843" alt="image" src="https://github.com/pythonkid2/DevOps-Practice/assets/100591950/f929ffc1-67d8-4934-a8ad-79e954d23357">

**Security**
<img width="563" alt="image" src="https://github.com/pythonkid2/DevOps-Practice/assets/100591950/dc498d25-f6e3-45db-9b31-aacfe52a6376">

