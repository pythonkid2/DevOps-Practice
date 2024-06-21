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
