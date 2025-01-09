for seccurity we need to make sure nothing is exposed (passwords, api,..etc)

checkout --> creating a local copy of appn source code inside the jenkins or any other cicd tool

compile --> Basically helping to find any syntax errors 

unit test cases --> finding out appn sourse code is woking fine as expected 

sonarqube --> 1, code quality check ( bugs, vulnerabilities, codesmell,..etc)
              2, code coverage (how much code is covered, is the test cases able to test all lines of code)

Trivy --> scan file system (config files vulnerabilities, checking any exposed pw or token

Build the app - we are getting app
      --> trivy scan artifact & dependencies (
       
publish artifact to repo

build docker image bfr pushing scan docker image with trivy 
       --> scan image(image will have artifact, base image& dependencies that will get scanned)

deploy to k8- (manifest files already scanned with trivy 

setup credentials ( create a seperate service acount with minimum privilage and creating credentila that can use in jenkins)

pen testing --> app is running on xyz.com
manually attacking that site with diff tools , and finding vulnerabilities 

monitor

---

1  - Development

main branch - production ready code 

ppod/pre-main ()

developers initially writing code to their local lap ->implimenting locally--> push to pre main branch

raising pull r/merge request  then archetect verifying the code and accepting the request

devops team creating a webhook 


2- Cicd 

checkpout-->complile-->unite test --> sonar--> trivy --> build --> nexus --> docker --> trivy -->docker hub ..> k8


3- monitoring 
grafana , prometheus 
