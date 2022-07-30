terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "3.45.0"
    }
  }
}

terraform {
  backend "s3" {
    bucket  = "dev-apne2-backend-bucket"
    key     = "terraform/dev-apne2-test/terraform.tfstate"
    region  = "ap-northeast-2"
    encrypt = true
  }
}

provider "aws" {
  region = "ap-northeast-2"
}

module "vpc" {
  source                    = "./vpc"
  vpc_cidr_block            = "192.168.0.0/16"
  public_subnet_cidr_block  = "192.168.0.0/24"
  private_subnet_cidr_block = "192.168.1.0/24"
  enable_dns_hostnames      = true
  enable_dns_support        = true
  service                   = "dev"
  owner                     = "changhwan"
  name                      = "dev-vpc"
}