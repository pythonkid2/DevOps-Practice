# EFK Stack (Elasticsearch, Fluentd, Kibana)

The **EFK stack** is a collection of open-source tools used for **centralized logging**, log management, and analysis in cloud-native environments. It is widely used for monitoring applications and infrastructure logs, enabling real-time search, filtering, and visualization of log data.

## **Components of EFK Stack**

### **1. Elasticsearch (E) - Storage and Indexing**
- **Function**: Distributed search and analytics engine that stores, indexes, and retrieves logs.
- **Role in EFK**: Stores log data and provides full-text search and filtering capabilities.
- **Deployment**: Deployed as a **StatefulSet** in Kubernetes to maintain logs persistently.
- **Port**: **9200** (default API port)
- **Persistence**: Uses a **Persistent Volume (PV)** for durability.
- **Scaling**: Horizontal scaling supported via **sharding** and **replication**.

### **2. Fluentd (F) - Log Collection and Forwarding**
- **Function**: Data collector that **aggregates, processes, and ships logs** from multiple sources (applications, servers, and containers) to Elasticsearch.
- **Role in EFK**:
  - Collects logs from different sources like application logs, system logs, and container logs.
  - Applies filters, parsing, and transformation to logs before forwarding them.
- **Deployment**: Deployed as a **DaemonSet** in Kubernetes to run on every node and collect logs.
- **Configuration**: Uses Fluentd plugins for log forwarding and transformation.
- **Output**: Forwards logs to **Elasticsearch**.

### **3. Kibana (K) - Visualization and Monitoring**
- **Function**: Web-based UI used to visualize and analyze logs stored in Elasticsearch.
- **Role in EFK**:
  - Provides dashboards and visual representations of logs.
  - Enables querying and filtering of logs using **Elasticsearch Query Language (EQL)**.
  - Facilitates alerting and anomaly detection.
- **Deployment**: Deployed as a **Deployment** in Kubernetes.
- **Port**: **5601** (default UI port)

## **EFK Stack Deployment in Kubernetes**
### **1. Elasticsearch (StatefulSet)**
- Requires **Persistent Volumes** for storing indexed logs.
- Needs sufficient **memory and CPU** resources due to high data processing demands.
- Uses **9200** for API requests and **9300** for cluster communication.

### **2. Fluentd (DaemonSet)**
- Runs on all nodes to **capture logs** locally.
- Parses and forwards logs to Elasticsearch.
- Can be configured with plugins for different log formats.

### **3. Kibana (Deployment)**
- Provides a user interface for querying logs.
- Exposed via **NodePort**, **Ingress**, or **LoadBalancer**.

## **Advantages of EFK Stack**
- **Centralized Logging**: Stores and aggregates logs in one place for easy access.
- **Scalability**: Can be horizontally scaled to handle large volumes of logs.
- **Real-time Monitoring**: Allows real-time log analysis and visualization.
- **Flexible Log Collection**: Fluentd supports various sources and formats.
- **Integration**: Works seamlessly with Kubernetes, Docker, and cloud services.

## **Use Cases**
- Application and infrastructure monitoring
- Troubleshooting and debugging
- Security and compliance auditing
- Log retention and analytics

By implementing the EFK stack, organizations can efficiently manage and analyze logs to improve system observability and performance.



yaml files - https://github.com/ashokitschool/kubernetes_manifest_yml_files/tree/main/04-EFK-Log

