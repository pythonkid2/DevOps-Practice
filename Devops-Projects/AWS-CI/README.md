# AWS CI

![ci diagram](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/03517e9b-f4d6-4a60-abb3-f922afbb5e7f)

### go to codebuild 
project neme 
aws-ci-python-codebuild
Description - optional

Source
Source 1 - Primary  select GitHub

Public repository
Repository URL
https://github.com/pythonkid2/DevOps-Practice

Environment - 
Operating system - ubuntu 

Runtime(s) - Standard

Image - aws/codebuild/standard:7.0

Buildspec-

```
version: 0.2

env:
  parameter-store:
    DOCKER_REGISTRY_USERNAME: /myapp/docker-credentials/username
    DOCKER_REGISTRY_PASSWORD: /myapp/docker-credentials/password
    DOCKER_REGISTRY_URL: /myapp/docker-registry/url

phases:
  install:
    runtime-versions:
      python: 3.11
  pre_build:
    commands:
      - echo "Installing dependencies..."
      - pip install -r Devops-Projects/AWS-CI/simple-python-app/requirements.txt

  build:
    commands:
      - echo "Running tests..."
      - cd Devops-Projects/AWS-CI/simple-python-app
      - echo "Building Docker image..."
      - echo "$DOCKER_REGISTRY_PASSWORD" | docker login -u "$DOCKER_REGISTRY_USERNAME" --password-stdin "$DOCKER_REGISTRY_URL"
      - docker build -t "$DOCKER_REGISTRY_URL/$DOCKER_REGISTRY_USERNAME/simple-python-flask-app:latest" .
      - docker push "$DOCKER_REGISTRY_URL/$DOCKER_REGISTRY_USERNAME/simple-python-flask-app:latest"

  post_build:
    commands:
      - echo "Build completed successfully!"

```
add AmazonSSMFullAccess policy to role we created 

### AWS Systems Manager Parameter Store

Parameter details 
Name - /myapp/docker-credentials/username/
  nameopff application/whatsit /what u wanna store
Tier - standard 
type - secure string 

My current account
KMS Key ID - alias/aws/ssm


### CodePipeline

 Create pipeline

Source
Source provider  GitHub (Version 2)

connect to github


+++

Sure, here's a more structured documentation of your CI process:

---

## AWS CI Documentation

### Overview
This document outlines the Continuous Integration (CI) process for automating the build and deployment of a Python application using AWS CodeBuild, AWS Systems Manager Parameter Store, and AWS CodePipeline.

### CI Architecture Diagram
![CI Diagram](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/03517e9b-f4d6-4a60-abb3-f922afbb5e7f)

### CodeBuild Configuration

- **Project Name**: aws-ci-python-codebuild
- **Description**: (Optional)
- **Source**:
  - **Source Provider**: GitHub (Version 1)
  - **Repository URL**: [https://github.com/pythonkid2/DevOps-Practice](https://github.com/pythonkid2/DevOps-Practice)
- **Environment**:
  - **Operating System**: Ubuntu
  - **Runtime(s)**: Standard
  - **Image**: aws/codebuild/standard:7.0
- **Buildspec**:

```yaml
version: 0.2

env:
  parameter-store:
    DOCKER_REGISTRY_USERNAME: /myapp/docker-credentials/username
    DOCKER_REGISTRY_PASSWORD: /myapp/docker-credentials/password
    DOCKER_REGISTRY_URL: /myapp/docker-registry/url

phases:
  install:
    runtime-versions:
      python: 3.11
  pre_build:
    commands:
      - echo "Installing dependencies..."
      - pip install -r Devops-Projects/AWS-CI/simple-python-app/requirements.txt

  build:
    commands:
      - echo "Running tests..."
      - cd Devops-Projects/AWS-CI/simple-python-app
      - echo "Building Docker image..."
      - echo "$DOCKER_REGISTRY_PASSWORD" | docker login -u "$DOCKER_REGISTRY_USERNAME" --password-stdin "$DOCKER_REGISTRY_URL"
      - docker build -t "$DOCKER_REGISTRY_URL/$DOCKER_REGISTRY_USERNAME/simple-python-flask-app:latest" .
      - docker push "$DOCKER_REGISTRY_URL/$DOCKER_REGISTRY_USERNAME/simple-python-flask-app:latest"

  post_build:
    commands:
      - echo "Build completed successfully!"
```

- **IAM Role**: Add `AmazonSSMFullAccess` policy to the role used by CodeBuild.

### AWS Systems Manager Parameter Store

- **Parameter Details**:
  - **Name**: /myapp/docker-credentials/username/
  - **Description**: (Optional)
  - **Tier**: Standard
  - **Type**: Secure String
  - **KMS Key ID**: alias/aws/ssm (KMS key for encryption)

### CodePipeline Configuration

- **Create Pipeline**:
  - **Source**:
    - **Source Provider**: GitHub (Version 2)
    - Connect to GitHub repository for source code.
  - **Stages and Actions**: (Pending)

---

Feel free to customize and expand upon this documentation as needed for your specific requirements.
