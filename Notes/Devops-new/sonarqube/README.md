
docker run -d --name sonar -p 9000:9000 sonarqube:lts-community

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
                git branch: 'main', url: 'https://github.com/jaiswaladi246/Boardgame.git'
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

