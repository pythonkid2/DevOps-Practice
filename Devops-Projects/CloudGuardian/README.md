#pending

**Project Title: CloudGuardian: AWS Compliance Automation**

**Project Description:**

As a Cloud Engineering team, we oversee the AWS environment to maintain compliance with organizational policies. Using AWS CloudWatch alongside AWS Lambda, we manage resources according to these policies. For instance, we trigger a Lambda function upon the creation of an Amazon Elastic Block Store (EBS) volume. Leveraging Amazon CloudWatch Events, we monitor and convert EBS volumes from type GP2 to GP3 as needed.

STEPS 

create lambda function 

Create function  -> Function name (ebs_volume_check) -> Runtime (Python 3.12) ->Change default execution role -> 
Create a new role with basic Lambda permissions ->


go to cloudwatch
events -> rules 
