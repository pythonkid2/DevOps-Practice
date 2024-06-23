# Docker

alpine images are smaller in size

#### for permission -

sudo usermod -aG docker $USER

newgrp docker 

sudo chmod 666 /var/run/docker.sock  - not secure, everyone will have the permission 

to remove docker container
docker rm containerid 

remove image

docker rmi imageid

host port:container port


go inside -

docker exec -it id /bin/sh


# check
how to find running container size

docker ps --size

## Writing Dockerfile


## ECR

 sudo usermod -aG docker ubuntu
newgrp docker

# ECR
Elastic Container Registry --> Create a repository -->

namespace / repo name

in IAM 
create new user 
attach policies - AmazonEC2ContainerRegistryFullAccess 

security credentials ->access key


aws confidure

then got o Push commands for devops

![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/f45bdd22-99d3-451d-a142-f0a2b349b53a)

![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/2dd344d8-aa9f-4dfb-9544-2bbc80b176cf)


## Docker Network

Bridge is the default network , WHEN WE CREATING CONTAINER BY DEAFULT CONTAINER WILL GET CONNECTED TO THIS 
host - host mmachines network shared with docker container
none - 

docker network ls -sowing availble networks
![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/5b084b3c-bc09-4bb5-92d9-c0750c6ec238)
