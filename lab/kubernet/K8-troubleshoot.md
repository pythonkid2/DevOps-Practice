problem -The connection to the server 172.31.21.140:6443 was refused - did you specify the right host or port?

Solution -

sudo -i && swapoff -a && exit

https://docs.tigera.io/calico/latest/getting-started/kubernetes/self-managed-onprem/onpremises#install-calico-with-kubernetes-api-datastore-50-nodes-or-less

kubeadm init --apiserver-advertise-address=172.31.28.13  --pod-network-cidr=192.168.0.0/16
![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/8fd307f8-95f3-40bf-b557-4a25e472ebc4)

+++
 **Here's a summary of the current situation:**

- **Docker Socket Permission:** The ownership of `/var/run/docker.sock` seems correct (owned by `root`, group `docker`), so permission issues with the socket itself are less likely.
- **Docker Daemon Options:** The Docker daemon is running with standard options (`-H fd://` and `--containerd=/run/containerd/containerd.sock`), which don't appear to restrict socket access.
- **Alternative Drivers:** You still have the option to install one of the suggested drivers (kvm2, podman, qemu2) if the Docker permission issue persists.

**Next Steps for Troubleshooting:**

1. **Review minikube Logs Thoroughly:** Inspect the full output of `minikube start` for any additional clues or error messages that might shed light on the problem. Look for hints about why it's still reporting permission issues even though the socket ownership and daemon options seem correct.

2. **Temporarily Adjust Docker Socket Permissions:** Although not recommended for long-term use due to security concerns, try temporarily making the socket world-readable and writable to see if it allows minikube to start:

   ```bash
   sudo chmod 666 /var/run/docker.sock
   minikube start
   ```

   If this works, it confirms a permission-related problem and you'll need to investigate further to find a more secure solution.

3. **Explore Security Contexts (if applicable):** If you're using tools like SELinux or AppArmor, they might have policies that restrict access to the Docker socket. Check the documentation for your security tools to see if any adjustments are needed for minikube to function properly.

4. **Seek Community Assistance:** If the issue persists, consider reaching out to the minikube community forums or GitHub issue tracker for more specialized help. Provide detailed information about your environment, steps taken, and relevant logs to get assistance from experienced users and developers.
