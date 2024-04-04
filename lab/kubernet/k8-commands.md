1. **kubectl version (ℹ️):** Check kubectl & cluster version for compatibility.

2. **kubectl get nodes ():** List all worker nodes in your cluster.

3. **kubectl get pods ():** List all pods running in your cluster.

4. **kubectl describe pod <pod_name> ():** Get detailed info on a specific pod.

5. **kubectl logs pod <pod_name> ():** View logs for a running pod.

6. **kubectl exec -it pod <pod_name> /bin/bash ():** Get an interactive shell in a pod.

7. **kubectl apply -f <filename.yaml> ():** Apply a YAML file to create/update resources.

8. **kubectl delete pod <pod_name> (️):** Delete a pod.

9. **kubectl scale deployment <deployment_name> --replicas=2 ():** Scale a deployment (e.g., set replicas to 2).

10. **kubectl get deployments ():** List all deployments in your cluster.

11. **kubectl get services ():** List all services running in your cluster.

12. **kubectl expose deployment <deployment_name> --type=LoadBalancer ():** Expose a deployment externally.

13. **kubectl get namespaces ():** List all namespaces in your cluster.

14. **kubectl create namespace <new_namespace> (➕):** Create a new namespace.

15. **kubectl get events ():** View recent cluster events.

16. **kubectl cordon node <node_name> ():** Mark a node unschedulable for maintenance.

17. **kubectl drain node <node_name> ():** Drain a node by evicting pods in preparation for maintenance.

18. **kubectl rollout history deployment <deployment_name> (⏱️):** View deployment rollout history.

19. **kubectl label pod <pod_name> <key>=<value> (️):** Add or update labels on a pod.

20. **kubectl port-forward pod <pod_name> <local_port>:<container_port> ():** Forward a pod's port to your local machine.
