# [Link to the project](https://github.com/pythonkid2/Jenkins-Zero-To-Hero/tree/main/java-maven-sonar-argocd-helm-k8s)

# Spring Boot based Java web application
 
This is a simple Sprint Boot based Java application that can be built using Maven. Sprint Boot dependencies are handled using the pom.xml 
at the root directory of the repository.

This is a MVC architecture based application where controller returns a page with title and message attributes to the view.

## Execute the application locally and access it using your browser

Checkout the repo and move to the directory

```
git clone https://github.com/pythonkid2/Jenkins-Zero-To-Hero
```
```
cd Jenkins-Zero-To-Hero/java-maven-sonar-argocd-helm-k8s/spring-boot-app
```

Certainly! Here's the properly formatted installation process for Apache Maven 3.9.6 on Ubuntu:

1. **Download Apache Maven**:
   ```
   wget https://dlcdn.apache.org/maven/maven-3/3.9.6/binaries/apache-maven-3.9.6-bin.zip
   ```

2. **Install unzip** (if not already installed), and extract the ZIP file:
   ```
   sudo apt install unzip -y && unzip apache-maven-3.9.6-bin.zip
   ```

3. **Move Apache Maven to a suitable directory** (e.g., /opt):
   ```
   sudo mv apache-maven-3.9.6 /opt
   ```

4. **Set up environment variables**:
   Open the `.bashrc` file for editing:
   ```
   nano ~/.bashrc
   ```
   Add the following lines to the end of the file:
   ```
   export M2_HOME=/opt/apache-maven-3.9.6
   export PATH=$PATH:$M2_HOME/bin
   ```

5. **Apply the changes**:
   After adding the lines to `.bashrc`, save and close the file (in Nano, press `Ctrl + X`, then `Y`, and then `Enter`). Then, apply the changes to your current session:
   ```
   source ~/.bashrc
   ```

6. **Verify the installation**:
   ```
   mvn -version
   ```

This should display the Maven version, confirming that it's installed correctly.


Execute the Maven targets to generate the artifacts

```
mvn clean package
```

The above maven target stroes the artifacts to the `target` directory. You can either execute the artifact on your local machine
(or) run it as a Docker container.

** Note: To avoid issues with local setup, Java versions and other dependencies, I would recommend the docker way. **


### Execute locally (Java 11 needed) and access the application on http://localhost:8080

```
java -jar target/spring-boot-web.jar
```

### Install Docker

https://docs.docker.com/engine/install/ubuntu/


### The Docker way

Build the Docker Image

```
docker build -t ultimate-cicd-pipeline:v1 .
```

```
docker run -d -p 8010:8080 -t ultimate-cicd-pipeline:v1
```

Hurray !! Access the application on `http://<ip-address>:8010`


## Next Steps

### Configure a Sonar Server locally

```
apt install unzip
adduser sonarqube
wget https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-9.4.0.54424.zip
unzip *
chmod -R 755 /home/sonarqube/sonarqube-9.4.0.54424
chown -R sonarqube:sonarqube /home/sonarqube/sonarqube-9.4.0.54424
cd sonarqube-9.4.0.54424/bin/linux-x86-64/
./sonar.sh start
```

Hurray !! Now you can access the `SonarQube Server` on `http://<ip-address>:9000` 


![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/202ea4d1-3c8c-443f-9137-0b9c9efde7a9)


