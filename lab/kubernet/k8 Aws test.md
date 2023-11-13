
```markdown
# Setting Up a Kubernetes Cluster on Amazon Linux 2 Instances

## SSH into Your EC2 Instances

```bash
ssh -i your-key.pem ec2-user@your-ec2-instance-ip
```

## Set Hostnames

```bash
sudo su
hostnamectl set-hostname kmaster
hostnamectl set-hostname kworker1
hostnamectl set-hostname kworker2
```

Edit the `/etc/hosts` file:

```bash
vi /etc/hosts
```

Add the following lines:

```plaintext
private-ip    kmaster
private-ip    kworker1
private-ip    kworker2
```

## Update the System

```bash
sudo yum -y update
```

## Configure Kubernetes Yum Repository

```bash
sudo tee /etc/yum.repos.d/kubernetes.repo <<EOF
[kubernetes]
name=Kubernetes
baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-\$basearch
enabled=1
gpgcheck=1
gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
exclude=kubelet kubeadm kubectl
EOF
```

## Clean and Make Yum Cache

```bash
sudo yum clean all
sudo yum -y makecache
```

## Install Kubernetes Components

```bash
sudo yum -y install kubelet-1.23* kubeadm-1.23* kubectl-1.23* --disableexcludes=kubernetes
```

Check the installed version:

```bash
kubeadm version
```

## Disable SELinux

```bash
sudo sed -i 's/^SELINUX=.*/SELINUX=permissive/g' /etc/selinux/config
sudo setenforce 0
```

*Note: Disabling SELinux allows containers to easily access the host filesystem.*

## Disable Swap

```bash
sudo sed -i '/ swap / s/^\(.*\)$/#\1/g' /etc/fstab
sudo swapoff -a
```

## Load Kernel Modules

```bash
sudo modprobe overlay
sudo modprobe br_netfilter
```

## Configure Kernel Parameters

```bash
sudo tee /etc/sysctl.d/kubernetes.conf <<EOF
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
net.ipv4.ip_forward = 1
EOF
sudo sysctl --system
```

## Install Docker

```bash
sudo yum install docker -y
```

## Create Docker systemd Directory and Configuration

```bash
sudo mkdir -p /etc/systemd/system/docker.service.d
```

Create `/etc/docker/daemon.json`:

```bash
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

## Restart Docker

```bash
sudo systemctl restart docker
sudo systemctl enable docker
```

## Enable Docker and Kubernetes Services

```bash
sudo systemctl enable kubelet
```

**Only on the Master Node:**

## Initialize Kubernetes Cluster

```bash
sudo kubeadm init
```

Copy and paste the join commands in the worker nodes.

```
Certainly, I'll format the instructions for troubleshooting the join command and the remaining steps in a markdown file:

```markdown
# Troubleshoot Join Command and Complete Kubernetes Setup

### Troubleshoot Join Command

#### Generate Join Command on Master Node

Run the following command on your Kubernetes master node to generate a new token and obtain the complete kubeadm join command:

```bash
kubeadm token create --print-join-command
```

Copy the output, as it will include the correct token and SHA-256 hash of the CA certificate.

#### Join Worker Nodes

On each worker node, execute the following command with the token and CA certificate hash obtained from the master:

```bash
kubeadm join 172.31.31.177:6443 --token <valid_token> --discovery-token-ca-cert-hash <valid_sha256_hash>
```

---

### Continue Setup on Master Node

17. **Set Up kubectl for Your User:**

```bash
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

18. **Install a CNI (Container Network Interface):**

```bash
kubectl apply -f https://github.com/weaveworks/weave/releases/download/v2.8.1/weave-daemonset-k8s.yaml
```

19. **Monitor Pod Creation in kube-system Namespace:**

```bash
watch -n 1 kubectl get pod -n kube-system
```

20. **Run an Nginx Pod:**

```bash
kubectl run nginx --image=nginx
```

21. **Check the Status of the Nginx Pod:**

```bash
kubectl get pods
kubectl get pods -o wide
```

22. **Access Kubernetes API Server:**

```bash
curl http://10.96.0.1
```

23. **Access the Nginx Pod:**

```bash
kubectl get svc
```

Identify the ClusterIP of the Nginx service and use it to access Nginx:

```bash
curl http://<ClusterIP>
```

### Additional Command:

- **Delete All Pods:**

```bash
kubectl delete pod --all
```




