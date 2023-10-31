
# Infrastructure as Code (IaC)

Infrastructure as Code (IaC) is a methodology and practice in which infrastructure resources, such as servers, networks, databases, and other components, are provisioned, configured, and managed using code and automation rather than manual processes. With IaC, infrastructure is treated as software, allowing it to be defined, versioned, and managed just like application code.

## Key characteristics and principles of Infrastructure as Code include:

- **Code-Based Configuration:** IaC relies on code (typically written in a domain-specific language or a scripting language) to describe infrastructure configurations. This code defines what resources should be created, their properties, relationships, and how they should be configured.

- **Version Control:** IaC code is stored in version control systems (e.g., Git) to track changes, collaborate with team members, and maintain a history of infrastructure modifications. This enables rollbacks and collaboration on infrastructure changes.

- **Automation:** IaC tools automate the provisioning and configuration of infrastructure based on the code-defined specifications. This automation reduces human error, accelerates deployments, and ensures consistency.

- **Reproducibility:** IaC allows you to recreate entire infrastructure environments consistently. Whether it's for development, testing, or production, you can use the same code to create identical environments.

- **Scalability:** IaC supports scaling infrastructure resources up or down based on demand by modifying the code, making it easy to adapt to changing requirements.

- **Documentation:** The IaC code itself serves as documentation for the infrastructure, providing clear and up-to-date information on how the infrastructure is configured and managed.

- **Collaboration:** Multiple team members can work together on IaC code, facilitating collaboration between development, operations, and other teams.

- **Security and Compliance:** Security and compliance requirements can be incorporated into the IaC code, ensuring that infrastructure is provisioned and configured with security best practices in mind.

- **Testing:** IaC code can be tested to validate its correctness and functionality before being applied to production environments, reducing the risk of errors.

- **Auditability:** Changes to the infrastructure are traceable back to code commits, providing an audit trail for all modifications.


# Ansible vs Terraform

| Ansible                                     | Terraform                                   |
|---------------------------------------------|---------------------------------------------|
| **Purpose**                                 | **Purpose**                                 |
| Ansible is primarily a configuration       | Terraform is specifically designed for      |
| management and automation tool. It is used  | infrastructure provisioning and management.  |
| for tasks such as software installation,    | It focuses on creating and managing cloud   |
| configuration, and orchestration of tasks   | resources, virtual machines, networks, and   |
| on existing infrastructure.                 | other infrastructure components.            |
|                                             |                                             |
| **Domain-Specific Language**                | **Domain-Specific Language**                |
| Ansible uses YAML-based playbooks to        | Terraform uses its own declarative language  |
| define automation tasks and configurations. | called HashiCorp Configuration Language      |
| These playbooks describe the desired state | (HCL) or JSON. HCL is specifically designed  |
| of a system and how to achieve it using     | for describing infrastructure resources and  |
| tasks and roles.                            | their relationships.                         |
|                                             |                                             |
| **State Management**                        | **State Management**                        |
| Ansible does not maintain a centralized     | Terraform maintains a state file that tracks |
| state of infrastructure. It operates on     | the state of your infrastructure resources.  |
| the current state of the target systems.    | This state file is crucial for understanding |
| While you can use Ansible to modify         | the current state of the infrastructure and  |
| configurations, it doesn't inherently track  | making incremental changes based on your     |
| the state of your infrastructure like       | configuration.                               |
| Terraform does.                             |                                             |
|                                             |                                             |
| **Idempotency**                             | **Idempotency**                             |
| Ansible strives to ensure idempotent        | Terraform is inherently idempotent. It       |
| operations, meaning that running Ansible    | calculates the difference between the        |
| playbooks multiple times should have the    | current state and the desired state and      |
| same result as running them once, provided  | applies only the necessary changes, making  |
| the desired state is already achieved.      | it safe to apply configurations multiple     |
|                                             | times.                                      |
|                                             |                                             |
| **Use Cases**                               | **Use Cases**                               |
| Ansible is well-suited for tasks related to | Terraform is best suited for infrastructure  |
| configuration management, application       | provisioning, including creating and managing|
| deployment, and automation of operational   | cloud resources, networks, storage, and      |
| tasks on existing servers. It is often      | virtual machines. It excels in the initial   |
| used in a post-provisioning phase for       | setup and management of infrastructure.      |
| system configuration.                       |                                             |
|                                             |                                             |
| **Ecosystem**                               | **Ecosystem**                               |
| Ansible has a broad ecosystem of            | Terraform has a wide range of providers for  |
| community-contributed roles and modules     | various cloud platforms and services, making |
| for various tasks and integrations with     | it well-suited for multi-cloud and hybrid    |
| different technologies.                     | cloud environments.                          |

**infrastructure provisioning tools**
- Terraform
- AWS CloudFormation
- Azure Resource Manager (ARM) Templates
- Google Cloud Deployment Manager
- OpenStack Heat
- Packer
- Vagrant
- Ansible
- Chef Provisioning
- Pulumi
- Cloudify
- Rancher
- Nomad

# Terraform

Terraform is an open-source infrastructure as code (IaC) tool developed by HashiCorp. It is used for defining and provisioning infrastructure resources in a declarative manner. With Terraform, you can describe your infrastructure as code using a domain-specific language called HashiCorp Configuration Language (HCL) or, alternatively, use JSON.

## Key Concepts and Capabilities

- **Declarative Configuration:** Terraform allows you to define your infrastructure in a declarative manner, specifying what resources you want and their configurations, rather than writing scripts to provision and manage them.

- **Providers:** Terraform supports a wide range of cloud providers, as well as on-premises and third-party services.

- **Resources:** Resources are the building blocks of your infrastructure. These represent the actual cloud or infrastructure components you want to create or manage.

- **Modules:** Terraform allows you to create reusable modules to encapsulate and organize your infrastructure code.

- **State Management:** Terraform maintains a state file that keeps track of the current state of your infrastructure.

- **Execution Plan:** Before making any changes, Terraform generates an execution plan, showing you the actions it will take to achieve the desired state.

- **Idempotent Operations:** Terraform is idempotent, making it safe to apply configurations multiple times.

- **Version Control Integration:** Terraform works well with version control systems such as Git.

- **Extensibility:** Terraform is extensible and has a growing ecosystem of third-party plugins and extensions.

## Benefits of Terraform

- **Infrastructure as Code (IaC):** Allows you to define your infrastructure as code, making it easy to version, review, and collaborate on infrastructure changes.

- **Multi-Cloud and Hybrid Cloud Support:** Supports multiple cloud providers, enabling the management of resources across different environments.

- **Declarative Syntax:** Simplifies configuration management and determines the necessary actions to bring the infrastructure to the desired state.

- **State Management:** Maintains a state file that records the current state of your infrastructure.

- **Idempotent Operations:** Safely applies the same configuration multiple times without unexpected changes.

- **Execution Plans:** Provides a clear view of actions to be taken before applying changes.

- **Modularity:** Supports the creation of reusable modules, promoting code reusability and maintainability.

- **Ecosystem:** Has a vast ecosystem of providers and community-contributed modules for common use cases.

- **Integration with Version Control:** Tracks changes to infrastructure code and facilitates collaboration with team members.

- **Scalability and Automation:** Handles large and complex infrastructures, integrating into CI/CD pipelines for automated and consistent deployments.

- **Community and Support:** Offers resources and forums for troubleshooting, learning best practices, and commercial support options for enterprises.

- **Cost Management:** Manages cloud resources cost-effectively through automated lifecycle management and cost-saving strategies.

+++	
- terraform using hashiCorp Configuration Language -

	

██ ███    ██ ███████ ████████  █████  ██      ██       █████  ████████ ██  ██████  ███    ██ 
██ ████   ██ ██         ██    ██   ██ ██      ██      ██   ██    ██    ██ ██    ██ ████   ██ 
██ ██ ██  ██ ███████    ██    ███████ ██      ██      ███████    ██    ██ ██    ██ ██ ██  ██ 
██ ██  ██ ██      ██    ██    ██   ██ ██      ██      ██   ██    ██    ██ ██    ██ ██  ██ ██ 
██ ██   ████ ███████    ██    ██   ██ ███████ ███████ ██   ██    ██    ██  ██████  ██   ████ 
                                                                                             
                                                                                             
Installation:

- Terraform information: [Terraform Installation Guide](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)

- Install AWS CLI:

  ```
  sudo apt-get update
  sudo apt-get install awscli
  ```

  For AWS CLI configuration, run the command `aws configure` and enter the required information.

EC2 Instance Creation using Terraform:

1. Create a directory for your Terraform configuration and navigate to it in your terminal.

2. Create a Terraform configuration file (e.g., main.tf) with the following content:

   ```hcl
   provider "aws" {
     region = "us-east-2"
     shared_credentials_files = ["~/.aws/credentials"]
   }

   resource "aws_instance" "app_server" {
     instance_type = "t2.micro"
     key_name      = "ohiokey"
     ami           = "ami-0430580de6244e02e"

     tags = {
       Name = "ExampleAppServerInstance"
     }
   }
   ```

3. Initialize the Terraform workspace by running the following command in your terminal:

   ```
   terraform init
   ```

4. Optionally, you can create an execution plan using the command `terraform plan` to preview the changes Terraform will make to your infrastructure.

5. To create the EC2 instance, run:

   ```
   terraform apply
   ```

6. To destroy the EC2 instance, run:

   ```
   terraform destroy
   ```

For more detailed AWS CLI installation, you can refer to [Install AWS CLI on Ubuntu](https://linuxhint.com/install_aws_cli_ubuntu/).
