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

mysql> GRANT ALL PRIVILEGES ON react_node_app.* TO 'appuser'@'localhost';

# Setting up the Backend Database: Creating Database, Tables and Restoring Data

CREATE DATABASE react_node_app;
use react_node_app;

INSERT INTO `author` VALUES (1,'J.K. Rowling (Joanne Kathleen Rowling)','1965-07-31','J.K. Rowling is a British author best known for writing the Harry Potter fantasy series. The series has won multiple awards and sold over 500 million copies, becoming the best-selling book series in history. Rowling has also written other novels, including The Casual Vacancy and the Cormoran Strike crime series under the pen name Robert Galbraith.','2024-05-29','2024-05-29'),(3,'Jane Austen','1775-12-16','Jane Austen was an English novelist known for her wit, social commentary, and romantic stories. Her six major novels, which explore themes of love, marriage, and money, have earned her a place as one of the greatest writers in the English language.','2024-05-29','2024-05-29'),(4,'Harper Lee','1960-07-11','Harper Lee was an American novelist best known for her Pulitzer Prize-winning novel To Kill a Mockingbird. The novel explores themes of racial injustice and the importance of compassion. Lee published a sequel, Go Set a Watchman, in 2015.','2024-05-29','2024-05-29'),(5,'J.R.R. Tolkien','1954-07-29','J.R.R. Tolkien was a British philologist and writer best known for his fantasy novels The Hobbit and The Lord of the Rings. Tolkien\'s works have had a profound influence on the fantasy genre and popular culture.','2024-05-29','2024-05-29'),(6,'Mary Shelley','1818-03-03','Mary Shelley was a British novelist, playwright, and short story writer, the daughter of Mary Wollstonecraft Godwin and the wife of poet Percy Bysshe Shelley. Frankenstein, or, The Modern Prometheus (1818) is her most famous work.','2024-05-29','2024-05-29'),(7,'Douglas Adams','1979-10-12','Douglas Adams was an English science fiction writer, satirist, humorist, dramatist, screenwriter, and occasional actor. He is best known for the Hitchhiker\'s Guide to the Galaxy comedy series, which inspired a radio comedy, several books, stage shows, comic books, a 1981 TV series, a 1984 video game, a 2005 feature film, and a 2008 sequel film.','2024-05-29','2024-05-29'); 


INSERT INTO `book` VALUES (1,'Harry Potter and the Sorcerer\'s Stone','1997-07-26','On his birthday, Harry Potter discovers that he is the son of two well-known wizards, from whom he has inherited magical powers. He must attend a famous school of magic and sorcery, where he establishes a friendship with two young men who will become his companions on his adventure. During his first year at Hogwarts, he discovers that a malevolent and powerful wizard named Voldemort is in search of a philosopher\'s stone that prolongs the life of its owner.',223,'2024-05-29','2024-05-29',1),(3,'Harry Potter and the chamber of secrets','1998-07-02','Harry Potter and the sophomores investigate a malevolent threat to their Hogwarts classmates, a menacing beast that hides within the castle.',251,'2024-05-29','2024-05-29',1),(4,'Pride and Prejudice','1813-01-28','An English novel of manners by Jane Austen, first published in 1813. The story centres on the relationships among the Bennet sisters, in particular Elizabeth Bennet the middle daughter, and the wealthy Mr. Darcy. Austen satirizes the social classes of the English gentry through a witty and ironic narrative voice.',224,'2024-05-29','2024-05-29',3),(5,'Harry Potter and the Prisoner of Azkaban','1999-07-08','Harry\'s third year of studies at Hogwarts is threatened by Sirius Black\'s escape from Azkaban prison. Apparently, it is a dangerous wizard who was an accomplice of Lord Voldemort and who will try to take revenge on Harry Potter.',317,'2024-05-29','2024-05-29',1),(6,'Harry Potter and the Goblet of Fire','2000-07-08','Hogwarts prepares for the Triwizard Tournament, in which three schools of wizardry will compete. To everyone\'s surprise, Harry Potter is chosen to participate in the competition, in which he must fight dragons, enter the water and face his greatest fears.',636,'2024-05-29','2024-05-29',1),(7,'The Hitchhiker\'s Guide to the Galaxy','1979-10-12','A comic science fiction comedy series created by Douglas Adams. The story follows the comedic misadventures of Arthur Dent, a hapless Englishman, following the destruction of the Earth by the Vogons, a race of unpleasant bureaucratic aliens. Arthur escapes with his friend Ford Prefect, who reveals himself to be an undercover researcher for the titular Hitchhiker\'s Guide to the Galaxy, a galactic encyclopedia containing information about anything and everything.',184,'2024-05-29','2024-05-29',7),(8,'Frankenstein; or, The Modern Prometheus','1818-03-03','A Gothic novel by Mary Shelley that tells the story of Victor Frankenstein, a young scientist who creates a grotesque creature in an unorthodox scientific experiment. Frankenstein is horrified by his creation and abandons it, but the creature seeks revenge. The novel explores themes of scientific responsibility, creation versus destruction, and the nature of good and evil.',211,'2024-05-29','2024-05-29',6),(9,'The Lord of the Rings: The Fellowship of the Ring','1954-07-29','The first book in J.R.R. Tolkien\'s epic fantasy trilogy, The Lord of the Rings. The Fellowship of the Ring follows hobbit Frodo Baggins as he inherits the One Ring, an evil artifact of power created by the Dark Lord Sauron. Frodo embarks on a quest to destroy the Ring in the fires of Mount Doom, accompanied by a fellowship of eight companions.',482,'2024-05-29','2024-05-29',5);


![image](https://github.com/user-attachments/assets/c15bc4fb-e0fa-4769-aa4e-9e85b273cc1d)


