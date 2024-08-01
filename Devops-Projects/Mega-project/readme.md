
## First Create a user in AWS IAM with any name
## Attach Policies to the newly created user
## below policies
AmazonEC2FullAccess

AmazonEKS_CNI_Policy

AmazonEKSClusterPolicy	

AmazonEKSWorkerNodePolicy

AWSCloudFormationFullAccess

IAMFullAccess

#### One more policy we need to create with content as below

json

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "eks:*",
            "Resource": "*"
        }
    ]
}
```
Attach this policy to your user as well

![Policies To Attach](https://github.com/jaiswaladi246/Microservice/blob/Infra-Steps/Policies.png)

# AWSCLI
```
sudo apt install unzip
```
[Install](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

### [Install Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)

Install Terraform to manage your infrastructure:

```
sudo snap install terraform --classic
```
Create a directory for your EKS setup:

```
mkdir eks
cd eks
```

### Create Terraform Files
Create the following Terraform configuration files:

**main.tf**
```
provider "aws" {
  region = "us-east-2"
}

resource "aws_vpc" "mega_project_vpc" {
  cidr_block = "10.0.0.0/16"

  tags = {
    Name = "mega_project-vpc"
  }
}

resource "aws_subnet" "mega_project_subnet" {
  count = 2
  vpc_id                  = aws_vpc.mega_project_vpc.id
  cidr_block              = cidrsubnet(aws_vpc.mega_project_vpc.cidr_block, 8, count.index)
  availability_zone       = element(["us-east-2a", "us-east-2b"], count.index)
  map_public_ip_on_launch = true

  tags = {
    Name = "mega_project-subnet-${count.index}"
  }
}

resource "aws_internet_gateway" "mega_project_igw" {
  vpc_id = aws_vpc.mega_project_vpc.id

  tags = {
    Name = "mega_project-igw"
  }
}

resource "aws_route_table" "mega_project_route_table" {
  vpc_id = aws_vpc.mega_project_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.mega_project_igw.id
  }

  tags = {
    Name = "mega_project-route-table"
  }
}

resource "aws_route_table_association" "a" {
  count          = 2
  subnet_id      = aws_subnet.mega_project_subnet[count.index].id
  route_table_id = aws_route_table.mega_project_route_table.id
}

resource "aws_security_group" "mega_project_cluster_sg" {
  vpc_id = aws_vpc.mega_project_vpc.id

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "mega_project-cluster-sg"
  }
}

resource "aws_security_group" "mega_project_node_sg" {
  vpc_id = aws_vpc.mega_project_vpc.id

  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "mega_project-node-sg"
  }
}

resource "aws_eks_cluster" "mega_project" {
  name     = "mega_project-cluster"
  role_arn = aws_iam_role.mega_project_cluster_role.arn

  vpc_config {
    subnet_ids         = aws_subnet.mega_project_subnet[*].id
    security_group_ids = [aws_security_group.mega_project_cluster_sg.id]
  }
}

resource "aws_eks_node_group" "mega_project" {
  cluster_name    = aws_eks_cluster.mega_project.name
  node_group_name = "mega_project-node-group"
  node_role_arn   = aws_iam_role.mega_project_node_group_role.arn
  subnet_ids      = aws_subnet.mega_project_subnet[*].id

  scaling_config {
    desired_size = 3
    max_size     = 3
    min_size     = 3
  }

  instance_types = ["t2.medium"]

  remote_access {
    ec2_ssh_key = var.ssh_key_name
    source_security_group_ids = [aws_security_group.mega_project_node_sg.id]
  }
}

resource "aws_iam_role" "mega_project_cluster_role" {
  name = "mega_project-cluster-role"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "eks.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF
}

resource "aws_iam_role_policy_attachment" "mega_project_cluster_role_policy" {
  role       = aws_iam_role.mega_project_cluster_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy"
}

resource "aws_iam_role" "mega_project_node_group_role" {
  name = "mega_project-node-group-role"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF
}

resource "aws_iam_role_policy_attachment" "mega_project_node_group_role_policy" {
  role       = aws_iam_role.mega_project_node_group_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy"
}

resource "aws_iam_role_policy_attachment" "mega_project_node_group_cni_policy" {
  role       = aws_iam_role.mega_project_node_group_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy"
}

resource "aws_iam_role_policy_attachment" "mega_project_node_group_registry_policy" {
  role       = aws_iam_role.mega_project_node_group_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly"
}

```

**variables.tf**
```
variable "ssh_key_name" {
  description = "The name of the SSH key pair to use for instances"
  type        = string
  default     = "ohiokey"
}
```

**output.tf**
```
output "cluster_id" {
  value = aws_eks_cluster.mega_project.id
}

output "node_group_id" {
  value = aws_eks_node_group.mega_project.id
}

output "vpc_id" {
  value = aws_vpc.mega_project_vpc.id
}

output "subnet_ids" {
  value = aws_subnet.mega_project_subnet[*].id
}

```
### Initialize and Apply Terraform Configuration
Initialize Terraform and apply the configuration to set up your EKS cluster:

```
terraform init
```
```
terraform plan
```
```
terraform apply --auto-approve
```

### For create/update kubeconfig file
```
aws eks --region us-east-2 update-kubeconfig --name mega_project-cluster
```
```
sudo snap install kubectl --classic
```

#### go to RBAC to create token - change names where required(example jenkins)

pipeline syntax --> withKubeConfig: Configure Kubernetes CLI (kubectl)

secret text --> paste secret

add k8-token

Kubernetes server endpoint :go to aws eks copy API server endpoint

cluster name : copy 

### Setup email notification

prereq: port 465

Manage Jenkins --> System --> Extended E-mail Notification --> 

SMTP server 
```
smtp.gmail.com
```

Add credention -mail id and app password created


Manage Jenkins --> System --> **E-mail Notification**

SMTP server 
```
smtp.gmail.com
```
click advanced enable  use ssl

use smtp authentication 

username - 

```
mjcmathew@gmail.com
```

password- (create app password)

go to 
```
https://myaccount.google.com/apppasswords
```

smtp port 

465


## Step 2: Create EC2 Instances


## Create VMs
```
mkdir vm
cd vm
```
```
vi main.tf
```
```
provider "aws" {
  region = "us-east-2"
}

resource "aws_instance" "ec2_instance" {
  count         = var.number_of_instances
  ami           = var.ami_id
  subnet_id     = var.subnet_id
  instance_type = var.instance_type
  key_name      = var.ami_key_pair_name
  security_groups = ["sg-09b752b3641fd65c4"]
  tags = {
    Name = "${var.instance_name}-${count.index + 1}"  # Append unique index to instance name
  }

  root_block_device {
    volume_size = 20  # Set the storage size to 20 GiB
  }
}

resource "null_resource" "disable_strict_host_key_checking" {
  count = var.number_of_instances

  connection {
    type        = "ssh"
    host        = aws_instance.ec2_instance[count.index].public_ip
    user        = "ubuntu"
    private_key = file("/home/ubuntu/vm/ohiokey.pem")
  }

  provisioner "remote-exec" {
    inline = [
      "mkdir -p ~/.ssh",
      "echo 'Host *' >> ~/.ssh/config",
      "echo '  StrictHostKeyChecking no' >> ~/.ssh/config",
      "echo '  UserKnownHostsFile=/dev/null' >> ~/.ssh/config",
      "echo '  LogLevel ERROR' >> ~/.ssh/config" # Suppress warnings
    ]
  }

  depends_on = [aws_instance.ec2_instance]
}

resource "null_resource" "configure_ssh" {
  count = var.number_of_instances

  connection {
    type        = "ssh"
    host        = aws_instance.ec2_instance[count.index].public_ip
    user        = "ubuntu"
    private_key = file("/home/ubuntu/vm/ohiokey.pem")
  }

  provisioner "file" {
    source      = "/home/ubuntu/.ssh/id_ed25519.pub"
    destination = "/home/ubuntu/id_ed25519.pub"
  }

  provisioner "remote-exec" {
    inline = [
      "mkdir -p ~/.ssh",
      "cat /home/ubuntu/id_ed25519.pub >> ~/.ssh/authorized_keys",
      "chmod 700 ~/.ssh",
      "chmod 600 ~/.ssh/authorized_keys"
    ]
  }

  depends_on = [aws_instance.ec2_instance, null_resource.disable_strict_host_key_checking]
}

output "vm_info" {
  value = { for idx, instance in aws_instance.ec2_instance : "${instance.tags.Name}" => instance.public_ip }
}

```
```
vi terraform.tfvars
```
```
#terraform.tfvars
instance_name        = "Test-instance"
instance_type        = "t2.medium"
subnet_id            = "subnet-022eea447577344cf"
ami_id               = "ami-0862be96e41dcbf74"  # Updated AMI ID
number_of_instances  = 3
ami_key_pair_name    = "ohiokey"
```

```
vi variables.tf
```

```
#  variables.tf
variable "instance_name" {
  description = "Name of the instance to be created"
  default     = "Test-instance"
}

variable "instance_type" {
  description = "Type of instance to be created"
  default     = "t2.micro"
}

variable "subnet_id" {
  description = "The VPC subnet the instance(s) will be created in"
  default     = "subnet-022eea447577344cf"
}

variable "ami_id" {
  description = "The AMI to use"
  default     = "ami-0862be96e41dcbf74"
}

variable "number_of_instances" {
  description = "Number of instances to be created"
  default     = 1
}

variable "ami_key_pair_name" {
  description = "Key pair name for the instances"
  default     = "ohiokey"
}

variable "resource_tags" {
  description = "Tags for the VM on cloud"
  default     = "Test-VM"
}
```

Generate SSH keys for the instances:

```
ssh-keygen
```

to add public key of ansible master to created vms 

copy pem file to primary server 

```
scp -i "ohiokey.pem" ohiokey.pem ubuntu@3.16.55.120:/home/ubuntu/vm
```

```
terraform init
```
```
terraform plan
```
Apply the configuration with variables:
```
terraform apply --var-file='terraform.tfvars'
```





Create 4 EC2 instances for the following purposes:
- Jenkins Master
- Jenkins Slave (t2.medium)
- SonarQube
- Nexus

### Installation with Ansible
#### Install Ansible

```
sudo apt install ansible-core
```
```
vi inventory
```
```
[servers]
test-instance-1 ansible_host=3.111.197.52 ansible_user=ubuntu
test-instance-2 ansible_host=52.66.210.89 ansible_user=ubuntu
test-instance-3 ansible_host=43.205.118.230 ansible_user=ubuntu

[jenkins]
test-instance-1

[sonarqube]
test-instance-2

[nexus]
test-instance-3

```
```
vi install.yml
```
```
---
- hosts: all
  become: yes
  tasks:
    - name: Update and upgrade apt packages
      apt:
        update_cache: yes
        upgrade: dist

- hosts: jenkins
  become: yes
  tasks:
    - name: Install JDK
      apt:
        name: openjdk-17-jre-headless
        state: present

    - name: Add Jenkins repository key
      shell: |
        wget -O /usr/share/keyrings/jenkins-keyring.asc https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
      register: result
      until: result.rc == 0
      retries: 3
      delay: 5

    - name: Add Jenkins repository
      shell: |
        echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/" | tee /etc/apt/sources.list.d/jenkins.list
      register: result
      until: result.rc == 0
      retries: 3
      delay: 5

    - name: Update apt cache
      shell: apt-get update
      register: result
      until: result.rc == 0
      retries: 3
      delay: 5

    - name: Install Jenkins
      shell: apt-get install -y jenkins
      register: result
      until: result.rc == 0
      retries: 3
      delay: 5

    - name: Install Docker
      apt:
        name: docker.io
        state: present

    - name: Add current user to Docker group
      shell: sudo chmod 666 /var/run/docker.sock

    - name: Label Jenkins server IP
      set_fact:
        jenkins_ip: "{{ ansible_host }}"

- hosts: sonarqube
  become: yes
  tasks:
    - name: Install Docker
      apt:
        name: docker.io
        state: present

    - name: Add current user to Docker group
      shell: sudo chmod 666 /var/run/docker.sock

    - name: Run SonarQube container
      docker_container:
        name: sonarqube
        image: sonarqube:lts-community
        state: started
        ports:
          - "9000:9000"

    - name: Label SonarQube server IP
      set_fact:
        sonarqube_ip: "{{ ansible_host }}"

- hosts: nexus
  become: yes
  tasks:
    - name: Install Docker
      apt:
        name: docker.io
        state: present

    - name: Add current user to Docker group
      shell: sudo chmod 666 /var/run/docker.sock

    - name: Run Nexus container
      docker_container:
        name: nexus
        image: sonatype/nexus3
        state: started
        ports:
          - "8081:8081"

    - name: Label Nexus server IP
      set_fact:
        nexus_ip: "{{ ansible_host }}"

- hosts: localhost
  gather_facts: no
  tasks:
    - name: Gather IPs of all servers
      set_fact:
        jenkins_ip: "{{ hostvars['test-instance-1'].jenkins_ip }}"
        sonarqube_ip: "{{ hostvars['test-instance-2'].sonarqube_ip }}"
        nexus_ip: "{{ hostvars['test-instance-3'].nexus_ip }}"

    - name: Print Jenkins IP
      debug:
        msg: "Jenkins IP: {{ jenkins_ip }}"

    - name: Print SonarQube IP
      debug:
        msg: "SonarQube IP: {{ sonarqube_ip }}"

    - name: Print Nexus IP
      debug:
        msg: "Nexus IP: {{ nexus_ip }}"

```
to run ansible 

```
ansible-playbook -i inventory install.yml
```



## Step 3: Jenkins Master Setup

### Install Java

```
sudo apt-get update
sudo apt-get install openjdk-17-jdk -y
```

### Install Jenkins

debianubuntu

```
https://www.jenkins.io/doc/book/installing/linux/#debianubuntu
```

### Install Docker

https://docs.docker.com/engine/install/ubuntu/

ssh to jenkins vm 

### Install Trivy
Follow the [Trivy installation guide](https://aquasecurity.github.io/trivy/v0.18.3/installation/) to install Trivy on your VM.


## Jenkins Setup 
```
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```

set up the jenkins server 

### Install Jenkins Plugins
Install the following plugins in Jenkins:

- SonarQube Scanner
- Config File Provider
- Pipeline Maven Integration
- Docker Pipeline
- Pipeline: Stage View
- Kubernetes
- Kubernetes CLI


### Configure Jenkins Tools

In Jenkins, configure the tools used in the pipeline:

**Maven:**
   - Manage Jenkins → Tool → Maven → Add Maven
   - Name: M3
   - Install automatically: Yes
   - Version: 3.9.8

**SonarQube Scanner installations**

Manage Jenkins → Tool → SonarQube Scanner installations

Name : sonar-scanner


**credentials** :


docker-cred
Username with password ( docker hub)



global --> add credentials 

git-cred 

Username with password

in git hub --> Settings --> Developer Settings  -->generate classic token


global --> add credentials 
Secret text

go to sonar server --> Administration --> Security --> Users --> generate 

add as sonar-token

**SonarQube Configuration:**
   - Manage Jenkins → System → SonarQube Servers
   - Name: sonar
   - Server URL: http://<SonarQube-server-IP>:9000
   - Server authentication token: <generated-token>

. **Docker Configuration:**  - fo r manual 
   - Install Docker in Jenkins Master:
     ```bash
     sudo apt-get install docker.io -y
     sudo usermod -aG docker jenkins
     sudo systemctl restart jenkins
     ```





## Nexus config 

Dashboard --> Manage Jenkins --> Managed files --> Add a new Config --> Global Maven settings.xml --> id

ssh to nexus vm 
```
sudo docker ps
```
```
docker exec -it container id /bin/bash
```
```
cat /nexus-data/admin.password
```

in nexus server -- settings -- repositories --> Deployment policy --> Allow redeploy

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
     

### Configure Nexus in `pom.xml`

Add the following `distributionManagement` configuration to your `pom.xml` file:

```
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



3. **Set Nexus environment variables in Jenkins pipeline:**
   ```groovy
   environment {
       NEXUS_USERNAME = credentials('nexus-cred').username
       NEXUS_PASSWORD = credentials('nexus-cred').password
   }
   ```


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

```
kubectl create ns webapps
```
```
vi ServiceAccount.yml
```
```
apiVersion: v1
kind: ServiceAccount
metadata:
  name: jenkins
  namespace: webapps
```

### Create Role 

```
vi role.yml
```
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
```
kubectl apply -f role.yml
```

### Bind the role to service account

```
vi rolebinding.yml
```
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
```
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
install kubectl in jenkins vm 


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




![image](https://github.com/user-attachments/assets/3c0835b9-e548-4b7a-9535-201caf606d6b)
