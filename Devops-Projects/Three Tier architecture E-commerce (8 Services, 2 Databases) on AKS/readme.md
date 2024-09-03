# Three Tier architecture E-commerce (8 Services, 2 Databases) on AKS

- Understand what is three tier architecuture
- How different services connect to each other in three tier architecture
- How to create Dockerfiles for each service ?
- How to create Deployment, Service and Ingress
- How does Ingress controller work ?
- Expose the three tier application to end users.

![Screenshot 2024-02-16 at 1 43 25 PM](https://github.com/iam-veeramalla/Azure-zero-to-hero/assets/43399466/0623a010-d8f1-4632-abce-d06f5755b1fa)

Repo link: https://github.com/pythonkid2/three-tier-architecture-project

### Microservices Architecture for Stance Robot Shop

1. **User Service**  
   - **Functionality:** Handles user registration, validation (e.g., email format, password strength), and login.  
   - **Flow:** The first step is user registration. Validation checks (like email and password policies) ensure valid inputs. Once registered, the user credentials are securely stored in the database. After successful registration, users can log in to the platform.  
   - **Database:** MongoDB, storing user information such as usernames, passwords, and other related data.

2. **Catalog Service**  
   - **Functionality:** Manages product catalogs, including various categories, product descriptions, prices, and images.  
   - **Flow:** After logging in, the user can browse the catalog to explore products. The catalog microservice fetches product details like descriptions, pricing, and images from its database.  
   - **Database:** MySQL, storing product information and associated images.

3. **Cart Service**  
   - **Functionality:** Allows users to add products to their cart and maintains the state of the cart even if the user logs out.  
   - **Flow:** Users can add products (robots) to the cart, and the cart data persists even across sessions (e.g., when logging out and logging back in). Once the user proceeds to checkout and buys the product, the items are removed from the cart. If they don’t complete the payment, the items remain in the cart for later.  
   - **Persistent Cart:** Cart data is maintained until the payment process is completed.

4. **Shipping Service**  
   - **Functionality:** Calculates shipping costs based on the user's location.  
   - **Flow:** After the cart is confirmed, shipping costs are computed based on the product’s destination. This service factors in location and distance to determine shipping fees. In real-world applications, this might involve querying a shipping provider's API or using a predefined formula.

5. **Payment Service**  
   - **Functionality:** Manages the payment process.  
   - **Flow:** After calculating shipping costs, the user is prompted to complete the payment. The payment service handles the transaction and ensures payment is successfully processed before moving to the next step.

6. **Dispatch Service**  
   - **Functionality:** Manages the dispatch process once the payment is completed and provides tracking information.  
   - **Flow:** After successful payment, the dispatch service prepares the product for shipment and provides tracking information to the user, confirming that the product is ready for delivery.

7. **Rating Service**  
   - **Functionality:** Handles product ratings, allowing users to rate and review products dynamically.  
   - **Flow:** After receiving and using the product, users can rate it. Ratings are stored dynamically, and changes reflect immediately. The rating data is stored in an in-memory data store (Redis) for fast retrieval, given the frequent and dynamic nature of the updates.

8. **Web Service**  
   - **Functionality:** Hosts the front-end web interface for the e-commerce platform.  
   - **Flow:** The web service, built with technologies like Angular, React, or simple HTML/CSS/JavaScript, serves as the user interface. This microservice runs on a web server like Nginx or Apache and is responsible for serving the application to users.

### Databases
- **MongoDB:** Used for storing user-related information, such as registration details, usernames, passwords, and other personal data.
- **MySQL:** Used for product-related data, including product descriptions, prices, and images.

### Additional Considerations:
- **Programming Languages:** Each microservice is implemented in different programming languages (e.g., Node.js for Cart, Python for Payments, PHP for Dispatch) to demonstrate the versatility of microservice architecture. In real-world scenarios, however, teams may choose a single language for consistency. This diversity of languages helps DevOps engineers gain experience with writing Dockerfiles for various environments.
  
- **In-Memory Data Store (Redis):** Used in the Rating Service for fast, dynamic updates. Redis is set up as a StatefulSet in Kubernetes with persistent volumes to ensure data persistence in case of failure.

### Deployment Strategy:
- Each microservice is containerized and independently deployable. The goal is to ensure that each service can be updated, scaled, or replaced without affecting the other services, enhancing the flexibility, maintainability, and reliability of the system.

## **Dockerfile Notes for Microservices**

1. **Cart Application (Node.js)**:
   - **Base Image**: Start with a Node.js base image.
   - **Environment Variables**: Ignore non-essential fields like `INSTANA_AGENT_KEY` if not relevant to the project (e.g., monitoring tools like Instana).
   - **Working Directory**: Set a working directory where the subsequent operations will take place.
   - **Dependencies**: Copy `package.json` (Node.js equivalent of `requirements.txt` in Python or `pom.xml` in Java) to the working directory and run `npm install` to install dependencies.
   - **Source Code**: Copy `server.js` (the main source code file) to the working directory.
   - **CMD**: Use `node server.js` to run the application.

2. **Python Microservice**:
   - **Base Image**: Start with a Python base image.
   - **Working Directory**: Set the working directory.
   - **Dependencies**: Copy `requirements.txt` and run `pip install` to install Python dependencies.
   - **Source Code**: Copy application files (e.g., `app.py`).
   - **CMD**: Use `python app.py` to run the application.

3. **Go Microservice**:
   - **Base Image**: Start with a Go base image.
   - **Working Directory**: Set the working directory.
   - **Dependencies**: Copy `go.mod` and run `go install` to build the Go binary.
   - **Source Code**: Copy the source code and run the binary directly.

4. **Java Microservice (Multi-Stage Docker Build)**:
   - **Stage 1 (Build Stage)**: 
     - Use a heavy image (e.g., Debian) and install necessary build tools like Maven.
     - Build the `.jar` or `.war` file and store it.
   - **Stage 2 (Runtime Stage)**:
     - Use a lightweight image (e.g., OpenJDK).
     - Copy the built `.jar` file from the build stage to this lightweight image.
     - **CMD**: Run the `.jar` file using `java -jar <file>.jar`.

5. **Best Practices**:
   - **Multi-Stage Builds**: Reduce the final image size by separating the build environment from the runtime environment (e.g., building in a Debian image and running in a smaller OpenJDK image).
   - **Avoid Root User**: Avoid running the container as the root user to enhance security.
   - **Consistency**: Dockerfiles across languages (Node.js, Python, Go, Java) share a similar structure (setting the base image, working directory, copying dependencies, installing them, and running the application).


---

### **Project Overview**

- **Subscription**: Free Trial  
- **Resource Group**: aks-ecommerce-store  
- **Region**: West US 2

---

### **Step 1: Create Resource Group**

1. **Log in to Azure Portal**: [Azure Portal](https://portal.azure.com)
2. **Navigate to Resource Groups**:
   - In the left-hand menu, select **Resource Groups**.
3. **Create a Resource Group**:
   - Click on the **+ Create** button at the top.
   - In the **Basics** tab, fill in the following details:
     - **Subscription**: Select **Free Trial**.
     - **Resource Group Name**: `aks-ecommerce-store`.
     - **Region**: Select **West US 2** from the dropdown.
4. **Review + Create**:
   - Review the details and click **Create** to provision the resource group.

---

### **Step 2: Create AKS Cluster**

1. **Navigate to Kubernetes Services**:
   - In the left-hand menu, search for and select **Kubernetes services**.
2. **Create a Kubernetes Cluster**:
   - Click on the **+ Create** button at the top.
3. **Basics Tab**:
   - **Subscription**: Select **Free Trial**.
   - **Resource Group**: Choose `aks-ecommerce-store`.
   - **Kubernetes Cluster Name**: Choose a unique name for your cluster.
   - **Region**: Select **West US 2**.
   - **Kubernetes Version**: Choose the version you want (latest stable version recommended).
   - **Node Size**: Choose a node size based on your workload requirements (e.g., `Standard_DS2_v2`).
   - **Node Count**: Start with a default node count (e.g., 3).

   ![image](https://github.com/user-attachments/assets/2ec5a886-95f7-40bc-abf2-6c5eaacf8a00)

4. **Node Pools Tab**:
   - Configure your node pools based on workload requirements.
   - Add additional node pools if required.

   ![image](https://github.com/user-attachments/assets/822a03b8-d405-4145-8313-a9a3177984b1)

5. **Networking Tab**:
   - Choose between Azure CNI or Kubenet based on your network requirements.
   - Enable other advanced settings as required (e.g., network policies, load balancer options, etc.).

   ![image](https://github.com/user-attachments/assets/413bf2c4-b9e1-49f2-9636-f9fa7a79b283)

6. **Integrations Tab** (Optional):
   - Enable any required integrations such as monitoring, logging, or Azure Active Directory.

7. **Review + Create**:
   - Review the configurations across all tabs.
   - Click **Create** to deploy the AKS cluster.


Once the AKS cluster is created, you can manage your cluster and deploy workloads using Azure Kubernetes Service.

![cluster deployed](https://github.com/user-attachments/assets/4dee3b82-0456-4377-8d96-392eb50f40c5)

---

## Connecting to the VM and Working with the AKS Cluster

To set up and connect to the VM for interacting with the AKS cluster, follow these steps:

### Step 1: SSH into the VM
Use the following command to establish an SSH connection to the VM from the local terminal:

```
ssh <username>@<VM_IP_Address>
```

Replace `<username>` with the VM's username and `<VM_IP_Address>` with the public IP of the VM.

### Step 2: Install Azure CLI
If the Azure CLI is not already installed, use the command below to install it on the VM:

```
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
```

### Step 3: Login to Azure
Once the installation is complete, log in to Azure:

- **For Windows:**
  ```
  az login
  ```
- **For Linux:**
  ```
  az login --use-device-code
  ```

This will generate a code and link for authentication. Follow the instructions to complete the login process.

![Azure Login](https://github.com/user-attachments/assets/cbccb265-f76f-4e49-8661-e486c1a06c96)
<img width="800" alt="Azure Login Success" src="https://github.com/user-attachments/assets/3b75f1f2-ae85-4e08-8200-f46f02befda2">

### Step 4: Get Credentials for the AKS Cluster
After logging in, retrieve the credentials for the AKS cluster with the following command:

```
az aks get-credentials --resource-group aks-ecommerce-store --name <AKS_Cluster_Name>
```

Replace `<AKS_Cluster_Name>` with the name of the AKS cluster. For example:

```
az aks get-credentials --resource-group aks-ecommerce-store --name three-tier
```

### Step 5: Install `kubectl`
Install `kubectl` to manage the Kubernetes cluster:

```
sudo snap install kubectl --classic
```

![Install kubectl](https://github.com/user-attachments/assets/98741588-bc65-4a04-8466-f7fc9acffd52)

### Step 6: Verify the Connection to the Cluster
Check the connection to the AKS cluster by listing the nodes in the cluster:

```
kubectl get nodes
```

If successful, this will display a list of the nodes in the cluster, confirming the connection.

![kubectl get nodes](https://github.com/user-attachments/assets/51bd99a9-4da5-472c-96bb-e6b799ddba4d)

ubuntu@controller:~$ kubectl config current-context
three-tier


--- 

## Deploying the Helm Chart to AKS

### Step 1: Clone the Repository
Clone the project repository from GitHub:

```
git clone https://github.com/pythonkid2/three-tier-architecture-project.git
```

Navigate into the project directory:

```
cd three-tier-architecture-project/
```

### Step 2: Navigate to the Helm Directory
Move to the directory containing the Helm chart:

```
cd AKS/
cd helm/
```

### Step 3: Create a Kubernetes Namespace
Create the `robot-shop` namespace in the Kubernetes cluster:

```
kubectl create ns robot-shop
```

### Step 4: Install Helm (if not already installed)
Install Helm using Snap:

```
sudo snap install helm --classic
```

### Step 5: Deploy the Helm Chart
Deploy the Helm chart to the `robot-shop` namespace:

```
helm install robot-shop --namespace robot-shop .
```

![image](https://github.com/user-attachments/assets/fd76ee23-dd54-4d1f-97fc-b334f71cdcbd)

![image](https://github.com/user-attachments/assets/e9a4529a-c35c-48a8-8a67-69994bd44ea0)

---

need to move to cluster and enable ingress config

three-tier > settings>  Networking


![image](https://github.com/user-attachments/assets/41377759-d098-4336-8407-528e8a88a410)

![image](https://github.com/user-attachments/assets/da0aec35-69b9-4f94-a47d-9bcf738cab80)

![image](https://github.com/user-attachments/assets/133c262b-5617-4759-abd0-df0c93f35ac3)

![image](https://github.com/user-attachments/assets/06e17a2f-b1fe-49f9-9a8b-4dd9a71cc0b8)

![image](https://github.com/user-attachments/assets/96fdc95f-a6fa-4704-b2cf-9da63a88914f)

