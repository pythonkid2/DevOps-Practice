```
source <(kubectl completion bash) 
alias k=kubectl
complete -o default -F __start_kubectl k
```

check accessibility

curl 

Check service status

kubectl describe service service-name

compare the selectors with pods labels


check pod
check restarts number 
describe
logs
kubectl logs web -f 
kubectl logs web -f --previous 


K CONFIG SET-CONTEXT --CURRENT --NAMESPACE=ALPHA



check dependedent service and pod 



control plane issue ensure the pods on kubesystem namespace are running
check svc logs
cat /etc/kubernetes/manifests 

nodestatus

check node status , ready or not ready 
kubectl describe node command
servce kubelet status
check kubelet certificate


