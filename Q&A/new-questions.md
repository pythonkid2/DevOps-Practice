---

# DevOps Interview Question Bank (Categorized)

---

# CI/CD (Jenkins, Git, Pipelines)

## Questions

* How did you design a production pipeline?
* How do you handle rollbacks?
* How do you secure Jenkins in enterprise setups?
* How did you integrate Jenkins with Docker, Kubernetes, and AWS?
* Explain your end-to-end CI/CD workflow.
* Which type of Jenkins pipeline do you use and why?
* Difference between Declarative and Scripted Jenkins pipelines.
* How do you define and trigger Jenkins pipelines?
* What are Jenkins Shared Libraries? How are they structured and used?
* What types of applications have you deployed using Jenkins pipelines?
* Which deployment tools have you used (Docker, Kubernetes, Helm, Terraform)?
* If a Jenkins pipeline runs but the build does not trigger, what could be the reasons?
* What is a webhook and how is it used in CI/CD?
* What stages do you define in Jenkins pipelines for code quality?
* How do you design and reuse Jenkins Shared Libraries?
* What types of pipeline failures have you encountered?
* How do you troubleshoot CI/CD pipeline failures?
* How do you integrate/deploy an Angular app using Jenkins?
* Can you write a basic Jenkins pipeline script?
* What is CI/CD and why is it important?
* What branching strategy do you follow (GitFlow / Trunk-based)?
* How do you avoid breaking the release branch?
* If a critical bug is found in production, how do you handle it?
* Explain complete deployment workflow from commit to production.

---

# Docker

## Questions

* What real problems did Docker solve in your environment?
* What are the stages involved in building a Docker image?
* What is the Docker container lifecycle?
* How do you optimize Docker images?
* How do you handle Docker image security?
* How do you manage images in ECR?
* How do you perform image vulnerability scanning?
* Which tools have you used for image scanning?
* How do you pass environment variables during Docker build and runtime?
* What is the difference between ENTRYPOINT and CMD?
* What is the purpose of docker tag?
* What command is used to build a Docker image?
* Which container registries have you used?

---

# Kubernetes

## Questions

* Describe a real production issue you handled in Kubernetes.
* What common Kubernetes errors have you faced and how did you resolve them?
* How do you troubleshoot CrashLoopBackOff?
* How do you design HA and autoscaling in Kubernetes?
* Explain Kubernetes architecture.
* What are components of master (control plane) and worker nodes?
* What is the role of kubelet?
* What happens when a pod crashes repeatedly?
* What happens if kubelet cannot recreate a pod?
* What controllers exist in Kubernetes?
* What does controller manager manage?
* Can ETCD get corrupted? How do you handle it?
* Can ETCD run in HA mode?
* How do you set up a Kubernetes cluster from scratch?
* How do you create an ingress controller in AWS EKS?
* How do you manage SSL certificates in Kubernetes/EKS?
* What is the best option for SSL in EKS?
* How do you upgrade an EKS cluster?
* Do you upgrade nodes in-place or create new node groups?
* Deployment vs StatefulSet — when and why?
* ReplicaSet vs Deployment?
* What is a DaemonSet? Give examples.
* How do you troubleshoot DaemonSet pod pending?
* What are Kubernetes service types?
* Which service type is used in production?
* How do you access a running pod?
* How do you define Kubernetes objects?
* How do you write a Kubernetes Deployment YAML?
* How do you write a Kubernetes Service YAML?
* How do you write a CronJob in Kubernetes?
* What is Role vs ClusterRole vs RoleBinding?
* If a pod is in Pending state, how do you troubleshoot?
* Can you get logs from a Pending pod?
* If node is out of capacity, what will you do?
* How do you troubleshoot service not accessible?
* How do you handle OOMKilled pods?
* What happens if ConfigMap updates are not reflected?
* How do you troubleshoot cluster performance issues?
* How do you implement zero downtime deployment?
* What happens if database pod is deleted?

---

# AWS & Cloud

## Questions

* How do you design highly available systems?
* Multi-AZ vs Multi-Region — when to use each?
* How do you enforce least-privilege IAM?
* How do you design disaster recovery?
* What is IAM and how do you assign permissions?
* How do you ensure correct IAM permissions?
* What is IAM Access Analyzer?
* What is EBS and its use cases?
* What is a Snapshot and how is it different from backup?
* What is an AMI?
* What are EC2 instance types and when to use them?
* Explain S3 storage classes.
* How do you write S3 lifecycle policy?
* How do you secure S3 bucket?
* What is a VPC?
* Public vs Private subnet?
* How do you make a subnet public or private?
* What is IGW and NAT Gateway?
* What ports are used for HTTP/HTTPS?
* Are Security Groups stateful or stateless?
* How do you design a 3-tier architecture?
* Can S3 be attached to EC2?
* What is the maximum object size in S3?
* Is there a limit on S3 bucket size?
* What is Lambda max runtime?
* What are common Lambda issues (cold start)?
* How do you troubleshoot RDS high CPU?
* What is EKS vs ECS?
* How do you transfer data to S3 apart from copy command?
* How do you establish secure DB connections?
* How do you authenticate to EKS and manage secrets?
* How do you create and deploy AWS Lambda?
* What are ways to push artifacts to Lambda?

---

# Terraform

## Questions

* What is Terraform and how does it work?
* What are important Terraform concepts?
* Explain Terraform modules.
* How do you pass values to Terraform modules?
* What are Terraform dependencies?
* What is terraform init, plan, apply?
* What is terraform taint vs untaint?
* What is terraform refresh?
* How do you store Terraform state remotely?
* How do you view Terraform state?
* How do you secure Terraform state file?
* How do you avoid exposing sensitive values?
* How do you handle secrets in Terraform?
* How do you avoid hardcoding values?
* How do you import existing infrastructure?
* How do you create Kubernetes cluster using Terraform?
* How do you configure Security Groups using Terraform?
* What happens if Terraform remote backend fails?

---

# Networking

## Questions

* What is a CIDR block?
* What is the difference between public and private subnet?
* How do you design CIDR blocks for VPC and subnets?
* How do you check DNS entry in a system?

---

# Linux

## Questions

* What are common Linux commands you use daily?
* How do you find a file with specific size?
* How do you search file by name?
* How do you change file permissions?
* Explain grep use cases.
* Explain ls command options.
* If you install Nginx, which config file do you modify?

---

# Monitoring & Troubleshooting

## Questions

* Explain Prometheus architecture and components.
* If an application becomes unresponsive, how do you troubleshoot?
* How do you troubleshoot production incidents?
* How do you troubleshoot Kubernetes issues systematically?

---

# Advanced / System Design / Chaos Engineering

## Questions

* How do you implement service discovery using Istio/Envoy at scale?
* How do you use eBPF + Cilium for network security?
* How do you design multi-cloud routing, IAM, and secrets?
* How do you handle systemd failures on EKS nodes?
* How do you validate custom AMIs before production?
* How do you design advanced health probes beyond HTTP checks?
* How do you handle DNS outages inside service mesh?
* What will you do if Terraform remote state backend times out?
* How do you debug mTLS failures in service mesh?
* Why would HPA not scale even if CPU is high?
* How do you debug latency spikes after introducing sidecars?
* How do you troubleshoot 504 errors in distributed systems?
* What could cause sudden NAT Gateway cost spikes?

---

# Scenario-Based / RCA Questions

## Questions

* Pod in CrashLoopBackOff — how do you debug?
* Service not accessible — how do you debug?
* Node NotReady — how do you troubleshoot?
* Pods getting OOMKilled — how do you fix?
* Deployment failed — how do you rollback?
* Pod stuck in Pending — what are reasons?
* ConfigMap updated but not reflected — why?
* Cluster performance degraded — how do you analyze?
* Database pod deleted — what happens?
* Karpenter setup doubled costs — how do you fix?
* Everything is 200 OK but user drop — how do you debug?
* Helm rollback succeeded but app still broken — next steps?
* S3 replication failed silently — how do you detect?
* HA system still had outage — what went wrong?

---

# Behavioral / DevOps Mindset

## Questions

* Can you explain a real production incident end-to-end?
* How do you troubleshoot systematically?
* How do you justify architectural decisions?
* How do you show ownership?
* What are your day-to-day responsibilities as a DevOps Engineer?
* How do you build SLO-driven engineering culture?
* How do you test chaos and resilience?
* How do you prove ROI of infra modernization?

---

# Project / Experience-Based

## Questions

* Introduce yourself and explain your project.
* Can you explain your project architecture in detail?
* How many Git tools/repositories have you used?
* Have you worked with Terraform?

---

Good attempt, but you've mixed **Blue-Green** and **Canary**.

### Score: 6.5/10

---

## Mistake

You said:

> Blue-Green sends 10% traffic to Green and gradually increases.

That is actually **Canary Deployment**.

---

# Correct Definitions

## 1. Rolling Update (Default Kubernetes Strategy)

```text
Version 1 Pods
      ↓
Gradually Replace
      ↓
Version 2 Pods
```

Example:

```text
10 Pods v1
```

Update:

```text
9 v1 + 1 v2
8 v1 + 2 v2
...
0 v1 + 10 v2
```

Advantages:

✅ No extra environment

✅ Default in Kubernetes

Disadvantages:

❌ Rollback is slower

❌ Both versions coexist temporarily

---

## 2. Blue-Green Deployment

Two complete environments:

```text
Blue = Production
Green = New Version
```

Before switch:

```text
100% → Blue
0%   → Green
```

After testing:

```text
0%   → Blue
100% → Green
```

Traffic switch is usually immediate.

Advantages:

✅ Very fast rollback

✅ Safe testing

Disadvantages:

❌ Double infrastructure cost

---

## 3. Canary Deployment

Gradual traffic shifting.

Example:

```text
90% → v1
10% → v2
```

Then:

```text
75% → v1
25% → v2
```

Then:

```text
50% → v1
50% → v2
```

Eventually:

```text
100% → v2
```

Advantages:

✅ Lower risk

✅ Real-user validation

Disadvantages:

❌ More complex routing

❌ Requires ingress/service mesh support

---

# Interview Answer

> Kubernetes supports multiple deployment strategies.
>
> Rolling Update is the default deployment strategy where old pods are gradually replaced with new pods while maintaining application availability.
>
> Blue-Green Deployment uses two identical environments. One environment serves production traffic while the other receives the new version. After validation, traffic is switched completely to the new environment, providing fast rollback capability.
>
> Canary Deployment gradually shifts a small percentage of production traffic to the new version. If the application behaves correctly, traffic is increased incrementally until the new version receives all traffic.
>
> Rolling Updates are simple and commonly used, Blue-Green provides the fastest rollback, and Canary offers the safest production validation.

---

# Interview Follow-Up

### Which one would you choose for a banking application?

Good answer:

> For critical banking or payment applications, I would prefer Canary Deployment because it allows gradual exposure of the new version to a small percentage of users while continuously monitoring errors and performance before a full rollout.

---

Once the scheduler assigns the pod to a worker node, the kubelet running on that node detects the assignment and reads the PodSpec.

Kubelet instructs containerd to pull the required image from ACR, ECR, or another registry if it is not already present on the node.

Containerd creates and starts the containers. Once the application starts, Kubernetes executes the readiness probe. If the readiness probe succeeds, the pod is added to the Service endpoints and starts receiving traffic.

Kube-proxy updates networking rules so that traffic reaching the Service can be forwarded to the healthy pod.


