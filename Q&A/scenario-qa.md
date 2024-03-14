
Q1
how you can set up a Jenkins pipeline using Terraform to create an AWS load balancer and automatically destroy it after a day

## Q1

To create a pipeline using Jenkins and Terraform that automatically destroys AWS resources (in this case, a load balancer) after a day to avoid cost problems, you can follow these steps:

1. **Set Up Jenkins**:
   - Install Jenkins on a server or use a Jenkins instance.
   - Install necessary plugins like the Pipeline plugin for Jenkins.

2. **Set Up Terraform**:
   - Install Terraform on the machine where Jenkins is running.
   - Configure the AWS provider in Terraform with appropriate credentials.

3. **Create a Jenkins Pipeline**:
   - Create a new Jenkins pipeline job.
   - Define the pipeline script in the Jenkinsfile.

4. **Define the Terraform Configuration**:
   - Create Terraform configuration files to create the AWS resources, in this case, an AWS load balancer.
   - Include a resource that schedules the destruction of the load balancer after a day. This can be achieved using a `time_sleep` resource in Terraform.

5. **Pipeline Steps**:
   - The pipeline steps should include:
     - Checkout code from your version control system.
     - Initialize Terraform.
     - Plan and apply Terraform to create the load balancer.
     - Schedule the destruction of the load balancer after a day.
     - Commit the changes to the Terraform configuration back to the repository.

6. **Destroy Resources**:
   - Create a separate Jenkins job that runs daily to destroy the resources created by Terraform after a day.
   - This job should run a Terraform destroy command to remove the load balancer.

By following these steps, you can create a pipeline using Jenkins and Terraform that automatically destroys AWS resources, such as a load balancer, after a day to prevent cost problems. This approach helps in managing resources efficiently and avoiding unnecessary costs from running resources longer than needed.

---

Below is an example of how you can set up a Jenkins pipeline using Terraform to create an AWS load balancer and automatically destroy it after a day:

1. **Jenkins Pipeline Script (Jenkinsfile)**:
```groovy
pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/your-repo.git'
            }
        }
        
        stage('Terraform Apply') {
            steps {
                script {
                    sh 'terraform init'
                    sh 'terraform plan -out=tfplan'
                    sh 'terraform apply tfplan'
                }
            }
        }
    }
    
    post {
        always {
            script {
                sh 'echo "Destroying resources after a day"'
                sh 'terraform destroy -auto-approve'
            }
        }
    }
}
```

2. **Terraform Configuration**:
- Create a Terraform configuration file (e.g., `main.tf`) to define the AWS load balancer and schedule its destruction after a day.
- Here is an example of how you can use the `time_sleep` resource in Terraform to schedule the destruction after a day:
```hcl
resource "aws_lb" "example" {
  // AWS load balancer configuration
}

resource "time_sleep" "destroy_after_day" {
  depends_on = [aws_lb.example]
  duration   = "1d"
}
```

3. **Jenkins Job for Daily Destruction**:
- Create a separate Jenkins job that runs daily to destroy the resources created by Terraform after a day.
- This job should run a Terraform destroy command to remove the load balancer.

By setting up the Jenkins pipeline with Terraform and scheduling the destruction of resources after a day, you can automate the process of creating and destroying AWS resources to avoid unnecessary costs.
