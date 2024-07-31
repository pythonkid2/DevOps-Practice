# Ultimate Corporate DevOps Pipeline Project

Create 1 st vm, infra server -

install aws cli for connecting with aws

- run aws configure
-  create credentials(access keys)
## Install terraform

sudo snap install terraform --classic
- create directory as eks
```
mkdir eks
cd eks
```
create -

main.tf
varible.tf
output.tf
![output.tf](https://github.com/user-attachments/assets/6931ddec-10b2-4c60-ab0c-887983c3526c)

terraform init
terraform plan 
terraform apply --auto-approve for eks cluster setup

+++

ssh-keygen

terraform apply --var-file='terraform.tfvars'



-  

create 4 machines
jenkins master slave - t2.medium
sonar and nexus 

## Jenkis Master
install java
install jenkins 
install docker
sudo usermod -aG docker ubuntu


install plugins (video 35:00)

sonarqbe scanner
config file provider
pipeline maven itegration
maven integration
docker
dockerpipeline
pipelinbe:stageview
kubernetes
kubernetes cli

Tools

Docker installation
Maven 
sonarqube 
scaner name : sonar-scanner

Pipeline

Discard old build , 2

```
pipeline 
{
    agent any
    tools {
        maven 'M3'   
    }
    environment {
        SCANNER_HOME= tool 'sonar-scanner'
    }
```
configure tool in jenkins 


```
    stages {
        stage('git') {
            steps {
                echo 'git checkput'
                git branch: 'main', url: 'https://github.com/jaiswaladi246/Boardgame.git'
            }
        }
```
add credentilas if the repo is private 

kind: username and password(create token as password) 


```
        stage('compile') {
            steps {
                sh 'mvn compile'
            }
        }
```

doing for find any sytax based error 

```
        stage('Unit Testing') {
            steps {
                echo 'mvn test'
                sh 'mvn test'
            }
        }
```

```
        stage('Trivy FS Scan') {
            steps {
                echo 'mvn package'
                sh 'trivy fs --format table -o fs-report.html .'
            }
        }
```
install trivy in vm 

https://aquasecurity.github.io/trivy/v0.18.3/installation/

```

        stage('sonarqube analysis') {
            steps {
                withSonarQubeEnv('sonar'){
                    sh ''' $SCANNER_HOME/bin/sonar-scanner -Dsonar.projectkey= TaskMaster \ -Dsonar.projectName=TaskMaster -Dsonar.java.binaries=target '''                
            }
        }

```
set sonar environemnt 

pipeline syntax -->  withSonarQubeEnv: Prepare SonarQube Scanner environment --> 

sonarqube server configuration - 

administartion --> security --> user --> provide name and generate token

manage jenkins --> credential -->secret text -->id sonar-token

manage jenkins --> system --> sonarQube instalations --> name , server url, authentication token



```
        stage('publish to nexus') {
            steps {
                withMaven(globalMavenSettingsConfig: 'settings', jdk:",maven: 'maven3', mavenSettingsConfig:",traceability:true){
               sh 'deploy'
            }
        }    
```    

need to add url of nexus server to pom.xml file (after the buld)

go to nexus server --> Browse --> maven-releases and snapshot


  <distributionManagement>
      <repository>
      <id>repo-id2</id>
      <name>my repository</name>
      <url>file:///path/to/repo</url>
      </repository>
      <snapshotRepository>
      <id>repo-id</id>
      <name>my snapshot repository</name>
      <url>file:///path/to/snapshot/repo</url>
    </snapshotRepository>
    
  </distributionManagement>
 

as we installed config file provider we have 

manage jenkins --> manage files --> add new config --> global maven settings.xml --> id (settings)

find servers

 <server>
     <id>rmaven-releases</id>
     <usename>repo usename (admin)</usename>
     <password>repo password</password>
</server>



+++
use pipeline syntax

find withmaven: provide maven environment

select maven 

select --> global maven setting config

generate 
+++

```
stage('Build & Tag Docker') {
            steps {
script{
                withDockerRegistry(credentialID: 'docker-cred', toolname: 'docker'){
                    sh 'docker build -t username/taskmaster:latest .'
            }
        }    


pipeline syntax --> wiith docker registery --> credentials setup docker hub username and password


+++

stage('scan docker image By Trivy') {
            steps {
                echo 'mvn package'
                sh 'trivy image --format table -o image-report.html username/imagename:tag'
            }
        }    

stage('push docker image ') {
            steps {
                script{
                withDockerRegistry(credentialID: 'docker-cred', toolname: 'docker'){
                    sh 'docker push push username/imagename:tag'
            }
            }
        }    


stage('Build app') {
            steps {
                echo 'mvn package'
                sh 'mvn package'
            }
        }    

```





# sonar 
docker install
sudo usermod -aG docker ubuntu

docker run -d --name sonar -p 9000:9000 sonarqube:lts-community

## nexus 

docker run -d --name nexus -p 8081:8081 sonatype/nexus3

docker exec -it c-id /bin/bash

# EKS

on server - install kubectl

aws eks --region [region name] update-kubeconfig --name (cluster name)

 

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

