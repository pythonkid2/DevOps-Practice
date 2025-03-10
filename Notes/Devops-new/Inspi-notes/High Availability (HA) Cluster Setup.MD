# Kubernetes Quorum and High Availability (HA) Cluster Setup

## 1. Why Quorum Matters in Kubernetes

- Kubernetes uses **etcd** as a distributed key-value store for storing cluster state.
- **Quorum** is the majority of etcd nodes required to perform updates and maintain consistency.
- Formula: Quorum = (N/2) + 1, where **N** is the total number of etcd (master) nodes.

### Risks of Not Maintaining Quorum

- With **2 master nodes**, if **1** fails, the cluster loses quorum (as 2/2 = 1, and 1 is not a majority), causing the control plane to become **unavailable**.
- With **3 master nodes**, the quorum is **2**, allowing the cluster to remain operational if **1** node fails.

## 2. Recommended Master Node Configuration

- **For High Availability (HA):** Use an **odd** number of master nodes (e.g., **3, 5, 7**).
- **Minimum HA Setup:** 3 master nodes.
- **Failure Tolerance:** An HA cluster can tolerate **(N-1)/2** master node failures.

| Master Nodes | Quorum | Tolerated Failures |
| ------------ | ------ | ------------------ |
| 2            | 2      | 0                  |
| 3            | 2      | 1                  |
| 5            | 3      | 2                  |

## 3. Scenario: 1 Worker Node with 2 Masters

- Even with only **1 worker node**, using **2 master nodes** is not recommended due to quorum risks.
- To maintain HA, add a **3rd master node** or consider a **managed Kubernetes service**.

## 4. Alternative Options

1. **Non-HA Development Setup:**

   - 1 master + 1 worker node.
   - Suitable for development or testing environments.

2. **Managed Kubernetes Services:**

   - **Amazon EKS**, **Google GKE**, **Azure AKS** provide HA for the control plane.
   - Reduces complexity by managing master nodes and etcd internally.

## 5. Key Takeaways

- Always prefer an **odd number of master nodes** for HA.
- Avoid **2-master setups** to prevent losing quorum if **1 node fails**.
- Managed services offer a hassle-free HA control plane.


