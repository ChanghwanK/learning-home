# locals {
#   cidr_block = "192.168.0.0/16"
# }

resource "aws_vpc" "order-dev-vpc-192-168-0-0" {
  cidr_block = var.cidr_block
  tags = {
    Name: "order-dev-vpc"
  }
}