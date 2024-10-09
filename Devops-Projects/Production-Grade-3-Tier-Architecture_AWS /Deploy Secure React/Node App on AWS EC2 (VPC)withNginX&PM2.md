https://github.com/learnItRightWay01/react-node-mysql-app

# Deploy Secure React/Node App on AWS EC2 (VPC) with NginX & PM2 
![image](https://github.com/user-attachments/assets/0dc49a3c-a4e1-4b4e-8fd1-6202f5ab7a5c)
# Archetecture Diagram 
![image](https://github.com/user-attachments/assets/446518e4-7763-47b0-8fc1-c73e31909204)

# VPC 
![image](https://github.com/user-attachments/assets/545801fa-cebc-4cf8-a42a-3e58c6e28d13)

![image](https://github.com/user-attachments/assets/20a8f0ca-a952-4ad8-a767-8bb39fe79aad)

# SG

![image](https://github.com/user-attachments/assets/10f9538e-70d1-4a81-94b5-1975a7a07589)
![image](https://github.com/user-attachments/assets/aa2f9b77-44ed-4583-9efa-3332afa1fd0a)

# Scp
```
scp -i "ohiokey.pem" ohiokey.pem ec2-user@ec2-3-145-97-77.us-east-2.compute.amazonaws.com:/home/ec2-user/
```
ssh to private instance 

# Installing Git on the Public Subnet EC2 Instance
```
sudo yum install git -y
```

# Cloning the Git Repository to the Public Subnet EC2 Instance 

```
git clone https://github.com/learnItRightWay01/react-node-mysql-app
```
![image](https://github.com/user-attachments/assets/9fa4cd8a-9490-4bd2-a28d-9e32c75092e0)


# Installing Git on the Private Subnet EC2 Instance
![image](https://github.com/user-attachments/assets/2a83b868-1005-41f7-8c17-675e32e2cf5a)

# Installing NodeJS on the Public Subnet EC2 Instance

Install node.js
To install node version manager (nvm)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
To load nvm
source ~/.bashrc
To use nvm to install the latest LTS version of Node.js
nvm install --lts
To test that Node.js is installed and running
node -e "console.log('Running Node.js ' + process.version)"

Setting up the Presentation Tier

# Installing Frontend Dependencies with npm

 cd react-node-mysql-app/frontend/

npm install

# Configuring Environment Variables with a .env File
sudo vi .env
```
VITE_API_URL="/api"
```

# Building the React Application for Production

npm install 
npm run build
![image](https://github.com/user-attachments/assets/0fc01327-433d-4d02-8017-bd5fe093e7fa)


# Installing NodeJS on the Private Subnet EC2 Instance


# Updating Database Credentials in the Backend Application

cd react-node-mysql-app/backend/

vi configs/db.js

```
const mysql = require('mysql2');

const db = mysql.createConnection({
   host: 'localhost',
   port: '3306',
   user: 'appuser',
   password: '9400157857',
   database: 'react_node_app'
});

module.exports = db;

```

# Installing Backend Dependencies with npm

npm install 

# Installing MySQL on the Private Subnet EC2 Instance
Install MySQL
To download MySQL repository package:
wget https://dev.mysql.com/get/mysql80-community-release-el9-1.noarch.rpm
To verify the package download:
ls -lrt 
To install MySQL repository package:
sudo dnf install -y mysql80-community-release-el9-1.noarch.rpm 
To import GPG key:
sudo rpm --import https://repo.mysql.com/RPM-GPG-KEY-mysql-2023 
To update package index:
sudo dnf update –y 
To install MySQL server:
sudo dnf install -y mysql-community-server  
To start the mysql service:
sudo systemctl start mysqld
To enable mysql to start on boot:
sudo systemctl enable mysqld 



sudo grep 'temporary password' /var/log/mysqld.log 

ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '9400157857Mm#';

# Creating a Dedicated Application User for the Backend


CREATE USER 'appuser'@'localhost' IDENTIFIED WITH mysql_native_password BY '9400157857Mm2#';



