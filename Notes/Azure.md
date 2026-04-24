azure
<img width="1027" height="539" alt="image" src="https://github.com/user-attachments/assets/54d32e04-f6d1-4bf7-97cc-2d4aa6acf5a9" />


Virual network 


nsg: used to conrol the trafic to azure resource


<img width="1284" height="705" alt="image" src="https://github.com/user-attachments/assets/77fd5665-ebf3-4359-abcf-547e93c47a65" />

In Amazon Web Services (AWS), the equivalent of an Azure Network Interface (NIC) is the Elastic Network Interface (ENI). 

Key Comparison: ENI vs. Azure NIC
While they perform the same basic function, there are slight differences in how you interact with them:
Feature 	AWS Elastic Network Interface (ENI)	Azure Network Interface (NIC)
Primary Use	Attached to EC2 instances to provide network connectivity.	Attached to Azure VMs to provide network connectivity.
IP Addresses	Can have a primary private IP, multiple secondary private IPs, and Elastic IPs.	Can have multiple IP configurations, each with private and public IPs.
Security	Associated with AWS Security Groups.	Associated with Azure Network Security Groups (NSGs).
MAC Address	Includes a fixed MAC address that stays with the ENI even if moved between instances.	Includes a MAC address assigned at creation.
Detaching	Can be hot-attached or detached from instances (if it's not the primary interface).	Can be added or removed from VMs, though some restrictions apply based on the VM state.




# Storage Service


<img width="1286" height="692" alt="image" src="https://github.com/user-attachments/assets/3b910c7c-f656-47fa-825d-6bbb90ec11db" />

<img width="1231" height="697" alt="image" src="https://github.com/user-attachments/assets/894007c8-c3f1-4c36-a0ac-2baf8b394a98" />

<img width="1279" height="611" alt="image" src="https://github.com/user-attachments/assets/6e3263a7-24b9-4f24-b5a6-6cf23bc79a0d" />

Blob Storage is the direct alternative to AWS S3, not EBS. 
Both are object storage services designed to store unstructured files like images, logs, and backups. [2, 3, 4] 
The confusion often arises because Azure Blob Storage is split into different "sub-types" behind the scenes, and Azure handles its virtual hard disks a bit differently than AWS. [5, 6] 
Here is the quick breakdown to clear up the confusion.
------------------------------
## 🗺️ The Actual Equivalent Services
The real map between AWS and Azure storage is:

* 🗃️ Object Storage: AWS S3 $\leftrightarrow$ Azure Blob Storage
* 💽 Block Storage: AWS EBS $\leftrightarrow$ Azure Managed Disks (Compute disks attached to VMs)
* 📁 File Storage: AWS EFS $\leftrightarrow$ Azure Files (Shared network drives) [3, 6, 7] 
* 

------------------------------
## 🤔 Why Do People Connect Blob to EBS?
There are two technical reasons why Azure Blob storage is sometimes mentioned alongside EBS:
## 1. Page Blobs vs. Block Blobs
Inside Azure Blob storage, there are different types of blobs: [5] 

* Block Blobs: Used for standard files (This is the exact match to S3).
* Page Blobs: Optimized for random read/write operations. Azure uses Page Blobs to store the virtual hard disk (.vhd) files that back Azure Virtual Machines. Because they act as the backend for VM disks, people sometimes associate them with AWS EBS. [4, 5, 8, 9] 
* 

## 2. AWS S3 Powers EBS Snapshots
On the AWS side, when you take a backup snapshot of an EBS block volume, AWS automatically saves that raw snapshot into Amazon S3 in the background. [10] 
------------------------------
## ⚖️ Summary of the Differences

| Feature [1, 5, 6, 11, 12] | AWS EBS / Azure Managed Disks | AWS S3 / Azure Blob Storage |
|---|---|---|
| Storage Type | Block Storage | Object Storage |
| Primary Use | OS boot drives, live databases | App data, media files, backups |
| Accessibility | Must be attached to a specific VM | Accessible anywhere via internet URL |



