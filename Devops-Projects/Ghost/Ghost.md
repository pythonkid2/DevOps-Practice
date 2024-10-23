This sequence of commands sets up a new user, installs necessary packages, configures MySQL, and installs Ghost CMS in a designated directory. Feel free to modify any user or directory names as needed!


# Update package lists
```
sudo apt update 
```
# Add a new user
```
sudo adduser peerxp
```
# Add user to the superuser group to unlock admin privileges
```
sudo usermod -aG sudo peerxp
```
# Log in as the new user
```
su - peerxp
```
# Update package lists again
```
sudo apt-get update
```
# Install NGINX
```
sudo apt-get install nginx -y
```
# Install MySQL
```
sudo apt-get install mysql-server -y
```
# Enter MySQL
```
sudo mysql
```
# Update permissions for root user
```
ALTER USER 'root'@'localhost' IDENTIFIED WITH 'mysql_native_password' BY 'Password';
```
# Reread permissions
```
FLUSH PRIVILEGES;
```
# Exit MySQL
```
exit
```
# Test MySQL login
```
mysql -u root -p
```
# Exit MySQL
```
exit
```
# Download and import the Nodesource GPG key
```
sudo apt-get update
sudo apt-get install -y ca-certificates curl gnupg
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | sudo gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg
```
# Create deb repository
```
NODE_MAJOR=18 # Use a supported version
echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_$NODE_MAJOR.x nodistro main" | sudo tee /etc/apt/sources.list.d/nodesource.list
```
# Run update and install Node.js
```
sudo apt-get update
sudo apt-get install nodejs -y
```
# Install Ghost-CLI
```
sudo npm install ghost-cli@latest -g
```
# Check Ghost-CLI version
```
ghost --version
```
# Create directory for Ghost installation
```
sudo mkdir -p /var/www/peerxp
```
# Set directory owner (replace <user> with your user name)
```
sudo chown peerxp:peerxp /var/www/peerxp
```
# Set the correct permissions
```
sudo chmod 775 /var/www/peerxp
```
# Navigate into the directory
```
cd /var/www/peerxp
```
# Install Ghost
```
ghost install
```


# Add .gitlab-ci.yml config below.
#
stages:
  - download

download_website:
  stage: download
  image: alpine
  script:
    - apk add --no-cache curl  # Install curl
    - curl http://43.205.118.193 > ghost-homepage.html  # Download the webpage
  artifacts:
    name: "ghost-homepage"
    expire_in: 1 hour
    paths:
      - ghost-homepage.html

![image](https://github.com/user-attachments/assets/e4fa5e3e-7475-4f92-8a24-033dc276a225)
