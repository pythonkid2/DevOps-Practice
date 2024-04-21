terraform {
  backend "s3" {
    bucket         = "mathewdemo" # change this
    key            = "mathew/terraform.tfstate"
    region         = "us-east-2"
    encrypt        = true
    dynamodb_table = "terraform-lock"
  }
}
