Jenkins plugins are on hpi extension 

basic plugins -

pipeline stage view - ui for seeing 
Eclipse Temurin installer

option to keep builds 

![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/46aa5155-4aeb-47f6-aa63-d94603aca8dc)


```
pipeline 
{
    agent any
    tools {
        maven 'M3'   
    }
    stages {
        stage('git') {
            steps {
                echo 'git checkput'
                git branch: 'main', url: 'https://github.com/jaiswaladi246/Boardgame.git'
            }
        }
        stage('unit test') {
            steps {
                echo 'mvn test'
                sh 'mvn test'
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

# Triggers

Basic triger - applying on master/main
Generic webhook trigger - 

go to build triggers --> generic webhhok Trigger 

![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/ccfb4510-c501-4049-b55e-157f8a1c5c4c)


multibranch scan webhook - whenevere we push 
