
## Step 1: Setting Up the Infrastructure Server

### Install AWS CLI
First, install the AWS CLI to connect to AWS services:
```bash
sudo apt-get update
sudo apt-get install awscli -y
```
Configure AWS CLI with your credentials:
```bash
aws configure
```

### Install Terraform
Install Terraform to manage your infrastructure:
```bash
sudo snap install terraform --classic
```
Create a directory for your EKS setup:
```bash
mkdir eks
cd eks
```

### Create Terraform Files
Create the following Terraform configuration files:

**main.tf**
```hcl
# Your main Terraform configuration for EKS cluster setup
```

**variables.tf**
```hcl
# Define your variables here
```

**output.tf**
```hcl
# Define your outputs here
```

### Initialize and Apply Terraform Configuration
Initialize Terraform and apply the configuration to set up your EKS cluster:
```bash
terraform init
terraform plan
terraform apply --auto-approve
```

Generate SSH keys for the instances:
```bash
ssh-keygen
```
Apply the configuration with variables:
```bash
terraform apply --var-file='terraform.tfvars'
```

## Step 2: Create EC2 Instances
Create 4 EC2 instances for the following purposes:
- Jenkins Master
- Jenkins Slave (t2.medium)
- SonarQube
- Nexus

## Step 3: Jenkins Master Setup

### Install Java
```bash
sudo apt-get update
sudo apt-get install openjdk-11-jdk -y
```

### Install Jenkins
```bash
wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add -
sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo apt-get update
sudo apt-get install jenkins -y
sudo systemctl start jenkins
sudo systemctl enable jenkins
```

### Install Docker
```bash
sudo apt-get install docker.io -y
sudo usermod -aG docker ubuntu
```

### Install Jenkins Plugins
Install the following plugins in Jenkins:
- SonarQube Scanner
- Config File Provider
- Pipeline Maven Integration
- Docker Pipeline
- Pipeline: Stage View
- Kubernetes
- Kubernetes CLI

### Jenkins Pipeline Configuration
In Jenkins, configure the tools and create a pipeline:

```
pipeline {
    agent any
    tools {
        maven 'M3'
    }
    environment {
        SCANNER_HOME = tool 'sonar-scanner'
    }
    stages {
        stage('Git Checkout') {
            steps {
                echo 'Git Checkout'
                git branch: 'main', url: 'https://github.com/jaiswaladi246/Boardgame.git'
            }
        }
        stage('Compile') {
            steps {
                sh 'mvn compile'
            }
        }
        stage('Unit Testing') {
            steps {
                echo 'Running Unit Tests'
                sh 'mvn test'
            }
        }
        stage('Package') {
            steps {
                sh 'mvn package'
            }
        }
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('sonar') {
                    sh ''' $SCANNER_HOME/bin/sonar-scanner \
                    -Dsonar.projectKey=TaskMaster \
                    -Dsonar.projectName=TaskMaster \
                    -Dsonar.java.binaries=target '''
                }
            }
        }
        stage('Trivy FS Scan') {
            steps {
                echo 'Running Trivy FS Scan'
                sh 'trivy fs --format table -o fs-report.html .'
            }
        }
        stage('Publish to Nexus') {
            steps {
                withMaven(globalMavenSettingsConfig: 'settings', maven: 'maven3') {
                    sh 'mvn deploy'
                }
            }
        }
        stage('Build & Tag Docker Image') {
            steps {
                script {
                    withDockerRegistry(credentialsId: 'docker-cred', toolName: 'docker') {
                        sh 'docker build -t username/taskmaster:latest .'
                    }
                }
            }
        }
        stage('Scan Docker Image with Trivy') {
            steps {
                echo 'Scanning Docker Image'
                sh 'trivy image --format table -o image-report.html username/taskmaster:latest'
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    withDockerRegistry(credentialsId: 'docker-cred', toolName: 'docker') {
                        sh 'docker push username/taskmaster:latest'
                    }
                }
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: '**/target/*.jar', allowEmptyArchive: true
        }
    }
}
```

### Configure Jenkins Tools
In Jenkins, configure the tools used in the pipeline:
1. **Maven Configuration:**
   - Manage Jenkins → Global Tool Configuration → Maven → Add Maven
   - Name: M3
   - Install automatically: Yes
   - Version: 3.6.3

2. **SonarQube Configuration:**
   - Manage Jenkins → Configure System → SonarQube Servers
   - Name: sonar
   - Server URL: http://<SonarQube-server-IP>:9000
   - Server authentication token: <generated-token>

3. **Docker Configuration:**
   - Install Docker in Jenkins Master:
     ```bash
     sudo apt-get install docker.io -y
     sudo usermod -aG docker jenkins
     sudo systemctl restart jenkins
     ```

### Configure Nexus in `pom.xml`
Add the following `distributionManagement` configuration to your `pom.xml` file:
```xml
<distributionManagement>
    <repository>
        <id>maven-releases</id>
        <name>Release Repository</name>
        <url>http://<Nexus-server-IP>:8081/repository/maven-releases/</url>
    </repository>
    <snapshotRepository>
        <id>maven-snapshots</id>
        <name>Snapshot Repository</name>
        <url>http://<Nexus-server-IP>:8081/repository/maven-snapshots/</url>
    </snapshotRepository>
</distributionManagement>
```

Configure Jenkins to use the Nexus credentials:
1. **Add Nexus credentials in Jenkins:**
   - Manage Jenkins → Manage Credentials → Global → Add Credentials
   - Kind: Username with password
   - ID: nexus-cred
   - Username: <Nexus-username>
   - Password: <Nexus-password>

2. **Configure Maven Settings in Jenkins:**
   - Manage Jenkins → Managed Files → Add a new Config
   - Select `Global Maven settings.xml`
   - Add the following to `servers` section:
     ```xml
     <server>
         <id>maven-releases</id>
         <username>${env.NEXUS_USERNAME}</username>
         <password>${env.NEXUS_PASSWORD}</password>
     </server>
     <server>
         <id>maven-snapshots</id>
         <username>${env.NEXUS_USERNAME}</username>
         <password>${env.NEXUS_PASSWORD}</password>
     </server>
     ```

3. **Set Nexus environment variables in Jenkins pipeline:**
   ```groovy
   environment {
       NEXUS_USERNAME = credentials('nexus-cred').username
       NEXUS_PASSWORD = credentials('nexus-cred').password
   }
   ```

### Create SonarQube and Nexus Servers

#### SonarQube
```bash
sudo docker run -d --name sonarqube -p 9000:9000 sonarqube:lts-community
```

#### Nexus
```bash
sudo docker run -d --name nexus -p 8081:8081 sonatype/nexus3
```

### Install Trivy
Follow the [Trivy installation guide](https://aquasecurity.github.io/trivy/v0.18.3/installation/) to install Trivy on your VM.

## Step 4: EKS Configuration

### Install kubectl
```bash
sudo apt-get update
sudo apt-get install -y kubectl
```

### Configure kubectl for EKS
```bash
aws eks --region <region-name> update-kubeconfig --name <cluster-name>
```

This setup should give you a comprehensive CI/CD pipeline with Jenkins, SonarQube, Nexus, Docker, and EKS. Make sure to replace placeholders like `<region-name>` and `<cluster-name>` with your actual values.



# RBAC

## Create Service Account, Role & Assign that role, And create a secret for Service Account and geenrate a Token

### Creating Service Account

kubectl create ns webapps

```
apiVersion: v1
kind: ServiceAccount
metadata:
  name: jenkins
  namespace: webapps
```

### Create Role 


```
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: app-role
  namespace: webapps
rules:
  - apiGroups:
        - ""
        - apps
        - autoscaling
        - batch
        - extensions
        - policy
        - rbac.authorization.k8s.io
    resources:
      - pods
      - componentstatuses
      - configmaps
      - daemonsets
      - deployments
      - events
      - endpoints
      - horizontalpodautoscalers
      - ingress
      - jobs
      - limitranges
      - namespaces
      - nodes
      - secrets
      - pods
      - persistentvolumes
      - persistentvolumeclaims
      - resourcequotas
      - replicasets
      - replicationcontrollers
      - serviceaccounts
      - services
    verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]
```

### Bind the role to service account


```
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: app-rolebinding
  namespace: webapps 
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: app-role 
subjects:
- namespace: webapps 
  kind: ServiceAccount
  name: jenkins 
```
### Create Cluster role & bind to Service Account
```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: jenkins-cluster-role
rules:
- apiGroups: [""] 
  resources: ["persistentvolumes"]
  verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]

---

apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: jenkins-cluster-role-binding
subjects:
- kind: ServiceAccount
  name: jenkins
  namespace: webapps
roleRef:
  kind: ClusterRole
  name: jenkins-cluster-role
  apiGroup: rbac.authorization.k8s.io

```
### Generate token using service account in the namespace

```
apiVersion: v1
kind: Secret
type: kubernetes.io/service-account-token
metadata:
  name: mysecretname
  annotations:
    kubernetes.io/service-account.name: jenkins
```
```
kubectl apply -f secret.yml -n webapps
```

```
kubectl describe secret mysecretname -n webapps
```

copy the token 



stage('Deploy to K8') {
steps {
withKubeConfig(
    caCertificate: 'path/to/ca.crt', // Provide the path to the CA certificate file
    clusterName: 'devopsshack-cluster',
    contextName: 'my-context', // Specify a context name
    credentialsId: 'k8-token', // Provide the correct credentials ID
    namespace: 'webapps',
    restrictKubeConfigAccess: false,
    serverUrl: 'https://6B8E4A35BB5F80D8DODC05A659BE05DF.gr7.ap-south-1.eks.amazonaws.com'
) {

sh 'kubectl apply -f deployment-service.yml -n webapps'
sleep 30 
}




pipeline syntax - 
withKubeConfig: Configure Kubectl

credentials --> secret text --> k8 token

id - K8-token
 

go to aws - eks -cluster 

get api server endpoints 
cluster name
namespace -webapps
 

[Create Token]([https://kubernetes.io/docs/reference/access-authn-authz/service-accounts-admin/#:~:text=To%20create%20a%20non%2Dexpiring,with%20that%20generated%20token%20data.)](https://kubernetes.io/docs/reference/access-authn-authz/service-accounts-admin/#:~:text=To%20create%20a%20non%2Dexpiring,with%20that%20generated%20token%20data.))



## verify the deployment 


stage('verify') {
steps {
withKubeConfig(
    caCertificate: 'path/to/ca.crt', // Provide the path to the CA certificate file
    clusterName: 'devopsshack-cluster',
    contextName: 'my-context', // Specify a context name
    credentialsId: 'k8-token', // Provide the correct credentials ID
    namespace: 'webapps',
    restrictKubeConfigAccess: false,
    serverUrl: 'https://6B8E4A35BB5F80D8DODC05A659BE05DF.gr7.ap-south-1.eks.amazonaws.com'
) {

sh 'kubectl get pods -n webapps'
sh 'kubectl get svc -n webapps'

}


install kubectl in jenkins vm 

