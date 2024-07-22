
![Pipeline](https://github.com/user-attachments/assets/37893915-402e-4f4a-b71f-c5998eaa455d)


https://gitlab.com/ 

Create new project --> Import project --> Repository by URL -->  user name and tocken as pw

settings -> cicd --> runner --> new project runner -

New project runner -->Tags(way to identify the runner)

Register runner --> 


GitLab Runner must be installed before you can register a runner. 



Enter the GitLab instance URL (for example, https://gitlab.com/):
[https://gitlab.com]: https://gitlab.com/
Verifying runner... is valid                        runner=xsiTxBkGx
Enter a name for the runner. This is stored only in the local config.toml file:
[ip-172-31-25-195]: runner-1
Enter an executor: instance, ssh, parallels, virtualbox, docker, docker-windows, kubernetes, docker-autoscaler, custom, shell, docker+machine:
shell
Runner registered successfully. Feel free to start it, but if it's running already the config should be automatically reloaded!

Configuration (with the authentication token) was saved in "/home/ubuntu/.gitlab-runner/config.toml"


![image](https://github.com/user-attachments/assets/29dd4575-bb7c-4010-ae68-6a4299e203df)

Go to build --> pipeline editor  -->configure pipeline -->


stage/job

```


stages:          # List of stages for jobs, and their order of execution
  - install-tools
  - test


install-tools in vm:       # This job runs in the install-tools stage, which runs first.
  stage: install-tools
  script:
    - sudo apt install -y openjdk-17-jre-headless maven 
    - wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | sudo apt-key add -
    - echo deb https://aquasecurity.github.io/trivy-repo/deb $(lsb_release -sc) main | sudo tee -a /etc/apt/sources.list.d/trivy.list
    - sudo apt-get update
    - sudo apt-get install -y  trivy
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
```

create vm in aws as runner 

t2.medium will do

prereq
