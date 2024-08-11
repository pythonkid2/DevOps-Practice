# installing the Azure CLI, logging in, creating a virtual machine (VM), and deleting it.

## Azure CLI Installation, Login, and VM Management

## 1. Install Azure CLI

To install the Azure CLI, follow the official documentation:
- **[Azure CLI Installation Guide](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)**

## 2. Log In to Azure CLI

Once the Azure CLI is installed, log in to your Azure account:

```
az login
```

This command will open a web browser where you can sign in to your Azure account.

## 3. Create a Resource Group

Before creating a VM, you need to create a resource group. A resource group is a container that holds related resources for an Azure solution.

```
az group create --name demoResourceGroup --location westus
```

This command creates a resource group named `demoResourceGroup` in the `westus` region.

## 4. Create an Azure Virtual Machine (VM)

### 4.1 Define PowerShell Variables

Define the necessary variables for creating the VM:

```
$vmName = "TutorialVM1"
$resourceGroup = "demoResourceGroup"
$vnetName = "demovnet"
$subnetName = "demosubnet"  # Define your subnet name here
```

### 4.2 Create the VM

Use the following Azure CLI command to create the VM:

```
az vm create --resource-group $resourceGroup --name $vmName --image Ubuntu2204 --vnet-name $vnetName --subnet $subnetName --generate-ssh-keys --output json --verbose
```

This command creates a VM with the specified resource group, VM name, image, virtual network, and subnet. It also generates SSH keys for secure access.

## 5. Delete the Resource Group

When you no longer need the VM and associated resources, you can delete the entire resource group. This will remove the VM and all other resources within the group.

```
az group delete --name demoResourceGroup --yes --no-wait
```

This command deletes the `demoResourceGroup` and all resources contained within it.

## Conclusion

This guide covers the steps for installing the Azure CLI, logging in, creating a VM, and deleting the resource group. For more detailed information, refer to the official Azure documentation.
```

This document provides a structured guide for managing Azure resources using the CLI.
