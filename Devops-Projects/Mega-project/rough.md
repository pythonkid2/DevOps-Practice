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

pipeline syntax -->    Qubeenv --> 

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

 







