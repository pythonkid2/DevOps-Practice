# Table of Contents

- [Docker](#Docker)
- [Ansible](#Ansible)
- [Terraform](#Terraform)
- [Kubernetes](#Kubernetes)
- [Git](#Git)
- [Section 5](#section-5)
- [Conclusion](#conclusion)

## Docker

Q, Difference between expose & Publish

- EXPOSE is used in the Dockerfile to document the intended ports that the container should expose, while the -p or --publish option is used during runtime to map those container ports to specific ports on the host machine. The EXPOSE instruction alone doesn't make the container's ports accessible from the host; it's more like a hint to users or developers about the expected ports.

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

## Terraform

## Kubernetes

## Git

* **What is a Version Control System (VCS)?**
    * A VCS is used to manage and track changes to a project's source code over time. It enables collaboration among developers, maintains a history of changes, and facilitates the management of different versions of the codebase.

* **What is the difference between a Centralized and a Distributed Version Control System?**
    * A Centralized VCS has a single server that stores all versions of the files, whereas a Distributed VCS allows each user to have a complete copy of the repository, enabling them to work independently and facilitating easier collaboration without a central server.

* **Why is Git a popular choice for version control?**
    * Git is popular due to its distributed nature, speed, and efficiency in managing large projects. Its ability to handle branching and merging effectively, along with its robust set of tools for managing repositories, makes it a preferred choice for both small and large development teams.

* **What is Git?**
    * Git is a distributed version control system that allows multiple developers to work on the same codebase simultaneously. It tracks the changes made to files, enabling collaboration, and provides a mechanism for version control.

* **What is the difference between Git and GitHub?**
    * Git is a version control system that is used to manage and track changes in files. GitHub, on the other hand, is a web-based platform that provides hosting for Git repositories. It offers additional features such as issue tracking, pull requests, and project management tools.

* **What is a Git repository?**
    * A Git repository is a storage location where a Git project's files and their complete history are kept. It contains all the files, data, and metadata necessary to track the changes made to the project over time.

### Getting Started with Git

* **How do you create a new Git repository?**
    * To create a new Git repository, you can use the `git init` command in the root directory of your project. This initializes a new Git repository and allows you to start tracking changes in your project files.

* **What is a commit in Git?**
    * A commit in Git is a record of the changes made to a repository. It represents a snapshot of the repository at a specific point in time. Each commit has a unique identifier and contains information about the changes made, such as the author, timestamp, and a commit message.

* **How do you create a new branch in Git?**
    * To create a new branch in Git, you can use the command `git checkout -b <branch_name>`. This command creates a new branch and switches to it, allowing you to work on new features or fixes without affecting the main codebase.

### Collaboration with Git and GitHub

* **What is a pull request in GitHub?**
    * A pull request in GitHub is a way to propose changes to a repository. It allows developers to notify others about the changes they've pushed to a branch in a repository. Other developers can review the changes, discuss any potential modifications, and then decide whether to merge the changes into the main codebase.

* **How do you merge a branch in Git?**
    * To merge a branch in Git, you can use the command `git merge <branch_name>`. This command integrates the changes from the specified branch into the current branch.

* **What is the difference between 'git pull' and 'git fetch'?**
    * `git pull` fetches the changes from a remote repository and merges them into the current branch, while `git fetch` only fetches the changes from the remote repository but does not automatically merge them. This allows you to review the changes before merging them into your branch.

* **How do you revert a commit in Git?**
    * To revert a commit in Git, you can use the command `git revert <commit_hash>`. This creates a new commit that undoes the changes made in the specified commit while keeping a record of the reversal in the commit history.

### Advanced Git Concepts

* **What is the purpose of 'git merge' and how do you handle merge conflicts?**
    * 'git merge' integrates changes from one branch into another. Merge conflicts occur when Git is unable to automatically resolve differences between branches. Resolving merge conflicts involves manually editing the affected files to incorporate the desired changes and then committing the resolved files.

* **Explain the use of 'git stash' and 'git rebase' in Git.**
    * 'git stash' is used to temporarily store changes that are not ready to be committed, allowing you to work on something else. 'git rebase' is used to apply changes from one branch to another. It allows you to


Rebasing:
	Rebasing is the process of moving or combining a sequence of commits to a new base commit. It allows you to maintain a cleaner, more linear project history. When you rebase a branch onto another, Git moves the base of the branch to a different point. This can be useful for integrating the latest changes from a master branch into a feature branch before merging it back.
	
	git rebase <base_branch>: Rebase the current branch onto the specified base branch.
	git rebase -i <base_branch>: Interactive rebase that allows you to edit, squash, or reorder commits during the rebase process.

Reverting:
	Reverting in Git refers to the act of creating a new commit that undoes the changes of a previous commit. Unlike reset, which rewrites the commit history, revert creates a new commit that effectively reverses the specified commit's changes while preserving the commit history. Reverting is a safer option when you want to undo changes that have already been pushed to a remote repository without altering the commit history.
	
	git revert <commit_hash>: Create a new commit that undoes the changes introduced by the specified commit.
	git revert HEAD: Revert the most recent commit.
	git revert <commit_hash1> <commit_hash2>: Revert multiple specific commits.

Resetting:
	Resetting in Git is a powerful command that allows you to undo changes by moving the current branch to a specific commit. It can be used to alter the commit history, but it should be used with caution, especially when working with shared repositories. There are different modes of resetting, such as soft, mixed, and hard, each of which affects the staging area and working directory differently.
	
	git reset --soft <commit_hash>: Move the current branch to the specified commit, preserving changes in the working directory and staging area.
	git reset --mixed <commit_hash>: Reset the staging area to match the specified commit while preserving changes in the working directory.
	git reset --hard <commit_hash>: Discard all changes and reset the working directory to match the specified commit.


Walk me through the process of collaborating with others using local and remote repositories in Git and GitHub.
	Collaborating with others involves pushing your changes to a remote repository on GitHub, pulling changes from the remote repository, resolving any conflicts, and pushing the resolved changes back to the remote repository. GitHub's pull request feature facilitates code review and discussion before merging changes into the main branch.

+++
	
1. Different Types of Git Workflow Models:

Centralized Workflow:
	In the centralized workflow, all developers work on a single branch, typically the 'master' branch. Each developer clones the central repository, makes changes locally, and then pushes the changes to the central server. It's a simple workflow suitable for small teams and small projects where the complexity of branching is not necessary.

Feature Branch Workflow:
	In the feature branch workflow, each new feature is developed in a dedicated branch. Developers create a new branch for each feature, work on it independently, and then merge it back into the main branch upon completion. This model allows for parallel development, enabling developers to work on multiple features simultaneously without affecting the main codebase.

Gitflow Workflow:
	Gitflow is a branching model that defines a strict branching structure designed for larger projects. It involves maintaining separate branches for feature development, release preparation, and hotfixes. It promotes a systematic approach to version control, ensuring a smooth and controlled release process with clearly defined stages for feature development and bug fixing.

2. Git Hooks:

Git hooks are scripts that Git executes before or after certain events, such as committing, pushing, or merging. They allow you to automate tasks and enforce certain actions in the Git workflow, ensuring consistency and preventing errors.

3. Examples of Git Hooks and Their Practical Applications:

Pre-commit Hook:
	A pre-commit hook is triggered before the commit is created. It can be used to run automated checks, such as code linting or formatting, to ensure that all committed code meets predefined standards.

Pre-push Hook:
	The pre-push hook runs before the push operation to a remote repository. It can be used to perform tests, ensuring that the pushed code doesn't break any critical functionality and adheres to the project's guidelines.

Post-commit Hook:
	The post-commit hook executes after a commit is completed. It can be used to trigger actions like sending notifications or updating external services to reflect the latest changes made to the repository.

4. Best Practices for Committing, Branching, and Merging in Git:
Committing Best Practices:
	Write clear and descriptive commit messages that explain the changes made in the commit. Commit small and logical changes frequently rather than large, infrequent commits. Avoid committing incomplete or work-in-progress changes.

Branching Best Practices:
	Create feature branches for new development work and bug fixes. Use meaningful branch names that reflect the purpose of the development work. Regularly merge changes from the main branch into feature branches to keep them up to date.

Merging Best Practices:
	Test your changes locally before merging them into the main branch. Resolve any conflicts that arise during the merge process. Use merge commits or rebase to maintain a clean and linear project history. Communicate with your team before performing any significant merges to ensure a smooth integration of changes.

+++
ref-

https://www.simplilearn.com/tutorials/git-tutorial/git-interview-questions
## Section 5
...
## Conclusion
...
