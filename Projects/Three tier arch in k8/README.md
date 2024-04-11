# Link to [three-tier-architecture-project](https://github.com/pythonkid2/three-tier-architecture-project)


![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/14602056-dace-44c5-bdbe-951e1c84c077)

![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/b1f8621f-5c08-464c-b5c1-bfe037c00af5)

![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/e8dd9860-3249-4ad5-ba27-319074699eb6)\

![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/9161d725-7356-4090-94cd-93645ad4ea19)
6 micro services 1 in memory datat store, 2 data bases


# Install EKS

## Install using Fargate

```
eksctl create cluster --name demo-cluster-three-tier-1 --region us-east-1
```

## Delete the cluster

```
eksctl delete cluster --name demo-cluster-three-tier-1 --region us-east-1
```

IAM OIDC (OpenID Connect) provider in AWS (Amazon Web Services) Identity and Access Management (IAM) is a service that allows you to integrate IAM with identity providers supporting the OpenID Connect protocol. With IAM OIDC provider, you can establish a trust relationship between your AWS account and an external identity provider, enabling you to use IAM roles to manage permissions for users authenticated by that identity provider.

Here's how it works:

1. **Configuration**: You configure an IAM OIDC provider in your AWS account by specifying the issuer URL provided by the identity provider. This establishes trust between AWS IAM and the external identity provider.

2. **Authentication**: When a user tries to access AWS resources, they authenticate with the external identity provider. Upon successful authentication, the identity provider issues an ID token to the user.

3. **Authorization**: The user presents the ID token to AWS. IAM OIDC provider validates the token with the identity provider to ensure its authenticity.

4. **Role Mapping**: IAM roles are configured with trust policies that specify the IAM OIDC provider as a trusted entity. When the token is validated, IAM retrieves the associated IAM role based on the attributes provided in the token, such as groups or roles.

5. **Temporary Credentials**: If the authentication and authorization process succeeds, IAM issues temporary security credentials to the user. These credentials grant access to AWS resources according to the permissions defined in the IAM roles mapped to the user.

By using IAM OIDC provider, you can manage access to AWS resources centrally, streamline authentication with external identity providers, and enforce fine-grained access controls using IAM roles and policies.

![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/a9098c56-3697-4642-91b8-d882cdc7c59f)

# commands to configure IAM OIDC provider 

```
export cluster_name=<CLUSTER-NAME>
```
```
export cluster_name=demo-cluster-three-tier-1
```

```
oidc_id=$(aws eks describe-cluster --name $cluster_name --query "cluster.identity.oidc.issuer" --output text | cut -d '/' -f 5) 
```

## Check if there is an IAM OIDC provider configured already

```
aws iam list-open-id-connect-providers | grep $oidc_id | cut -d "/" -f4
```

If not, run the below command

```
eksctl utils associate-iam-oidc-provider --cluster $cluster_name --approve
```
+++

# How to setup alb add on

Download IAM policy

```
curl -O https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/v2.5.4/docs/install/iam_policy.json
```

Create IAM Policy

```
aws iam create-policy \
    --policy-name AWSLoadBalancerControllerIAMPolicy \
    --policy-document file://iam_policy.json
```

Create IAM Role

```
eksctl create iamserviceaccount \
  --cluster=<your-cluster-name> \
  --namespace=kube-system \
  --name=aws-load-balancer-controller \
  --role-name AmazonEKSLoadBalancerControllerRole \
  --attach-policy-arn=arn:aws:iam::<your-aws-account-id>:policy/AWSLoadBalancerControllerIAMPolicy \
  --approve
```

## Deploy ALB controller

install Helm through operating system package managers.

```
curl https://baltocdn.com/helm/signing.asc | gpg --dearmor | sudo tee /usr/share/keyrings/helm.gpg > /dev/null
sudo apt-get install apt-transport-https --yes
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/helm.gpg] https://baltocdn.com/helm/stable/debian/ all main" | sudo tee /etc/apt/sources.list.d/helm-stable-debian.list
sudo apt-get update
sudo apt-get install helm
```

Add helm repo

```
helm repo add eks https://aws.github.io/eks-charts
```

Update the repo

```
helm repo update eks
```

Install

```
helm install aws-load-balancer-controller eks/aws-load-balancer-controller \            
  --namespace kube-system \
  --set clusterName=<your-cluster-name> \
  --set serviceAccount.create=false \
  --set serviceAccount.name=aws-load-balancer-controller \
  --set region=<region> \
  --set vpcId=<your-vpc-id>
```

Verify that the deployments are running.

```
kubectl get deployment -n kube-system aws-load-balancer-controller
```


# EBS CSI Plugin configuration

The Amazon EBS CSI plugin requires IAM permissions to make calls to AWS APIs on your behalf.

Create an IAM role and attach a policy. AWS maintains an AWS managed policy or you can create your own custom policy. You can create an IAM role and attach the AWS managed policy with the following command. Replace my-cluster with the name of your cluster. The command deploys an AWS CloudFormation stack that creates an IAM role and attaches the IAM policy to it. 

```
eksctl create iamserviceaccount \
    --name ebs-csi-controller-sa \
    --namespace kube-system \
    --cluster <YOUR-CLUSTER-NAME> \
    --role-name AmazonEKS_EBS_CSI_DriverRole \
    --role-only \
    --attach-policy-arn arn:aws:iam::aws:policy/service-role/AmazonEBSCSIDriverPolicy \
    --approve
```

Run the following command. Replace <AWS-ACCOUNT-ID> with the name of your cluster, <AWS-ACCOUNT-ID> with your account ID.

```
eksctl create addon --name aws-ebs-csi-driver --cluster <YOUR-CLUSTER-NAME> --service-account-role-arn arn:aws:iam::<AWS-ACCOUNT-ID>:role/AmazonEKS_EBS_CSI_DriverRole --force
```

**Note**: If your cluster is in the AWS GovCloud (US-East) or AWS GovCloud (US-West) AWS Regions, then replace arn:aws: with arn:aws-us-gov:.

**References**:
https://repost.aws/knowledge-center/eks-persistent-storage


+++
go to helm and deploy 

kubectl get pods -n robot-shop
kubectl apply -f ingress.yaml

kubectl get ingress -n robot-shop
