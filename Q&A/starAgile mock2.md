
# Devops

**advantages of devops**

DevOps, which combines development and operations, aims to shorten the systems development life cycle and provide continuous delivery with high software quality. Some key advantages of implementing DevOps practices include:
      
**Faster delivery of features** : DevOps enables faster development and deployment of software, allowing for quicker adaptation to market changes and customer needs.

**Increased frequency of deployments**: By automating the software delivery process, DevOps facilitates frequent and reliable software releases, reducing the time between fixes and improving customer satisfaction.

 **Higher quality products**: Through continuous integration and testing, DevOps helps to identify and address issues earlier in the development process, resulting in higher quality software products.
 
**Improved collaboration**: DevOps promotes collaboration between development, operations, and other teams, fostering a culture of shared responsibility and collective ownership.

**Greater efficiency and productivity**: Automation of manual tasks and streamlined processes lead to improved efficiency, enabling teams to focus on high-value tasks and innovation.

**Enhanced customer experience**: With faster delivery cycles and more reliable software, DevOps helps in delivering a better experience to end-users, ultimately increasing customer satisfaction and loyalty.

**Reduced risk**: Continuous monitoring and feedback loops in the DevOps process help in identifying and addressing issues promptly, minimizing the risk of failures and reducing downtime.

What is **CI (Continuous Integration)**?

**CI (Continuous Integration)**
It's the practice of developers regularly merging their code changes into a central repository, which is then verified by automated build and tests to catch bugs early.

**Continuous Delivery**

**Continuous Delivery** : It's the practice of automatically preparing code changes for a release to production, ensuring that your software can be deployed at any time with minimal risk.'


# Git

**what is version control system**
A version control system (VCS) is a software tool that helps track and manage changes to files, especially in software development. It allows multiple developers to collaborate, maintaining a record of changes made, facilitating collaboration, enabling reversion to previous versions, and managing different versions of files. Examples include Git, Subversion (SVN), and Mercurial.

**Source Code Management**
Source Code Management (SCM) is a broader term encompassing the management of changes to any kind of information source, not just software source code. It involves tracking and controlling changes to documents, programs, and other information assets. 

**git pull and git fetch**

git pull: This command is used to fetch the changes from the remote repository and merge them into your local branch. It is essentially a combination of git fetch and git merge. When you run git pull, it automatically fetches the changes from the remote branch and merges them into your current local branch.
            
            git pull <remote>

git fetch: This command only fetches the changes from the remote repository and stores them in your local repository, without automatically merging them into your current branch. It allows you to see what changes are present in the remote branch and gives you the opportunity to decide how to integrate those changes into your local branch.
            
            git fetch <remote>

**git log**
The git log command is used to display the commit history in the repository. It shows the commit logs starting from the latest commit, allowing you to view information such as commit hashes, author details, dates, and commit messages. Here's an example of how to use it: $ git log

git log using various options. For example, you can use options like --oneline to display each commit on a single line or --graph to visualize the commit history as a graph.

**git status**
Use `git status` to list all new or modified files that haven't yet been committed.

**git commit**
  In Git, the git commit command is used to save the changes to the local repository. When you run git commit, it takes the staged snapshot and commits it to the project history. 

**To create a new branch in Git**	  
    	git branch <branch_name>

After creating the branch, you can switch to the newly created branch using the following command: 
	git checkout <branch_name>
	
Alternatively, you can combine both commands into one using the -b flag to create and switch to the new branch in a single step: 
	git checkout -b <branch_name>

**git merge**
The git merge command in Git is used to integrate changes from one branch into another. It combines multiple sequences of commits into one unified history. When you want to merge one branch into another, you typically use the following syntax:

**git rebase**
The git rebase command in Git is used to reapply a series of commits from one branch to another. Unlike git merge, which integrates the changes of one branch into another, git rebase moves the entire feature branch to a new base commit. This effectively changes the base of the branch, allowing for a cleaner, more linear project history.

**git reset**
The **git reset** command in Git is a powerful tool that is used to reset the current state of the repository. **It can be used to undo changes or move the current branch to a different state**. Here are the key options with the git reset command:

git reset --soft: Moves the HEAD to the specified commit, but leaves the changes in the staging area. It does not affect the working directory.

git reset --mixed: This is the default option if no mode is specified. It moves the HEAD to the specified commit and updates the staging area but does not affect the working directory. This is useful when you want to unstage changes.

git reset --hard: Moves the HEAD to the specified commit and updates both the staging area and the working directory. Be cautious when using this option as it discards all changes since the specified commit.

Here is an example of how to use the git reset command:
		git reset --soft HEAD~3
**git revert**
used to create a new commit that undoes the changes from a previous commit. This is useful if you want to create a new commit that effectively reverses the changes introduced by an earlier commit, while keeping a record of the reversion. Here's how you can use it:
	git revert <commit-hash>

**Difference between Revert, Rebase, and Reset:**

**Git Revert** : It creates a new commit that undoes the changes from a specific previous commit. It is a safe way to undo changes on a public branch since it does not alter the existing commit history. Reverting is typically used to fix a mistake in a commit without altering the commit history.

**Git Rebase** : Rebase is a way to integrate the changes from one branch onto another. It works by moving the starting point of the branch to a different commit, applying the commits from one branch to another, and then reapplying the commits from the original branch on top of the new base. This can be used to maintain a linear project history. Rebase should be used carefully, especially when working with shared branches, as it rewrites commit history and can cause conflicts for other users.

**Git Reset** : Reset is used to reset the current HEAD to a specified state. It can be used to undo changes or move the current branch to a different commit. There are three types of resets: soft, mixed, and hard.

	Soft reset keeps the changes in the working directory.
	Mixed reset keeps the changes in the working directory but resets the staging area to the specified commit.
	Hard reset discards all changes in the working directory and staging area, reverting the repository to the specified commit.

In summary, revert creates a new commit to undo changes, rebase integrates changes from one branch onto another, and reset is used to move the current branch to a different commit or undo changes with various degrees of aggressiveness. Each command serves a different purpose and should be used according to the specific requirements of the Git workflow.


# Maven

maven commands

	
Maven is a powerful build automation tool used primarily for Java projects. It simplifies and standardizes the build process, managing project dependencies, and providing a uniform build system. Here are some commonly used Maven commands:

	mvn clean: This command cleans the project by deleting the target directory and removing all compiled class files and resources.

	mvn compile: It compiles the source code of the project.

	mvn test: This command runs the unit tests for the project.

	mvn package: It packages the compiled code of the project into a distributable format, such as a JAR, WAR, or EAR file.

	mvn install: This command installs the project's package into the local repository, making it available for other projects that need to use it as a dependency.

	mvn deploy: It deploys the built artifact to the remote repository for sharing with other developers and projects.

	mvn site: This command generates the project's website documentation.

	mvn archetype:generate: It generates a new project from an existing template, known as an archetype.

	mvn dependency:tree: This command displays the project's dependency tree.

	mvn help: It displays help information on Maven commands and options.

**mvn package** : This is a Maven build lifecycle phase, specifically the package phase. When you run mvn package, Maven will execute all phases up to and including the package phase. In this phase, Maven will create the JAR or WAR file of your project based on the configuration in the project's POM (Project Object Model) file. This does not include the installation of the artifact into the local repository or a remote repository.

**The POM (Project Object Model)** file
Essential configuration file used in Apache Maven-based projects. It is an XML file that contains information about the project and configuration details to build the project. The POM file provides details about the project's structure, dependencies, build settings, and other essential information required for Maven to build the project correctly.

key components of POM.xml

**Project information** : This includes the project's group ID, artifact ID, version, and other descriptive information.
**Dependencies** : These are the external libraries or modules required by the project.
**Build settings** : This includes information about plugins, goals, and other configurations for building the project.
**Repositories** : These are the locations where Maven can look for dependencies needed to build the project.

**The Maven build and Maven package**
	
 The Maven build and Maven package commands are both used in the context of building and packaging a Maven project, but they serve different purposes:

**Maven Build** Command: The mvn build command is a generic command that is used to build the project. It triggers the default lifecycle up to the package phase. This means it will compile the source code, run any tests, and package the compiled code into a JAR, WAR, or any other format defined in the project configuration.

**Maven Package** Command: The mvn package command is specifically used to execute the package phase of the Maven build lifecycle. This phase is responsible for taking the compiled code and packaging it into its distributable format, such as a JAR, WAR, or EAR file, depending on the type of the project.

**In summary, while the mvn build command is more generic and triggers the build process up to the package phase, the mvn package command specifically executes the package phase to create the distributable package as defined by the project configuration.**	

# Selenium

**advantages of selenium**

Selenium is a widely used open-source testing tool for web applications. Some of its advantages include:

**Cross-Browser Compatibility**: Selenium supports various browsers like Chrome, Firefox, Internet Explorer, Safari, and Opera. This cross-browser compatibility ensures that the web application works consistently across different browsers.
**Language Support**: Selenium provides support for multiple programming languages such as Java, Python, C#, Ruby, and more. This flexibility allows developers and testers to write test scripts in their preferred language.
**Open-Source Nature**: Selenium is an open-source tool, making it cost-effective and easily accessible. The community support and regular updates ensure that it stays relevant and competitive in the dynamic software testing landscape.
**Platform Compatibility**: Selenium can run on different operating systems like Windows, macOS, and Linux. This platform independence makes it a versatile tool for testing web applications developed on various platforms.
**Integration with CI/CD**: Selenium can be seamlessly integrated with Continuous Integration/Continuous Deployment (CI/CD) tools like Jenkins, Bamboo, and TeamCity, enabling automated testing in the deployment pipeline.
**Extensibility**: Selenium provides the flexibility to extend its functionalities through custom plugins and extensions. This extensibility allows users to incorporate additional features and integrate Selenium with other tools or frameworks.
**Support for Parallel Testing**: Selenium supports parallel testing, enabling the execution of multiple test cases simultaneously. This feature helps to speed up the testing process and provides faster feedback on the application's behavior.
**Large Community Support**: Selenium has a large and active user community that contributes to its development and shares best practices, tips, and solutions. This extensive community support ensures that users can find solutions to common issues and challenges while using Selenium.

**TestNG**

TestNG is a testing framework inspired by JUnit and NUnit but introducing new functionalities that make it more powerful and easier to use, especially for complex and integrated test scenarios. It is designed to cover all categories of tests: unit, functional, end-to-end, integration, etc., and it is suitable for all types of applications.

	Here are some key features and components of the TestNG framework:

**Annotations**: TestNG provides various annotations like @Test, @BeforeMethod, @AfterMethod, @BeforeClass, @AfterClass, etc., to facilitate the creation of test cases and the execution of setup and teardown operations.
**Assertions**: TestNG provides a rich set of assertion methods for verifying the expected behavior of the application during the test execution.
**Grouping and Prioritizing**: TestNG allows you to group test methods and prioritize the execution order, which is particularly useful when dealing with multiple test cases.
**Parameterization** : TestNG supports data-driven testing, allowing you to run the same test method with different sets of data.
**Listeners**: TestNG provides a way to implement custom listeners that can perform actions based on the events that occur during the test execution.
**Test Configuration**: TestNG allows the configuration of test suites and provides flexibility in defining suite parameters, test dependencies, parallel execution, and more.

**launch a browser using Selenium in Java**
To launch a browser using Selenium in Java, you need to have the appropriate **Selenium WebDriver** libraries and the corresponding driver executable for the browser you intend to automate. Here's a basic example using the Chrome browser:

**Download the Selenium WebDriver** for Java from the Selenium website and add it to your Java project's build path.

**Download the ChromeDriver executable from the ChromeDriver website** and place it in a location accessible by your Java project.

	Here's a basic code snippet for launching the Chrome browser using Selenium WebDriver in Java:

```markdown
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class SeleniumExample {
    public static void main(String[] args) {
        // Set the path to the ChromeDriver executable
        System.setProperty("webdriver.chrome.driver", "path_to_chromedriver_executable");

        // Create an instance of the ChromeDriver
        WebDriver driver = new ChromeDriver();

        // Open a website
        driver.get("https://www.example.com");

        // Perform any required operations

        // Close the browser
        driver.quit();
	}
}
```
**WebDriver driver = new ChromeDriver();**
By using this line of code, you can create a new instance of the ChromeDriver, which then allows you to control the Chrome browser through your Java code using Selenium WebDriver.
**why driver in selenium** 
In Selenium, the term "driver" refers to the software component that facilitates the communication between your test script and the browser. It acts as a bridge between the automation script and the browser's native support for automation (such as Chrome, Firefox, or others). The driver is a crucial part of the Selenium framework as it enables you to control the browser, navigate to URLs, and interact with web elements.	

# Jenkins

**Polling the SCM in jenkins**	

Polling the SCM (Software Configuration Management) in Jenkins refers to the process of periodically checking the source code repository for any changes. Jenkins can be configured to check the repository at a specified interval, and if changes are detected, it triggers a build process.

To enable polling the SCM in Jenkins, follow these steps:

	Go to your Jenkins dashboard and select the desired project.
	Click on "Configure" to access the project configuration.
	Look for the "Build Triggers" section.
	Check the option that allows polling the SCM. You may need to specify the frequency of the polling.
	Save the configuration.
	
Once enabled, Jenkins will check the source code repository at the specified interval. If it detects any changes, it will trigger a build process automatically. This can be an effective way to ensure that your project is continuously built and tested whenever there are updates in the source code repository.

**How to add slave connection in jenkins**
	
 Set up the Slave Node:

	Ensure that the slave machine is reachable from the Jenkins master.
	Install Java and the necessary tools on the slave machine if they are not already installed.
	Ensure that the slave machine has the required network access to the Jenkins master.
	
Configure Jenkins Master:

	Log in to your Jenkins dashboard as an administrator.
	Click on "Manage Jenkins" on the left-hand side.
	Select "Manage Nodes and Clouds."
	Click on "New Node" or "New Agent" to create a new node.
	Provide a node name and select the option for a permanent agent.
	Enter the necessary details such as the number of executors, remote root directory, labels, and usage.
	Choose the appropriate launch method, such as via Java Web Start or SSH.
	Enter the specific details required for the selected launch method.
	Save Configuration and Connect:

	Save the configuration of the node.
	Jenkins will provide you with a command or instructions on how to launch the agent on the slave machine. Execute this command on the slave machine to connect it to the Jenkins master.
	Verify the Connection:

	Once the connection is established, the slave node should appear in the Jenkins dashboard under "Nodes" or "Agents."
	You can then use this slave node to distribute build and test jobs from the Jenkins master.

**how to add custom plugin in jenkin**
Download the Plugin:
Locate the plugin you wish to install from the Jenkins Plugin Index or from a reliable source. Ensure that the plugin is compatible with your Jenkins version.

Install the Plugin:
	Log in to your Jenkins dashboard as an administrator.
	Click on "Jenkins" at the top left to go to the dashboard.
	In the left sidebar, select "Manage Jenkins."
	Click on "Manage Plugins."
	Navigate to the "Available" tab.
	Find the plugin you want to install, select the checkbox next to its name, and click "Install without restart" or "Download now and install after restart."
	Restart Jenkins (If Required):
        If the plugin installation requires a Jenkins restart, a notification will appear. Follow the instructions to restart Jenkins.
	Configure the Plugin:
	Once the plugin is installed, you may need to configure it based on your requirements. Check the plugin documentation or the Jenkins wiki for instructions on how to configure the specific plugin you have installed.

**Post build actions in jenkins** 
In Jenkins, post-build actions are the additional operations or tasks that you can configure to be executed after the main build step has completed. 
Some common post-build actions in Jenkins include:
**Archive the artifacts: Publish JUnit test result report: Triggering other projects: Sending email notifications: Post to Slack or other communication platforms: 
Publishing build reports and metrics:Executing shell scripts or batch commands**

**Plugins in Jenkins**
**Plugins in Jenkins** are software components that extend the functionality of the Jenkins automation server. They allow you to integrate additional features and tools into your Jenkins environment, enabling you to customize and enhance your CI/CD (Continuous Integration/Continuous Deployment) pipelines.
 
**available anotations in jenkins**
Jenkins supports various annotations and directives that can be used within Jenkinsfiles, which are used to define Jenkins pipelines. These annotations and directives provide instructions to Jenkins on how to execute the pipeline stages and steps. Some of the commonly used annotations in Jenkins are as follows:

agent: Specifies the agent to use for running the pipeline. For example, agent any indicates that the pipeline can be run on any available agent.
options: Provides various configuration options for the pipeline, such as timeouts, build discard policies, and more.
parameters: Defines input parameters that can be used to trigger the pipeline manually or to provide user-specified values during the pipeline execution.
stages: Defines the different stages of the pipeline, allowing you to organize the pipeline steps into logical groups.
steps: Represents the individual steps to be executed within a stage, such as building, testing, or deploying the application.
environment: Defines the environment variables that should be available to the steps within the pipeline.
post: Specifies actions that should be performed after the stages have been executed, such as sending notifications, archiving artifacts, or triggering other pipelines.
when: Allows conditional execution of certain stages or steps based on specific conditions, such as the result of a previous step or a predefined variable.

freestyle project vs pipe line

<table border="0">
 <tr>
    <td><b style="font-size:30px">Free style</b></td>
    <td><b style="font-size:30px">Pipeline</b></td>
 </tr>
 <tr>
    <td>Simple Configuration: Freestyle projects in Jenkins are simple and easy to set up. They allow users to configure build steps, post-build actions, and triggers through an intuitive user interface.

Limited Flexibility: Freestyle projects have limited flexibility compared to Pipeline projects. They are suitable for straightforward build and deployment tasks but may not be suitable for complex or advanced workflows.

Graphical User Interface (GUI) Configuration: Freestyle projects are configured primarily through the Jenkins web interface, making them more accessible to users who are not familiar with scripting or coding.

Plugin-based Customization: Freestyle projects allow users to incorporate various Jenkins plugins to extend functionality, such as source code management, build triggers, and post-build actions.</td>
    <td>Scripted or Declarative Pipeline: Pipeline projects in Jenkins allow for the creation of continuous delivery pipelines using a domain-specific language (DSL). They can be written in either Scripted or Declarative syntax, providing more advanced control and customization options.

Advanced Workflows: Pipelines support complex and advanced workflows, allowing users to define continuous integration and continuous deployment (CI/CD) pipelines as code. This enables the automation of complex tasks and the integration of various tools and services.

Version Control Integration: Pipeline projects can be stored in source control repositories, making it easier to manage and version the pipeline code alongside the application source code.

Better Visualization and Error Handling: Pipelines offer better visualization of the entire build process, including detailed logs, stage views, and error handling capabilities, which help in identifying and resolving issues more effectively.</td>
 </tr>
</table>

**"artifact" and "package"** refer to different concepts:

**Artifact**: In Maven, an artifact refers to a uniquely identifiable component, such as a JAR, WAR, or ZIP file that is produced as a result of the build process. It is essentially a file, usually a JAR file, which gets installed into a Maven repository. Each artifact has a specific coordinate that uniquely identifies it, consisting of a group ID, artifact ID, version, and packaging type. Maven artifacts are identified and managed using these coordinates, allowing for easy dependency management and build automation.

**Package**: The term "package" in Maven refers to the type of artifact that is being produced during the build process. It indicates the format in which the project is being packaged. Maven supports various packaging types, such as JAR, WAR, EAR, and others. The packaging type is specified in the project's configuration file (pom.xml) using the <packaging> element. Maven plugins use this information to generate the appropriate artifact during the build process. For example, if the packaging type is set to "jar," Maven will create a JAR artifact as the output.

In summary, "artifact" in Maven refers to the produced file or component that is managed and identified based on its coordinates, while "package" refers to the type of artifact that is being generated during the build process, which determines the format of the resulting file, such as JAR, WAR, or others.


# Docker

**cmd , entry point** in docker file

	In a Dockerfile, the CMD instruction is used to specify the command that should be executed when the Docker container starts. It defines the default command for the container, which can be overridden by providing a command at the end of the docker run command.
	
	The ENTRYPOINT instruction, on the other hand, is used to set the main command that is always executed when the container starts. Unlike CMD, the parameters are not ignored when providing a command to the docker run command.

Other commands 

**FROM** : Specifies the base image for subsequent instructions. It is usually the first instruction in a Dockerfile.
**RUN**: Executes commands in a new layer and creates a new image. This is used to install packages, run scripts, or perform any other actions during the build process.
**COPY**: Copies files or directories from the build context into the container's own filesystem at a specified location.
**ADD**: Similar to COPY, but it also supports URLs and automatically unpacks local tar files.
**WORKDIR**: Sets the working directory for any RUN, CMD, ENTRYPOINT, COPY, and ADD instructions that follow it in the Dockerfile.
**EXPOSE**: Informs Docker that the container listens on the specified network ports at runtime.
**ENV**: Sets the environment variable to a specific value inside the container.
**ARG**: Defines a variable that users can pass at build-time to the builder with the docker build command using the --build-arg flag.
**VOLUME**: Creates a mount point with the specified name and marks it as holding externally mounted volumes from the native host or other containers.
**USER**: Sets the user name or UID to use when running the image.
**HEALTHCHECK**: Tells Docker how to test a container to check that it is still working.

Difference between **container and image**
**Image**:
An image is a lightweight, standalone, and executable software package that includes everything needed to run a piece of software, including the code, runtime, system tools, system libraries, and settings. It is essentially a snapshot of a Docker container.

Images are read-only templates used to create Docker containers. They can be built from a Dockerfile using the docker build command or pulled from a registry using the docker pull command.

Images are used as the basis for creating containers. They can be versioned and distributed to other systems or users.

**Container:**
A container is a runtime instance of an image—basically, a running process isolated from the host and other containers. Containers are lightweight, portable, and self-sufficient, allowing applications to be easily deployed and run consistently in various environments. Each container is created from a specific image and represents a running instance of that application, providing an isolated environment for running the application. 

In summary, images are the blueprints used to create containers, while containers are the actual runtime instances of those images. Containers provide a consistent environment for running applications, and images provide a way to package and distribute software with all its dependencies.

**Types of docker networks ?**
Docker provides several types of networks to facilitate communication between containers and between containers and the outside world. These networks offer different features and functionalities to meet various use cases. Here are some of the types of Docker networks:

**Bridge network**: This is the default network that enables communication between containers on the same Docker daemon host. Containers connected to the same bridge network can communicate with each other via IP addresses. It also allows the containers to communicate with external networks using NAT (Network Address Translation).
**Host network**: With the host network mode, a container shares the network namespace with the Docker host. This means the container does not have network isolation from the host and can use the host's network directly. This can be beneficial for performance-critical applications that require full access to the host's network stack.
**Overlay network**: This type of network allows containers to communicate across multiple Docker daemons. It facilitates communication between containers running on different Docker hosts or even different cloud providers. It is particularly useful for container orchestration and clustering systems, enabling seamless communication between containers across the cluster.
**Macvlan network**: Macvlan allows you to assign a MAC address to a container, making it appear as a physical device on the network. This is useful when you need to connect containers directly to external networks, giving them direct access to the physical network without any encapsulation.
**None network**: Containers attached to the none network have no access to external networks and can only communicate with the Docker host. This can be useful in scenarios where you want to completely isolate a container from the network.
**Custom networks**: Docker also allows you to create your custom networks with specific configurations, enabling you to define your network's behavior, IP address range, and other properties according to your application's requirements. Custom networks provide flexibility and control over the networking environment for your containers.

**what does docker buid command do & build vs run command**
The docker build command is used to build Docker images from a Dockerfile. This process involves executing each instruction in the Dockerfile and creating a new layer for each instruction, ultimately producing a final image. The resulting image can be tagged and used to create containers.

The **docker run** command, on the other hand, is used to create and start a new container from a Docker image. When you run docker run, Docker takes the specified image and starts a container based on it. You can also provide additional options and configurations to the docker run command, such as exposing ports, setting environment variables, or specifying volumes to be mounted.

**docker create**
The docker create command is used to create a new container but does not start it. It returns a container ID that can be used in conjunction with other commands. This command is particularly useful when you want to set up a container without starting it immediately.
	
	docker create [OPTIONS] IMAGE [COMMAND] [ARG...]
**what is docker hub**
Docker Hub is a cloud-based registry service provided by Docker that allows you to store and manage Docker images. It provides a centralized resource for container image discovery, distribution, and change management. Docker Hub offers the following key features:

**Image Repositories**: It enables you to store and manage your Docker images, either publicly or privately.
**Collaboration and Sharing**: Docker Hub facilitates collaboration by allowing users to share Docker images with their team members or the broader community.
**Automated Builds**: It provides the functionality to automatically build Docker images from source code repositories, making it easier to manage the continuous integration and deployment process.
**Webhooks and APIs**: Docker Hub offers webhooks and APIs that can be integrated with other tools and services, enabling you to automate various processes related to your Docker images.
**User Access Control**: It allows you to manage user access and permissions for private repositories, ensuring that only authorized users can access sensitive images.
**Official Images**: Docker Hub hosts a collection of official images that are curated and maintained by Docker, ensuring that users have access to trusted and reliable base images for their containers.







virtualization and docker containerasation

	
	Virtualization and containerization are two distinct technologies that serve different purposes, though there are some similarities between them.

Virtualization:

	Virtualization is the process of creating a virtual version of something, such as a hardware platform, operating system, storage device, or network resources.
	It allows you to run multiple operating systems on a single physical machine, making it possible to run different applications on different operating systems.
	Each virtual machine runs its own operating system and is logically isolated from other virtual machines on the same physical server.
	Docker Containerization:

	Docker is a platform for developing, shipping, and running applications using containerization. It allows you to package an application and its dependencies into a container that can run on any Linux server.
	Containers are lightweight, standalone, executable software packages that include everything needed to run a piece of software, including the code, runtime, system tools, system libraries, and settings.
	Unlike virtual machines, containers share the host system's operating system kernel, which makes them more lightweight and faster to start up.
	Differences:

	Virtualization involves creating multiple virtual machines on a single hardware platform, while containerization involves isolating applications into discrete units that can run within a single operating system.
	Virtual machines emulate full-fledged computers, while containers share the operating system kernel of the host machine.
	Virtual machines are generally slower to start and consume more resources compared to containers, which can start quickly and have lower overhead.
	Similarities:

	Both virtualization and containerization provide isolation, allowing applications to run in a contained environment.
	They both contribute to efficient resource utilization, allowing multiple applications to run on a single physical machine.
	In summary, while virtualization and containerization have some similarities in terms of providing isolation and enabling resource efficiency, they serve different purposes and have different architectures.
	
	


advantages of maven

how to add custom plugin
master slave connection

test ng frame work

why test is choosing over selenium  - mailable reports



docker build
docker create
docker hub
Dockernetwork