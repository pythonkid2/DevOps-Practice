# K8

k8 - developed by google
now under cncf(cloud native computing foundation)

open sourse platform using to orchastrate containers


stopped pod will restart 
recreating 
probes 

liveness probe - need to setup time (example 10s, so k8 will check every 10 sec its running or not)
readiness probe - checking the app is ready or not, wheter app is apble to accepet the requests
![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/7a522c01-24a9-41b9-9773-52727e3da74c)

k8 can manage load 
automate deployment


## Archetecture 

![K8 Archetecture](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/ac93a0a6-0b6b-4b70-b93e-eb5e76001981)



Master 

Api server - cluster gateway(request is goiung firt to api server , and it will decide next )
ETCD - (cluster brain, it store every kind of info about the cluster in key value format)
Scheduler - (where we need to create pod, these kind of decision is done by scheduler)
Controller manager - detetects the state changes(ex-pod is down)


Worker 

Kubelet - creation os pods done by this and monitoring 
Kubeproxy - networking is managing by kube proxy
container runtime - conatainer creation and management 


## work flow 

request --> api server (storing in etcd)-->scheduler (finding suitable worker node) --> scheduler update info to etcd --> kubelet (ceating the pod --> kube proxy enable network rules for this pod 

controller will detect i something went wrong --> inform the scheduler 

## components of k8


