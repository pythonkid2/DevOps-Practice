# Trivy

Trivy's Scanning Capabilities Encompass:

1. Container Images
2. Filesystems (ex: sourse code)
3. Dependency & Libraries (ex: pom.xml, package.jason)
4. Remote Git Repositories (scan repo, complete source code scanning without taking clone)
5. Kubernetes 

What trivy will solve?

1. Vulnerabilities in Base Images [docker image]
2. Outdated Software Components
3. Common Vulnerabilities and Exposures CVEs [eg- CVE-2022-12345 - a public datat base , people adding their findings]
4. Misconfigurations [K8 manifest file scanning]
5. Security Risks in File Systems [eg; sensitive data in FS]
6. Package Manager Vulnerabilities [Depenedency vuln]


## Installation 

https://aquasecurity.github.io/trivy/v0.52/getting-started/installation/


```trivy -v 
```
### scan repo 

trivy repo https://github.com/pythonkid2/Boardgame.git

![report](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/8e6f2a34-dc1d-405c-927c-4fa5e424e9e4)

generate report in a file to share - 
```
trivy repo --format table -o report.txt https://github.com/pythonkid2/Boardgame.git
```

--format -> format for report 
-o for to give file name 

### scan file system
```
trivy fs . 
```

trivy fs --format jason -o report.jason .

jason -anither possible format 

