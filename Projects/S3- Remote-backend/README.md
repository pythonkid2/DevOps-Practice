![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/7bf205f9-eba6-46ea-858d-3f2e72277c33)

## Setting up Terraform with AWS Provider

### 1. Provider Configuration

```
provider "aws" {
  region = "us-east-2"
}
```

### 2. Define AWS Resources

```
resource "aws_instance" "Mathew" {
  instance_type = "t2.micro"
  ami           = "ami-053b0d53c279acc90" # Change this to your desired AMI
  subnet_id     = "subnet-019ea91ed9b5252e7" # Change this to your desired subnet
}

resource "aws_s3_bucket" "s3_bucket" {
  bucket = "mathewdemo" # Change this to your desired bucket name
}

resource "aws_dynamodb_table" "terraform_lock" {
  name         = "terraform-lock"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "LockID"

  attribute {
    name = "LockID"
    type = "S"
  }
}
```

**Notes**:
- Make sure to replace the placeholders with appropriate values for your environment.
- Ensure the AMI ID corresponds to the desired operating system and software configuration.
- Verify the subnet ID to ensure the instance is launched in the correct subnet.

## State Management with S3 and DynamoDB
State management is a critical aspect of Terraform to track the state of managed infrastructure resources. Terraform stores state information in a state file, which contains details about the resources provisioned and their current state.

### 1. Backend Configuration (backend.tf)

```
terraform {
  backend "s3" {
    bucket         = "mathewdemo" # Change this to the same bucket name used above
    key            = "mathew/terraform.tfstate"
    region         = "us-east-2"
    encrypt        = true
    dynamodb_table = "terraform-lock"
  }
}
```

### 2. Create S3 Bucket and DynamoDB Table

- **S3 Bucket**: `mathewdemo`
  - This bucket will store the Terraform state file.

- **DynamoDB Table**: `terraform-lock`
  - This table is used for state locking to prevent concurrent modifications.

**Notes**:
- Ensure the S3 bucket and DynamoDB table names are unique and compliant with AWS naming conventions.
- Terraform state locking with DynamoDB helps prevent conflicts when multiple users are running Terraform commands concurrently.

## Displaying Terraform State

```
terraform show
```


