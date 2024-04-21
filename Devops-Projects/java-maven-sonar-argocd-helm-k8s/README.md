![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/66eb0f88-a4e3-4448-af7f-726a390477a7)

## Spring Boot Java Web Application Setup Guide

### Introduction
This guide walks you through setting up and running a simple Spring Boot Java web application locally. 

### Project Repository
Find the project repository [here](https://github.com/pythonkid2/Jenkins-Zero-To-Hero/tree/main/java-maven-sonar-argocd-helm-k8s).

### Prerequisites
- Git installed on your system.
- Java Development Kit (JDK) 11 or later.
- Apache Maven for building the application.
- Docker (optional).

### Step-by-Step Setup

1. **Clone the Repository**:
   
   ```
   git clone https://github.com/pythonkid2/Jenkins-Zero-To-Hero
   cd Jenkins-Zero-To-Hero/java-maven-sonar-argocd-helm-k8s/spring-boot-app
   ```

2. **Download and Install Apache Maven**:

   ```
   wget https://dlcdn.apache.org/maven/maven-3/3.9.6/binaries/apache-maven-3.9.6-bin.zip
   sudo apt install unzip -y && unzip apache-maven-3.9.6-bin.zip
   sudo mv apache-maven-3.9.6 /opt
   nano ~/.bashrc
   ```
   Add the following lines to the end of the file:
   ```
   export M2_HOME=/opt/apache-maven-3.9.6
   export PATH=$PATH:$M2_HOME/bin
   ```
   Then, apply the changes:
   ```
   source ~/.bashrc
   ```

3. **Verify Maven Installation**:

   ```
   mvn -version
   ```

4. **Build the Application**:

   ```
   mvn clean package
   ```

### Running Locally

- **Execute with Java** (Java 11 needed):

  ```
  java -jar target/spring-boot-web.jar
  ```

#### Jenkins setup

adding docker as agent, lesser configuration 

add docker pipeline plugin
add SonarQube Scanner




- **Run as Docker Container**:

  Build Docker Image:
  ```
  docker build -t ultimate-cicd-pipeline:v1 .
  ```
  Run Docker Container:
  ```
  docker run -d -p 8010:8080 -t ultimate-cicd-pipeline:v1
  ```
  Access the application at `http://<ip-address>:8010`.

### Next Steps

1. **Set Up SonarQube Locally**:

   - Download the latest version from [here](https://www.sonarsource.com/products/sonarqube/downloads/).
   - Extract and set permissions.
   - Start SonarQube server:
     ```
     ./sonar.sh start
     ```
   Access SonarQube at `http://<ip-address>:9000`.

```
apt install unzip
```
```
adduser sonarqube
su sonarqube
wget https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-10.4.1.88267.zip
unzip *
chmod -R 755 /home/sonarqube/sonarqube-10.5.0.89998
chown -R sonarqube:sonarqube /home/sonarqube/sonarqube-10.5.0.89998
cd sonarqube-10.5.0.89998/bin/linux-x86-64/
./sonar.sh start
```


2. **Generate SonarQube Token**:
   - Go to `My Account` > `Security` > `Generate Tokens`.

3. **Configure Credentials in Jenkins**:
   - Go to `Manage Jenkins` > `Credentials`.
   - Add SonarQube token and DockerHub credentials.

4. **Grant Docker Daemon Permissions**:
   ```
   sudo usermod -aG docker jenkins
   sudo usermod -aG docker ubuntu
   systemctl restart docker
   ```

5. **Restart Jenkins**:
   Access Jenkins at `http://<ec2-instance-public-ip>:8080/restart`.

## Argo cd

install k8 controlllers with operators, so operators makes intallation and conf easy 






---

