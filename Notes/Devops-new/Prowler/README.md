# Prowler Setup and Usage Guide

## Overview

Prowler is a security tool to perform AWS security best practices assessments, audits, incident response, continuous monitoring, hardening, and forensics readiness.

## Prerequisites

1. **AWS CLI**: Ensure that the AWS CLI is installed. Follow the [AWS CLI installation guide](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).
2. **Python**: Ensure that Python version 3.9 or higher is installed.

## Installation Steps

### 1. Check Python Version

Make sure you have Python 3.9 or higher:
```sh
python3 --version
```

### 2. Install `pip` (if not already installed)

Install `pip` for Python 3:
```sh
sudo apt install python3-pip
```

Check `pip` version:
```sh
pip3 --version
```

### 3. Install `cffi` and Prowler

Install `cffi`:
```sh
pip3 install cffi
```

Install Prowler:
```sh
pip3 install prowler
```

### 4. Verify Prowler Installation

Check Prowler version:
```sh
prowler -v
```

## AWS Configuration

### Create a User for Prowler

1. **Create User**:
   - In the AWS Management Console, navigate to IAM.
   - Create a new user (e.g., `prowler-user`).

2. **Attach Policies**:
   - Provide `AdministratorAccess` (optional).
   - Attach `ViewOnlyAccess` and `SystemAudit` policies.

3. **Add Inline Policy**:
   Add the following inline policy to the user:
   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Action": [
           "account:Get*",
           "appstream:Describe*",
           "appstream:List*",
           "backup:List*",
           "cloudtrail:GetInsightSelectors",
           "codeartifact:List*",
           "codebuild:BatchGet*",
           "dlm:Get*",
           "drs:Describe*",
           "ds:Get*",
           "ds:Describe*",
           "ds:List*",
           "ec2:GetEbsEncryptionByDefault",
           "ecr:Describe*",
           "ecr:GetRegistryScanningConfiguration",
           "elasticfilesystem:DescribeBackupPolicy",
           "glue:GetConnections",
           "glue:GetSecurityConfiguration*",
           "glue:SearchTables",
           "lambda:GetFunction*",
           "logs:FilterLogEvents",
           "macie2:GetMacieSession",
           "s3:GetAccountPublicAccessBlock",
           "shield:DescribeProtection",
           "shield:GetSubscriptionState",
           "securityhub:BatchImportFindings",
           "securityhub:GetFindings",
           "ssm:GetDocument",
           "ssm-incidents:List*",
           "support:Describe*",
           "tag:GetTagKeys",
           "wellarchitected:List*"
         ],
         "Resource": "*",
         "Effect": "Allow",
         "Sid": "AllowMoreReadForProwler"
       },
       {
         "Effect": "Allow",
         "Action": [
           "apigateway:GET"
         ],
         "Resource": [
           "arn:aws:apigateway:*::/restapis/*",
           "arn:aws:apigateway:*::/apis/*"
         ]
       }
     ]
   }
   ```

4. **Create Access Keys**:
   - Navigate to the user's Security credentials.
   - Create new Access Keys.

### Configure AWS CLI

After installing AWS CLI, configure it with your credentials:
```sh
aws configure
```
Enter your AWS Access Key, Secret Key, region, and output format when prompted.

## Environment Variables

Set AWS credentials and default region as environment variables (optional):
```sh
export AWS_ACCESS_KEY_ID=your_access_key_id
export AWS_SECRET_ACCESS_KEY=your_secret_access_key
export AWS_DEFAULT_REGION=your_preferred_region
```

## Prowler Usage Examples

### 1. List Categories and Compliance

List available categories:
```sh
prowler aws --list-categories
```

List available compliance standards:
```sh
prowler aws --list-compliance
```

### 2. Run a Basic Prowler Scan

Run a basic scan:
```sh
prowler aws
```

### 3. List AWS Services and Run Specific Services

List AWS services:
```
prowler aws --list-services
```

Run a scan for specific services (e.g., S3 and EC2):
```
prowler aws --services s3 ec2
```

### 4. Exclude Specific Checks

Exclude specific checks (e.g., public access for S3 buckets):
```
prowler aws --excluded-checks s3_bucket_public_access
```

### 5. Specify AWS Profile and Region

Specify an AWS profile and region:
```
prowler aws --profile custom-profile -r us-east-1
```
Make sure to replace `custom-profile` with your AWS profile name and adjust the region as needed.

### 6. Output Results to a File

Save the scan results to a file:
```
prowler aws -M csv > prowler_report.csv
```

### 7. Run Specific Checks

Run specific checks by providing a comma-separated list:
```sh
prowler aws --checks check11,check12
```

### 8. Generate HTML Report

Generate an HTML report using Prowler’s output:
```
prowler aws -M html
```

### 9. Schedule Regular Scans

Use `cron` to schedule regular scans:
```
crontab -e
```
Add a line to run Prowler daily at midnight and save the output:
```
0 0 * * * /usr/local/bin/prowler aws -M csv > /path/to/reports/prowler_report_$(date +\%F).csv
```

## Running Prowler in a Docker Container

You can also run Prowler using Docker, which simplifies dependencies and setup:

1. **Install Docker**:
   Follow the [Docker installation guide](https://docs.docker.com/get-docker/).

2. **Run Prowler with Docker**:
   ```
   docker run --rm -ti -v ~/.aws:/root/.aws -v $(pwd):/prowler-output prowler -p custom-profile
   ```
   This command mounts your AWS credentials and the current directory to the Prowler container.

## Troubleshooting

1. **Check Permissions**:
   Ensure the AWS user has the necessary permissions as described in the inline policy.

2. **Network Connectivity**:
   Verify that the machine running Prowler has internet access to communicate with AWS services.

3. **Logs and Debugging**:
   Use verbose output for detailed logs:
   ```sh
   prowler aws -v
   ```

## Resources

- [Prowler GitHub Repository](https://github.com/prowler-cloud/prowler)
- [AWS IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html)
- [AWS CLI User Guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html)

