
https://github.com/vilasvarghese/docker-k8s/blob/master/cicd/centos-instruction.txt

++++
Number of instances :3
amazon linux 2 ami

t3a.medium

1. SSH into your EC2 instance:
   ssh -i your-key.pem ec2-user@your-ec2-instance-ip

2. Set the hostname:
```
sudo su
```
```
hostnamectl set-hostname kmaster
```
```
hostnamectl set-hostname kworker1
```
```
hostnamectl set-hostname kworker2
```
go to security group and configure **all trafic** for he security group
```
vi /etc/hosts
```
```
ip a
```
```
private-ip	kmaster 
private-ip	kworker1 
private-ip	kworker2
```
3. Update the system:

sudo yum -y update

4. Configure the Kubernetes Yum repository:
```
cat <<EOF | sudo tee /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-\$basearch
enabled=1
gpgcheck=1
gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
exclude=kubelet kubeadm kubectl
EOF
```
5. Clean Yum cache:
```
sudo yum clean all
```
6. Make Yum cache:
```
sudo yum -y makecache
```
7. Install Kubernetes components:
```
sudo yum -y install kubelet-1.23* kubeadm-1.23* kubectl-1.23* --disableexcludes=kubernetes
```
kubeadm  version

8. Disable SELinux:
```
sudo sed -i 's/^SELINUX=.*/SELINUX=permissive/g' /etc/selinux/config
sudo setenforce 0
```
why?
	By Disabling the SElinux all containers can easily access host filesystem
	But in production it is recommended to work with selinux
		that requires lot of system file updates
		More details: https://dev.to/carminezacc/does-kubernetes-support-selinux-3oop

9. Disable Swap:
```
sudo sed -i '/ swap / s/^\(.*\)$/#\1/g' /etc/fstab
sudo swapoff -a
```

10. Load Kernel Modules:
 ```
sudo modprobe overlay
sudo modprobe br_netfilter 
 ```
11. Configure Kernel Parameters:

```
sudo tee /etc/sysctl.d/kubernetes.conf<<EOF

net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
net.ipv4.ip_forward = 1
EOF
```
```
sudo sysctl --system

```

12. Install Docker:
```
sudo yum install docker -y
```
13. Create Docker systemd directory and configuration:

check - 
	ls /etc/docker
```
sudo mkdir -p /etc/systemd/system/docker.service.d
```
```
sudo tee /etc/docker/daemon.json <<EOF
{
  "exec-opts": ["native.cgroupdriver=systemd"],
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "100m" 
  },
  "storage-driver": "overlay2"
}
EOF
``` 
 

14. Restart Docker:
```
sudo systemctl restart docker
sudo systemctl enable docker
```

15. Enable Docker and Kubernetes services:

 ```
sudo systemctl enable kubelet
```
#systemctl start docker.service


**Only on master -**

16. Initialize Kubernetes cluster:
```
sudo kubeadm init
```

copy and paste join commands in both worker -


master ----

---
troubleshoot for join command -

tocken format -


kubeadm token create --print-join-command

	When you run this command on your Kubernetes master node, it will generate a new token and provide you with the complete kubeadm join command, including the correct token and SHA-256 hash of the CA certificate. You can then use this command on your worker nodes to join them to the Kubernetes cluster.


kubeadm join 172.31.31.177:6443 --token <valid_token> --discovery-token-ca-cert-hash <valid_sha256_hash>

---



17. Set up kubectl for your user:
    
```	
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

18. Install a CNI (Container Network Interface):
```
kubectl apply -f https://github.com/weaveworks/weave/releases/download/v2.8.1/weave-daemonset-k8s.yaml
```
19. Monitor pod creation in kube-system namespace:
```
    watch -n 1 kubectl get pod -n kube-system
```
21. Run an Nginx pod:
```
    kubectl run nginx --image=nginx
```
22. Check the status of the Nginx pod:
    ```
    kubectl get pods
    ```
```
kubectl get pods -o wide
```
22. Access Kubernetes API server: 
    curl http://10.96.0.1

23. Access the service:
```
    kubectl get svc
```
    Identify the ClusterIP of the Nginx service and use it to access Nginx:
    curl http://<ClusterIP>

```
 kubectl delete pod --all
```



