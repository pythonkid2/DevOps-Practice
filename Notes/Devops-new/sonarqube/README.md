
docker run -d --name sonar -p 9000:9000 sonarqube:lts-community

comminty branch - https://hub.docker.com/r/mc1arke/sonarqube-with-community-branch-plugin

![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/c0ffd9f8-cd13-41c3-a51b-02598e46470e)

Configuration - configuration of sq
Security - user management
Projects - Project management 
System - to check the status
Marketplace  - to install plugins and all

Quality profile 

we can add and modify the rules anfter taking a copy

jacoco is using for java

url and usr/password required for access any 

install sonaqube scanner plugin in jenkins

go to tools in jenkins 
![jenkins tools](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/b07d9eba-11ae-42da-adc9-76ba852c9f4e)

![system-sonar server](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/53f054ae-a783-483c-95fc-0d4635d0f43d)

![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/341dd4e5-81a1-4f2d-94c0-60c369c3d2fa)

Administration --> security --> user --> token -->

Manage Jenkins --> Credentials --> System --> Global credentials (unrestricted) --> New credentials

kind : secret text
Scope : Global (Jenkins, nodes, items, all child items, etc)
Secret : Token
ID: sonar-token
Description : sonar-token 

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
        stage('git') {
            steps {
                echo 'git checkout'
                git branch: 'main', url: 'https://github.com/pythonkid2/Boardgame.git'
            }
        }
        stage('unit test') {
            steps {
                echo 'mvn test'
                sh 'mvn test'
            }
        }
        stage('sonar analysis') {
            steps {
                withSonarQubeEnv('sonar-server') {
                    sh '''$SCANNER_HOME/bin/sonar-scanner -Dsonar.projectName=BoardGame -Dsonar.projectKey=BoardGame \
                    -Dsonar.java.binaries=target'''
                }
            }
        }
        stage('package') {
            steps {
                echo 'mvn package'
                sh 'mvn package'
            }
        }       
    }
}

```

+++

community branch pluggin -


mc1arke/sonarqube-community-branch-plugin
https://github.com/mc1arke/sonarqube-community-branch-plugin

https://hub.docker.com/r/mc1arke/sonarqube-with-community-branch-plugin


## instal jar manually 

1. **Access the SonarQube container:**
```
   docker exec -it 2710 /bin/bash
   ```

2. **Navigate to the `extensions/plugins` directory:**
   ```
   cd /opt/sonarqube/extensions/plugins
   ```

3. **Download the SonarQube Community Branch Plugin:**
   ```
   wget https://github.com/mc1arke/sonarqube-community-branch-plugin/releases/download/1.16.0/sonarqube-community-branch-plugin-1.16.0.jar
   ```
exit and restart the container 
docker restart 

## Sonar trouble shoot

![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/2141938d-e9cb-4b99-a08e-d2af5f533721)


## Branch change
![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/0d0a1301-1e31-4a99-bccf-482ccc0e545f)


plugin version matrix - to check the supported versions 
