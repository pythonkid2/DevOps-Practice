# CICD Corporate DevOps Pipeline Project

### [Link to the project]()
![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/7bfbef79-1a3c-4813-942e-c6644dd60506)
![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/8b4b744d-92b1-4e39-93fc-f2f30ca7e4da)

![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/b99eaa85-134a-4af8-ad0f-0bef75c64191)


## Kubeaudit setup

wget https://github.com/Shopify/kubeaudit/releases/download/v0.22.1/kubeaudit_0.22.1_linux_amd64.tar.gz

tar -xzvf kubeaudit_0.22.1_linux_amd64.tar.gz


sudo mv kubeaudit /usr/local/bin/
kubeaudit all


##

Sonar server 
install docker

```
docker run -d --name sonar -p 9000:9000 sonarqube:lts-community
```
## nexus server 
```
docker run -d --name nexus -p 8081:8081 sonatype/nexus3
```
http://ip:8081/

usename :admin 
password: 
Your admin user password is located in /nexus-data/admin.password on the server.

docker exec -it 2eaadd3a /bin/bash

cat sonatype-work/nexus3/admin.password
Enable anonymous access

## Jenkins Server

install jenkins
install docker

# phase 2
![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/3ae33389-63f7-46ca-9e7c-435d5f7e1468)

git repo creaed

# phase 3
![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/fafd9d2e-4d62-45a2-9257-3e2cc91c3c1f)

jenkins required plugins

Eclipse Temurin installerVersion
1.5
Provides an installer for the JDK tool that downloads the JDK from https://adoptium.net

Config File ProviderVersion
968.ve1ca_eb_913f8c


Pipeline Maven IntegrationVersion
1396.veb_f07b_2fc1d8

SonarQube ScannerVersion   - tool which is analysing and publsh report in server
2.17.2
External Site/Tool Integrations 

DockerVersion
1.6

Docker PipelineVersion
572.v950f58993843

KubernetesVersion
4203.v1dd44f5b_1cf9

Kubernetes CLIVersion
1.12.1
kubernetes

Kubernetes CredentialsVersion
0.11

	
Kubernetes Client APIVersion
6.10.0-240.v57880ce8b_0b_2

Maven IntegrationVersion
3.23

#### [Link to the video](https://www.youtube.com/watch?v=NnkUGzaqqOc&t=75s)

