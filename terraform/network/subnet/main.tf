variable "aws_vpc_id" {
  type    = string
  default = "vpc-0020c7205c33581b3"
}

resource "aws_subnet" "order-vpc-public-sunet-1" {
  vpc_id     = var.aws_vpc_id
  cidr_block = "192.168.1.0/24"
  availability_zone = "ap-northeast-2a"

  tags = {
    Name = "order-vpc-public-subnet-1"
  }
}

resource "aws_subnet" "order-vpc-public-sunet-2" {
  vpc_id     = var.aws_vpc_id
  cidr_block = "192.168.2.0/24"
  availability_zone = "ap-northeast-2a"

  tags = {
    Name = "order-vpc-public-subnet-2"
  }
}


resource "aws_subnet" "order-vpc-private-sunet-1" {
  vpc_id     = var.aws_vpc_id
  cidr_block = "192.168.3.0/24"
  availability_zone = "ap-northeast-2c"

  tags = {
    Name = "order-vpc-private-subnet-1"
  }
}


resource "aws_subnet" "order-vpc-private-sunet-2" {
  vpc_id     = var.aws_vpc_id
  cidr_block = "192.168.4.0/24"
  availability_zone = "ap-northeast-2c"

  tags = {
    Name = "order-vpc-private-subnet-2"
  }
}
