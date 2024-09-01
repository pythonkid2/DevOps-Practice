# Voting Application

![image](https://github.com/user-attachments/assets/f6c853c6-b58d-4a98-a05e-49922402018d)

Create new azure devops project -
![Azure devops project adding page](https://github.com/user-attachments/assets/b1aaa362-6cef-4b96-9a62-f02212a3ce88)
clone the github repo to azure devops repo
![import repo to azure devops](https://github.com/user-attachments/assets/3c2e5f37-b6e8-4369-9b10-4b950dd2183b)
![imported](https://github.com/user-attachments/assets/66bcb94e-1ca6-4447-b3e1-4b71941d8fda)

## Add Resource group

Home --> Resource groups

![image](https://github.com/user-attachments/assets/a2dff650-9543-4664-927a-8376d8ea955c)

## Set up container registry

go to azure and create container registry 

![image](https://github.com/user-attachments/assets/69fa5895-d0eb-40ea-9273-17630641e11b)

![image](https://github.com/user-attachments/assets/ba8c020b-900d-456f-8596-a54b116eecb7)

## Create VM

![image](https://github.com/user-attachments/assets/771c817f-9a51-4ec4-ba84-64e2aae986da)

![image](https://github.com/user-attachments/assets/91d0696a-3fac-4437-808c-200d0cac574f)

## Create 3 pipelines 

![basic of pipeline](https://github.com/user-attachments/assets/185d028f-4a66-4447-b90a-06ae76a82733)
In pipe line we have triggers - > when should the pipeline starts 
we are using path based trigger here 
stages- jobs-steps
variables 


### go to pipeline and create 1st pipeline for result application

![image](https://github.com/user-attachments/assets/dec4ef0c-fffe-41fd-b7a7-199fd1802626)

select the code 

![image](https://github.com/user-attachments/assets/c8f45d69-ad53-49b8-bdc3-d4f7a930f758)

Configure pipeline

<img width="959" alt="image" src="https://github.com/user-attachments/assets/3446af04-6339-468a-b0b4-862bb7ce005c">
sign in with git hub 

![image](https://github.com/user-attachments/assets/a301d3bd-986f-4c5f-8b20-5c5b7fafc000)


### go to azure pipeline doccumentation

> Agents & pools --> Self-hosted Linux agents

https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/linux-agent?view=azure-devops

![image](https://github.com/user-attachments/assets/52d958dd-4dec-435b-86de-06306640ab95)

![image](https://github.com/user-attachments/assets/f0d94215-f50b-471d-9917-d561a0d3ab42)
add agent
![image](https://github.com/user-attachments/assets/49124f0a-f7df-4b5c-a8d3-363afb8bf591)

<img width="958" alt="image" src="https://github.com/user-attachments/assets/e004c212-020c-4b94-8a62-ff008ada2c8d">
copy paste these commands to vm

<img width="760" alt="image" src="https://github.com/user-attachments/assets/989a63d5-c2fd-486a-934d-fd8b92d9c884">

### create the token

go to azure devops --> User settings --> Personal Access Tokens

<img width="395" alt="image" src="https://github.com/user-attachments/assets/98975b3d-f0d9-430b-b54e-7771bda2b977">

```
sudo apt install docker.io -y
```
```
 ./run.sh
```
![image](https://github.com/user-attachments/assets/4f1b4e08-5c8c-45cc-9539-11fd9bc7962e)

## set up 3 pipelines for 3 services 

![image](https://github.com/user-attachments/assets/0e4dc60c-2b1f-401e-b0ff-c6650956f43a)

```
trigger:
  paths:
    include:
      - result/*

resources:
- repo: self

variables:
  # Container registry service connection established during pipeline creation
  dockerRegistryServiceConnection: '666224ef-8a53-4449-883c-8fe10158a30d'
  imageRepository: 'resultapp'
  containerRegistry: 'vottingapllication.azurecr.io'
  dockerfilePath: '$(Build.SourcesDirectory)/result/Dockerfile'
  tag: '$(Build.BuildId)'

# Specify the agent pool
pool:
  name: 'azureagent'  # Use your self-hosted agent pool name

stages:
- stage: Build
  displayName: Build the docker container stage
  jobs:
  - job: Build
    displayName: Build
    pool:
      name: 'azureagent'  # Self-hosted agent pool
    steps:
    - task: Docker@2
      displayName: Build and push an image to container registry
      inputs:
        containerRegistry: 'vottingApllication'
        repository: '$(imageRepository)'
        command: 'build'
        Dockerfile: '$(dockerfilePath)'
        tags: '$(tag)'

- stage: Push
  displayName: Push to Azure Container Registry
  jobs:
  - job: Push
    displayName: Push
    pool:
      name: 'azureagent'  # Self-hosted agent pool
    steps:
    - task: Docker@2
      displayName: Push image to container registry
      inputs:
        containerRegistry: 'vottingApllication'
        repository: '$(imageRepository)'
        command: 'push'
        tags: '$(tag)'

```

## Continuous Delivery

###### Home > Kubernetes services > Create Kubernetes cluster

![image](https://github.com/user-attachments/assets/e1bd9f53-8f6e-4a9b-9a29-d2e9611f52be)
![image](https://github.com/user-attachments/assets/d7ea3ce9-2e81-44d3-8a58-f823fb216451)

###### Update node pool

![image](https://github.com/user-attachments/assets/00ce6d25-8e90-4cf1-8e25-65e5f2442e0b)

![image](https://github.com/user-attachments/assets/99a65db4-5f93-4a9a-ad1a-5765dbe931cc)





