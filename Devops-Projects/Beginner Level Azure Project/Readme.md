


![image](https://github.com/user-attachments/assets/7af9b674-800f-419a-9c28-667161712e5f)

## Create resource group

home --> resourse group --> review and create 
Demo-Project

## Virtual Network 

 ![Basics](https://github.com/user-attachments/assets/7a1eec5e-d229-40a3-8e23-20f27c9aef67)

 ![Azure Bastion](https://github.com/user-attachments/assets/ec73b99c-398c-4511-8123-9e5b4a6bb505)

 Create a public IP address

 ![Add a public IP address](https://github.com/user-attachments/assets/61088f28-a5d4-4069-b657-e5545381c11e)

Enable Azure Firewall
Policy(Create new)

![ip addresses](https://github.com/user-attachments/assets/d7fc430c-60a3-48c5-b57c-60a28460cd4f)

![deployment is complete](https://github.com/user-attachments/assets/ac8404cf-14f8-40b8-8d02-01ee014e5921)

Create a virtual machine  -->
![vm-part 1](https://github.com/user-attachments/assets/cafeb65e-e7e0-4513-bf1d-12f8f02f3507)
![vm-part 2](https://github.com/user-attachments/assets/00d048c8-45a1-487f-ac7c-966f682b71b1)

![networking](https://github.com/user-attachments/assets/7014d07a-655c-44e7-8991-3f8b721458ce)

![advanced](https://github.com/user-attachments/assets/41c49d76-0f8f-43e2-a2ff-edca2c928a51)

we can give script here for automation

![image](https://github.com/user-attachments/assets/3e66cdd1-9363-49e9-acbf-dd9c16361184)

![image](https://github.com/user-attachments/assets/bbbbe015-93e5-4983-8437-5bf3e8a1e523)


vm --> connect --> Bastion 

![image](https://github.com/user-attachments/assets/641f0b58-191f-44b6-94b6-e4adc183f40d)

![image](https://github.com/user-attachments/assets/77f45894-6e6b-46b1-8d2c-589465648e97)

# Install and Configure Nginx on Ubuntu

## Step 1: Update Package Lists

Before installing any new software, it's a good practice to update the package lists to ensure you get the latest version.

```
sudo apt update
sudo apt upgrade
```

## Step 2: Install Nginx

Install Nginx using the following command:

```
sudo apt install nginx -y
```

## Step 3: Start Nginx Service

```
sudo systemctl start nginx
```

## Step 4: Create HTML File

```
sudo vi /var/www/html/index.html
```

Add the HTML content, for example.

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Demo Page</title>
</head>
<body>
    <h1> I Learnt how networking works in Azure today</h1>
</body>
</html>
```

Save the file.

### Restart Nginx

```
sudo systemctl restart nginx
```

![image](https://github.com/user-attachments/assets/2c4f712b-a1af-431e-a230-e1ace2676bdb)

configuring firewall to access vm

firewalls-- select -- click on Firewall policy -->DNAT rules --> add a rule collection 

![image](https://github.com/user-attachments/assets/4236651e-bdc5-4457-85b8-eb3db93b6338)

![image](https://github.com/user-attachments/assets/28b98176-5d69-4a8c-b5c2-a12a5d721209)
![Add a DNAT rule](https://github.com/user-attachments/assets/6e9e4add-bdb7-46ce-9945-40fb1f714af6)

Rule collection group: DefaultDnatRuleCollectionGroup
Rule collection: nginx-firwall-rule(we created earlier)
Name: nginx-rule
Source Type: IP Address
Source IP Addresses
1x3.1x7.2x.x(my lap ip)
Destination IP Addresses: 20.186.109.36(firewall public ip address)
Protocol: TCP
Destination Ports: 4000 (firewall port)
Translated Type : IP address
Translated Address: 10.0.0.4(Private ip of vm)
Translated Port : 80
save

![image](https://github.com/user-attachments/assets/1c6e9d7f-6a5e-419c-813b-d71e2bfab998)
![image](https://github.com/user-attachments/assets/5580d892-7fa3-4a27-8216-5a3eadd0816f)
