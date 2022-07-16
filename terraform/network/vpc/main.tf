resource "aws_vpc" "order-dev-vpc-192-168-0-0" {
  cidr_block = "192.168.0.0/16"
  tags = {
    Name: "order-dev-vpc"
  }
}