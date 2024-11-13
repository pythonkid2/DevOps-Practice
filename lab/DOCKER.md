#### for permission -
sudo usermod -aG docker $USER
newgrp docker 


## Jenkins

```
docker volume create jenkins_data
```
```
docker run -d -p 8080:8080 \
   --name jenkins \
   -v jenkins_data:/var/jenkins_home \
   jenkins/jenkins:lts
```
