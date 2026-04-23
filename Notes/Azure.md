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
