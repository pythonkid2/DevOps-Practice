# Table of Contents

- [Docker](#Docker)
- [Ansible](#Ansible)
- [Section 2](#section-2)
- [Section 3](#section-3)
- [Conclusion](#conclusion)

## Docker
<img width="852" alt="image" src="https://github.com/pythonkid2/DevOps-Practice/assets/100591950/9228624d-3088-4e0b-89c5-4111755d72cb">
<img width="873" alt="image" src="https://github.com/pythonkid2/DevOps-Practice/assets/100591950/da6388c2-d018-46de-bd8d-cac4c5d4e3a6">
<img width="881" alt="image" src="https://github.com/pythonkid2/DevOps-Practice/assets/100591950/269046fb-e082-4c87-9ca6-a9b508e909ac">
<img width="866" alt="image" src="https://github.com/pythonkid2/DevOps-Practice/assets/100591950/28e4b2d0-46f1-4c67-8ed0-80d4cbaf67a7">
<img width="861" alt="image" src="https://github.com/pythonkid2/DevOps-Practice/assets/100591950/48e7ff22-c3a1-4771-9cae-810539af8140">

## Ansible
1, What is configuration Mangement

Configuration management (CM) is essentially a practice for keeping computer systems, including servers, applications, and network devices, in a desired state. 

2, Ansible is a strong choice for configuration management due to its:
written in python, strong comminity, yamal is the  script language 

  Simplicity: Easy-to-learn YAML language.
  Agentless: No need to install software on managed systems.

3, Can you write an Ansible Playbook to install httpd service
and get it running ?

```
---
- hosts: all
  become: true
  tasks:
    - name: Install httpd package
      # Adjust 'name' for your package manager (e.g., apt, dnf)
      package:
        name: httpd
        state: present

    - name: Enable httpd service on boot
      service:
        name: httpd
        enabled: yes

    - name: Start httpd service
      service:
        name: httpd
        state: started
```

4, What is Ansible Dynamic Inventory ?

Ansible dynamic inventory automatically grabs your managed host list from external sources (cloud, CMDB) in real-time. This means no more manual updates, keeping your playbooks running on the latest and most accurate infrastructure.

It's like having a self-updating shopping list for your Ansible playbooks!

5, What is Ansible Galaxy command and why is it used

The Ansible Galaxy command, ansible-galaxy, is your tool for managing roles and collections in Ansible. It lets you:

- Install: Download roles and collections from the Ansible Galaxy website.
- Remove: Uninstall roles and collections from your system.
- List: See what roles and collections are already installed.
- Search: Find specific roles and collections on the Galaxy website.

Think of it as an app store for Ansible, where you can find pre-built tools (roles and collections) to automate various tasks, saving you time and effort.

6, What are handlers in Ansible and why are they used ?

Ansible handlers are special tasks that only run when specifically triggered by other tasks in your playbook. They are commonly used for actions that should only happen when a change is made, such as:

- Restarting a service after its configuration file is updated.
- Notifying administrators about successful or failed tasks.

### Why use handlers?
- Efficiency: They prevent unnecessary actions from running if no changes occur, improving performance.
- Idempotency: They ensure tasks only run when needed, maintaining a consistent state across multiple runs.

7, Ansible Protocol?

ssh for linux
winrm for windows

## Section 2

## Section 3
...
## Conclusion
...
