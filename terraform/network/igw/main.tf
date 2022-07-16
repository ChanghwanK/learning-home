variable "aws_vpc_id" {
  type    = string
  default = "vpc-0020c7205c33581b3"
}

resource "aws_internet_gateway" "order-dev-igw" {
  vpc_id = var.aws_vpc_id

  tags = {
    Name = "order-dev-igw"
  }
}