problem -The connection to the server 172.31.21.140:6443 was refused - did you specify the right host or port?

Solution -

sudo -i && swapoff -a && exit

https://docs.tigera.io/calico/latest/getting-started/kubernetes/self-managed-onprem/onpremises#install-calico-with-kubernetes-api-datastore-50-nodes-or-less

kubeadm init --apiserver-advertise-address=172.31.28.13  --pod-network-cidr=192.168.0.0/16
![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/8fd307f8-95f3-40bf-b557-4a25e472ebc4)
