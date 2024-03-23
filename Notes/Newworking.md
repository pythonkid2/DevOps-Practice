
-[ip address](#ip-address)



## IP address

<img width="852" alt="image" src="https://github.com/pythonkid2/DevOps-Practice/assets/100591950/0a4a34b6-767e-4dfd-a74c-04118666c87e">

<img width="761" alt="image" src="https://github.com/pythonkid2/DevOps-Practice/assets/100591950/5888773d-49ff-4623-b2c4-e465ffe4d17d">

![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/1449ed48-840b-4cfc-af4d-398c81892d43)

<img width="900" alt="image" src="https://github.com/pythonkid2/DevOps-Practice/assets/100591950/fe236890-6719-40cc-b893-5180140996fa">

<img width="780" alt="image" src="https://github.com/pythonkid2/DevOps-Practice/assets/100591950/e622fa10-3410-462a-af49-af4526faeee8">






+++


<img width="539" alt="image" src="https://github.com/pythonkid2/DevOps-Practice/assets/100591950/81969360-c58f-49bb-893c-363987ec7ac2">

<img width="926" alt="image" src="https://github.com/pythonkid2/DevOps-Practice/assets/100591950/776d2fab-4b81-4d96-8ade-187a6f8f5c48">

IP CLassA

<img width="577" alt="image" src="https://github.com/pythonkid2/DevOps-Practice/assets/100591950/94658ea1-88eb-4fbc-aa53-030e49ea01ec">

TYpes 

<img width="619" alt="image" src="https://github.com/pythonkid2/DevOps-Practice/assets/100591950/e5787215-711a-4199-bfa3-fc3b9850cd80">




The IP address "192.168.0.0/16" represents a Class B private IP address range. The "/16" at the end indicates the subnet mask, which means the first 16 bits of the IP address are fixed as the network portion, leaving 16 bits for the host portion.

To create 1 VPC and 3 subnets from this IP range, you can follow these steps:

Create a VPC:

Since the given IP range is 192.168.0.0/16, it means the entire range of IP addresses from 192.168.0.0 to 192.168.255.255 is available for use within the VPC.
Creating Subnets:

Since you need to create 3 subnets, you can divide the available IP range into smaller subnets.

To divide the /16 range into 3 subnets, you can use the following subnet mask calculation:

Number of bits needed for 3 subnets = ceil(log2(3)) = 2 bits (as 2^2 = 4 > 3)

Therefore, the subnet mask for each subnet would be /16 + 2 = /18 (16 + 2 = 18)

Subnet 1: 192.168.0.0/18 (192.168.0.0 to 192.168.63.255)

Subnet 2: 192.168.64.0/18 (192.168.64.0 to 192.168.127.255)

Subnet 3: 192.168.128.0/18 (192.168.128.0 to 192.168.191.255)

This way, you have created 1 VPC with 3 subnets from the given IP address range "192.168.0.0/16". Each subnet will have a range of IP addresses that can be used for assigning to instances or resources within that subnet.



CIDR stands for Classless Inter-Domain Routing. It is a method used to allocate IP addresses and IP routing. In IPv4, CIDR notation is used to represent IP addresses and their associated subnet masks.

In CIDR notation, an IP address is followed by a forward slash and a number, which represents the number of bits in the subnet mask. For example, "192.168.0.0/16" represents the IPv4 address 192.168.0.0 with a subnet mask of 16 bits.

To calculate the number of IP addresses in a CIDR block, you can use the formula:

Number of IP addresses = 2^(32 - subnet mask)
For example, in a /16 CIDR block:

Number of IP addresses = 2^(32 - 16) = 2^16 = 65,536 IP addresses
CIDR notation allows for flexible allocation of IP addresses and efficient use of address space by allowing for variable-length subnet masks.
