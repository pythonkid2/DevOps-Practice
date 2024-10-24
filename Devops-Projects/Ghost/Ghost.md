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

http://65.0.73.24

To generate a personal access token in GitLab, follow these steps:

### Step 1: Log into GitLab
1. Go to GitLab instance
2. Sign in with your username and password.

### Step 2: Navigate to Access Token Settings
1. After logging in, click on your profile picture or avatar in the top-right corner.
2. From the dropdown menu, select **Settings**.

### Step 3: Go to Access Tokens
1. In the left-hand sidebar of the **Settings** page, scroll down to **Access Tokens**.
   - On some versions of GitLab, this might be listed under **User Settings** > **Access Tokens**.

### Step 4: Create a New Personal Access Token
1. In the **Personal Access Tokens** section:
   - **Name**: Enter a name for the token (e.g., "GitLab CI Token").
   - **Expiration date**: Optionally, you can set an expiration date. If you leave this blank, the token will not expire.
   - **Scopes**: Choose the appropriate scopes for your token. At minimum, you’ll need:
     - **api**: Full access to the GitLab API (needed for most operations).
     - **write_repository**: Allows you to push to GitLab repositories.
     - **read_repository**: Allows read access to the repository.
   - For more limited access, choose the relevant scopes based on needs.

### Step 5: Generate Token
1. Click the **Create personal access token** button.

### Step 6: Save the Token
1. GitLab will generate the token and display it once. **Copy** the token immediately because you won’t be able to see it again.
   - Store the token securely in a password manager or safe location.


## Git Clone
```
git clone https://peerxp.vegaops.com/devops-assignment/VOGL_DI_221024_5797.git
```
Cloning into 'VOGL_DI_221024_5797'...
Username for 'https://peerxp.vegaops.com': mjcmathew@gmail.com
Password for 'https://mjcmathew@gmail.com@peerxp.vegaops.com':

```
cd VOGL_DI_221024_5797/
```
git add .

git config --global user.email "mjcmathew@gmail.com"
git config --global user.name "Mathew Joseph"

git commit -m "updated vegaops-glci.yml"

git push origin main


When prompted:
- **Username**: Your GitLab username.
- **Password**: Paste the personal access token.



# Add .gitlab-ci.yml config below.
#
```
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
    paths:
      - ghost-homepage.html

```

![image](https://github.com/user-attachments/assets/e4fa5e3e-7475-4f92-8a24-033dc276a225)

Message: You are recommended to have at least 150 MB of memory available for smooth operation. It looks like you have ~139.8828125 MB available.


I set up a new user on an Ubuntu server and installed the necessary packages for Ghost CMS, including NGINX and MySQL. Upgrading to a t3.small instance ensured sufficient memory for Ghost.

I installed Node.js and Ghost-CLI, created a directory for the installation, and completed the setup. Additionally, I configured GitLab with a personal access token and created a .vegaops-glci.yml file to automate webpage downloads. The pipeline executed successfully, demonstrating effective DevOps practices.


Challenges Faced and Solutions:

Initially, I set up the server using a t3.micro instance (2 vCPUs, 1 GiB Memory), but I encountered performance issues. Ghost required a minimum of 150 MiB of free memory, and the t3.micro instance was not able to provide sufficient resources for the installation process. The installation was significantly slowed down due to memory constraints. To resolve this, I switched to a t3.small instance (2 vCPUs, 2 GiB Memory), which provided enough memory for the Ghost installation to proceed smoothly. I monitored memory usage in real-time using the watch free -h command to ensure the system had enough resources available.

Exit Code 127 Error: During pipeline execution, an error occurred when curl was not found. This was resolved by explicitly installing the required package within the pipeline script.

GitLab Runner Pending: The job remained in a pending state due to no assigned runners. After troubleshooting, I ensured shared runners were enabled and assigned correctly.


Why I Am a Good Fit for This Position:

DevOps Skills: I’ve got hands-on experience with CI/CD pipelines, automation, and cloud platforms, which helps me create efficient and scalable solutions that fit well with the team’s objectives.

Problem Solver: During the assessment, I faced several technical challenges but managed to resolve them effectively, showing that I can troubleshoot even under pressure.

Adaptable: I’m comfortable working with a variety of tools and environments. Whether it’s AWS, Docker, or GitLab, I can quickly get up to speed and deliver high-quality results.

Team Player: I have a solid track record of collaborating with teams to deliver complex projects, always keeping an eye on the details that make automation and deployment successful.
