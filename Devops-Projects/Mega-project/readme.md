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

install plugins 

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

 







