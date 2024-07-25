# GitLab Notes for DevOps Learning

### Introduction to GitLab
- **GitLab** is a web-based DevOps lifecycle tool that provides a Git repository manager with wiki, issue-tracking, and CI/CD pipeline features.
- GitLab is a single application for the entire DevOps lifecycle, from project planning and source code management to CI/CD and monitoring.

### Key Features
- **Source Code Management (SCM)**: Git-based version control for managing your source code.
- **Continuous Integration/Continuous Deployment (CI/CD)**: Automated pipelines to build, test, and deploy your applications.
- **Issue Tracking**: Manage project issues, bug reports, and feature requests.
- **Wiki and Documentation**: Built-in wiki to document your project.
- **Container Registry**: Securely store and manage Docker images.

### Best Practices
- **Security**: Use environment variables for sensitive data.
- **Efficiency**: Use caching to speed up builds.
- **Modularity**: Break down large pipelines into smaller, reusable jobs and stages.
- **Monitoring**: Integrate monitoring tools like Prometheus and Grafana for real-time insights.

GitLab provides a robust platform for managing your DevOps lifecycle, from code versioning to automated deployments. Understanding and effectively utilizing its features can greatly enhance your DevOps workflows.

---

### Setting Up a CI/CD Pipeline with GitLab and a Self-Hosted Runner on an AWS VM

#### 1. Create a New GitLab Project
1. Go to [GitLab](https://gitlab.com/).
2. Click on `Create new project`.
3. Select `Import project`.
4. Choose `Repository by URL`.
5. Enter your repository URL, username, and token.

#### 2. Register a GitLab Runner
1. Ensure GitLab Runner is installed on your machine. For installation instructions, visit the [GitLab Runner installation page](https://docs.gitlab.com/runner/install/).

2. Go to `Settings -> CI/CD -> Runners` in your GitLab project.
3. Click on `New project runner`.
4. Add tags to identify the runner, such as `self-hosted`.

#### 3. Register the Runner on Your Machine
Run the following command to register the runner:

```sh
sudo gitlab-runner register
```

Follow the prompts:
- Enter the GitLab instance URL: `https://gitlab.com`
- Enter the registration token from your GitLab project.
- Enter a description for the runner: `runner-1`
- Enter the executor: `shell`

Configuration (with the authentication token) will be saved in `/home/ubuntu/.gitlab-runner/config.toml`.

![image](https://github.com/user-attachments/assets/29dd4575-bb7c-4010-ae68-6a4299e203df)

#### 4. Create an AWS VM as Runner
1. Launch an EC2 instance on AWS. A `t2.medium` instance type is recommended.
2. SSH into your EC2 instance.
3. Install GitLab Runner:

```sh
sudo curl -L --output /usr/local/bin/gitlab-runner https://gitlab-runner-downloads.s3.amazonaws.com/latest/binaries/gitlab-runner-linux-amd64
sudo chmod +x /usr/local/bin/gitlab-runner
sudo useradd --comment 'GitLab Runner' --create-home gitlab-runner --shell /bin/bash
sudo gitlab-runner install --user=gitlab-runner --working-directory=/home/gitlab-runner
sudo gitlab-runner start
```

4. Register the runner on the VM using the same `sudo gitlab-runner register` command and steps as above.

---

#### 5. Configure Pipeline in `.gitlab-ci.yml`

```yaml
stages:          # List of stages for jobs, and their order of execution
  - install-tools
  - test
  - security
  - Build
  - Docker
  - Kubernetes

install-tools-in-vm:       # This job runs in the install-tools stage, which runs first.
  stage: install-tools
  script:
    - sudo apt install -y openjdk-17-jre-headless maven 
    - wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | sudo apt-key add -
    - echo deb https://aquasecurity.github.io/trivy-repo/deb $(lsb_release -sc) main | sudo tee -a /etc/apt/sources.list.d/trivy.list
    - sudo apt-get update
    - sudo apt-get install -y trivy
    - sudo apt install docker.io -y && sudo chmod 666 /var/run/docker.sock
    - sudo snap install kubectl --classic
  tags:
    - self-hosted

unit_testing:
  stage: test
  script:
    - mvn test
  tags:
    - self-hosted

trivy-fs-scan:
  stage: security
  script:
    - trivy --version
    - trivy fs --format table -o fs.html .
  artifacts:
    paths:
      - fs.html
  tags:
    - self-hosted

sonarqube-check:
  stage: security
  image: 
    name: sonarsource/sonar-scanner-cli:latest
  variables:
    SONAR_USER_HOME: "${CI_PROJECT_DIR}/.sonar"  # Defines the location of the analysis task cache
    GIT_DEPTH: "0"  # Tells git to fetch all the branches of the project, required by the analysis task
  cache:
    key: "${CI_JOB_NAME}"
    paths:
      - .sonar/cache
  script: 
    - sonar-scanner
  allow_failure: true
  only:
    - main

build-the-app:
  stage: Build
  script:
    - mvn package
  tags:
    - self-hosted
  only:
    - main

docker-build_tag_push:
  stage: Docker
  script:
    - docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD
    - mvn package
    - docker build -t mjcmathew/boardgamegitlab:latest .
    - docker push mjcmathew/boardgamegitlab:latest
  tags:
    - self-hosted
  only:
    - main
  
deploy-in-k8:
  stage: Kubernetes
  variables:
    KUBECONFIG_PATH: /home/ubuntu/.kube/config
  before_script:
    - mkdir -p $(dirname "$KUBECONFIG_PATH")
    - echo "$KUBECONFIG_DATA" | base64 -d > "$KUBECONFIG_PATH"
    - export KUBECONFIG="$KUBECONFIG_PATH"
  script:
    - kubectl apply -f deployment-service.yaml
  tags:
    - self-hosted
  only:
    - main
```

### Configure Pipeline in GitLab
1. Go to your GitLab project.
2. Navigate to `Build -> Pipeline Editor`.
3. Configure your pipeline using the `.gitlab-ci.yml` file created above.

![Pipeline](https://github.com/user-attachments/assets/37893915-402e-4f4a-b71f-c5998eaa455d)

---

### SonarQube Integration

To set up SonarQube as a container in the VM, use the following commands:

```sh
docker run -d --name sonar -p 9000:9000 sonarqube:lts-community
```

#### Setting up SonarQube with GitLab
1. **Login to SonarQube**
2. **From GitLab - Configuration Name:**
   - **Boardgame**
   - **GitLab API URL:**

#### For Creating Token:
- **Settings -> Access Tokens -> Add New Token**
  - Name: `sonar`
  - Select a role: `reporter`
  - Select scope

![image](https://github.com/user-attachments/assets/ff6da81f-477b-4174-b17e-4f78ce65b3b2)

#### Define the SonarQube Token Environment Variable:
In GitLab, go to `Settings > CI/CD > Variables` to add the following variable and make sure it is available for your project:
- **Key:** `SONAR_TOKEN`
- **Value:** Enter an existing token, or a newly generated one.
- **Uncheck the Protect Variable checkbox.**
- **Check the Mask Variable checkbox.**

#### Define the SonarQube URL Environment Variable:
Still in `Settings > CI/CD > Variables`, add a new variable and make sure it is available for your project:
- **Key:** `SONAR_HOST_URL`
- **Value:** `http://3.16.38.115:9000`
- **Uncheck the Protect Variable checkbox.**
- **Leave the Mask Variable checkbox unchecked.**

Create or update your `.gitlab-ci.yml` file with the given content.

---

### Kubernetes Integration for EKS

#### Generate Kubeconfig File:
Use the `aws eks update-kubeconfig` command to generate or update the kubeconfig file for your EKS cluster.

```sh
aws eks update-kubeconfig --region <region-code> --name <cluster-name>
```

#### Set Up GitLab CI/CD:
To use the kubeconfig file in GitLab CI/CD, follow these steps:

**Using GitLab CI/CD Variables**

#### Step 1: Encode the Kubeconfig File
Encode the kubeconfig file to base64.

```sh
base64 ~/.kube/config
```

Copy the base64 encoded content.

#### Step

 2: Add Kubeconfig as a Secret Variable in GitLab
- Go to `Settings > CI/CD > Variables`.
- Add a new variable.
  - **Key:** `KUBECONFIG_DATA`
  - **Value:** Paste the base64 encoded kubeconfig content.
  - **Protected:** Leave unchecked.
  - **Masked:** Leave unchecked.

---

### Images

Below are some reference images for setting up the pipeline and configuring the environment.

1. **New Project Runner Configuration**
![image](https://github.com/user-attachments/assets/29dd4575-bb7c-4010-ae68-6a4299e203df)

2. **SonarQube Token Creation**
![image](https://github.com/user-attachments/assets/ff6da81f-477b-4174-b17e-4f78ce65b3b2)

3. **Pipeline Example**
![Pipeline](https://github.com/user-attachments/assets/37893915-402e-4f4a-b71f-c5998eaa455d)

This guide provides an end-to-end setup for GitLab CI/CD, integrating various tools like Docker, Kubernetes, and SonarQube to create a robust DevOps pipeline. Happy learning!

---

