### Kubernetes Manifests & Helm Charts for Microservices

In this project, Kubernetes manifests are dynamically managed using Helm charts, which allows for the easy deployment of multiple microservices across different environments (Dev, Staging, Prod). Here’s how you can manage and deploy Kubernetes resources for the project:

---

### **Kubernetes YAML Manifest vs. Helm Chart**
- **Kubernetes YAML Manifest**:
  - Direct YAML manifests specify all configurations, such as deployments, services, etc.
  - For each microservice, you need a deployment and service YAML file (e.g., 24 YAML files for 8 microservices + 2 databases).
  - Using direct manifests across multiple environments leads to duplicate YAML files for each environment, making maintenance complicated (e.g., 120 files for 5 environments).

- **Helm Chart**:
  - Helm simplifies this by using a templating system that allows dynamic parameters in your YAML files, meaning you only manage one set of templates, even across multiple environments.
  - **Templates Folder**: Contains the YAML manifest files, but the fields that need to be dynamic (e.g., resource limits, image tags, environment variables) are templated.
  - **Values File**: Stores dynamic values such as image repository, resource limits, node selectors, etc., that are specific to different environments.
  - **Chart.yaml**: Provides metadata for the Helm chart (e.g., version, name, dependencies).

---

### **Helm Chart Components**
1. **Templates Folder**:
   - Contains templated versions of your YAML manifests.
   - Dynamic fields are handled using the Go templating language (`{{ }}` syntax).
   - Example:
     ```yaml
     apiVersion: apps/v1
     kind: Deployment
     metadata:
       name: payments
     spec:
       template:
         spec:
           containers:
             - name: payments
               image: "{{ .Values.image.repo }}:{{ .Values.image.tag }}"
               env:
                 - name: PAYMENT_GATEWAY
                   value: "{{ .Values.payment.gateway }}"
               resources:
                 requests:
                   memory: "{{ .Values.resources.requests.memory }}"
                   cpu: "{{ .Values.resources.requests.cpu }}"
                 limits:
                   memory: "{{ .Values.resources.limits.memory }}"
                   cpu: "{{ .Values.resources.limits.cpu }}"
     ```

2. **Values.yaml**:
   - Stores dynamic values that vary based on the environment.
   - You specify different values here for development, staging, and production environments.
   - Example:
     ```yaml
     image:
       repo: roboshop/payments
       tag: latest
     payment:
       gateway: stripe
     resources:
       requests:
         memory: "64Mi"
         cpu: "250m"
       limits:
         memory: "256Mi"
         cpu: "500m"
     ```

3. **Chart.yaml**:
   - Contains metadata about the Helm chart, such as its name, version, and dependencies.
   - Example:
     ```yaml
     apiVersion: v2
     name: roboshop
     description: A Helm chart for Roboshop microservices
     version: 1.0.0
     appVersion: "1.0"
     ```

---

### **Steps to Deploy Kubernetes Resources with Helm**
1. **Install Helm**: Ensure that Helm is installed and configured to interact with your Kubernetes cluster.
2. **Navigate to the Helm Chart Directory**: Go to the directory where the Helm chart (K folder) is located.
3. **Configure Values.yaml**:
   - Edit the `values.yaml` file to match the configuration for your environment (e.g., image repository, resource limits, environment variables).
4. **Deploy the Chart**:
   - Use the following command to deploy the chart to your cluster:
     ```bash
     helm install <release-name> ./path-to-chart
     ```
   - Example:
     ```bash
     helm install roboshop ./eks
     ```
5. **Upgrade the Chart**:
   - If you make any changes to the values or templates, upgrade the existing release:
     ```bash
     helm upgrade <release-name> ./path-to-chart
     ```

---

### **Advantages of Helm**:
1. **Dynamic Values**: You can change environment-specific parameters in a single place (`values.yaml`) rather than managing multiple YAML files for each environment.
2. **Versioning**: You can maintain and upgrade different versions of the Helm chart as your application evolves.
3. **Reusability**: Instead of duplicating YAML files, you manage only one set of templates, making it easier to maintain over time.
4. **Easier Rollback**: Helm provides built-in support for rollbacks, making it easy to revert to previous configurations if something goes wrong.

---

### **Summary**
Using Helm charts for Kubernetes manifest management allows you to scale microservices deployments across environments efficiently. Instead of manually editing individual YAML files, you can dynamically adjust parameters using Helm's templating system, simplifying multi-environment management and reducing redundancy.
