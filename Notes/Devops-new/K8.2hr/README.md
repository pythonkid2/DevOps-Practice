https://github.com/jaiswaladi246/K8-Master/blob/main/Direct-Deploy/Explain.md

![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/4c1192de-211e-4c65-95e4-d3d8683ca2a6)

Pod is the smallest usint in k8

![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/85f045f4-8c80-41ea-9c0b-f093b752c521)

for communicating we have svc , svc ip wont change 

![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/33b6b335-4e2f-4d68-937e-86c3f95be3c3)


secrets are using to store confidential data , like passwords

configmap is storing info like urls 

![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/079bcd56-ec4c-4f0c-ac73-335bd2c55ab0)

persistent volume - defining some amount of storage, for 

pvc - used to conect to pv
![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/d45d8fa7-4bda-4305-bcb8-8ca41b03d9b2)



clusterip- by default it will create for internal communication 
nodeport- 
load balancer- external url will generate 
Ingress - https

https://github.com/jaiswaladi246/K8-Master/blob/main/Direct-Deploy/Explain.md


encoding data to save in secrets
![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/9d1531e7-b9e0-4c59-baf6-a5c3bcd331bd)


RBAC
user- service account
role - group of permission 
assigning the role to the user

binding the role to service account RoleBinding


Namespaces


apply vs create - create can be used only for the first time
apply can be use update and create


jenkins-

pluging kubernetes kubernetes cli , kubernetes pipeline, kubernetes credential provier




