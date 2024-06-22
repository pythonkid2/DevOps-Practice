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



## Docker Network

Bridge is the defaiult network 


host - host mmachines network shared with docker container
none - 

docker network ls -sowing availble networks
![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/5b084b3c-bc09-4bb5-92d9-c0750c6ec238)
