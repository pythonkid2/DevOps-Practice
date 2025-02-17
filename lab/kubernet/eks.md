# EKS

![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/73530670-c8c5-4228-9ec3-45e42b831ee1)
![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/528ede28-caa8-4769-a6c2-e883cb9bcd71)
![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/3526b2bd-7375-467a-b57d-10e487650c9f)
![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/0b78a999-1989-4894-b08a-1533a96d34c8)


## To install or upgrade eksctl on Linux using curl

**[Click here](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/setting-up-eksctl.html)**

```
eksctl version
```

## Install and Set Up kubectl on Linux

**[Click here](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/)**
```
sudo snap install kubectl --classic
```
```
kubectl version --client
```
## Install or update to the latest version of the AWS CLI

**[Click here](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)**
```
sudo snap install aws-cli --classic
```
```
aws configure
```
(go to IAM --> Security credentials)

Default region name [None]: us-east-2
Default output format [None]: JSON

```
eksctl create cluster --name eks-cluster --region us-east-2 --nodegroup-name linux-nodes --node-type t2.medium --nodes 1 --ssh-access --ssh-public-key ohiokey
```

**To temporarily stop and restart an Amazon EKS cluster**, you can use the following commands:

1. To stop the cluster:
   ```
   eksctl delete cluster --name eks-cluster
   ```

2. To restart the cluster:
   ```
   eksctl create cluster --name eks-cluster --region us-east-2 --nodegroup-name linux-nodes --node-type t2.medium --nodes 1 --ssh-access --ssh-public-key ohiokey
   ```

**for restart** -

```
aws eks update-kubeconfig --name eks-cluster
```

**To remove** 

```
eksctl delete cluster --name eks-cluster --region us-east-2
```
