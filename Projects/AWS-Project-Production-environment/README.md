This example demonstrates **how to create a VPC that you can use for servers in a production environment.**

To improve resiliency, you deploy the servers in two Availability Zones, by using an Auto Scaling group and an Application Load Balancer. For additional security,you deploy the servers in private subnets. The servers receive requests through the load balancer. The servers can connect to the internet by using a NAT gateway. To improve resiliency, you deploy the NAT gateway in both Availability Zones.

![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/b97addca-f1d3-4b16-90db-4bad8ce273ee)

![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/baec8d16-a40a-4875-9c4e-153eed84ffc7)

VPC --> Your VPCs --> Create VPC --> 

![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/d7a88da9-9f5b-4121-ab56-2e25d370876d)

![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/ecb945ef-8e5f-4a00-b664-0cee9645d859)

![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/84517b87-1623-4a2f-9399-b8496fc65337)

### Auto scaling groups 

EC2 --> Launch templates --> Create launch template

EC2 --> Auto Scaling groups --> Create Auto Scaling group

![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/66c99847-9bb9-4e92-816f-0681e9eea13a)


These instance has no public ip so need to use jumphost/bastion server 

jump server on same vpc, security grp should have ssh accessabiliy 

scp and copy paste pem key tothe jump server 

```
scp -i "x.pem" x.pem  ubuntu@ec2-18-191-237-225.us-east-2.compute.amazonaws.com:/home/ubuntu
```

login to server 

take private ip and ssh

create index.html

run using 
```
python3 -m http.server 8000
```

### EC2 --> Load balancers --> Create Application Load Balancer -->

load balacer shuld be in public subnet and should have access to ig


Listeners and routing Info - A listener is a process that checks for connection requests using the port and protocol you configure. The rules that you define for a listener determine how the load balancer routes requests to its registered targets.

include as pending -




