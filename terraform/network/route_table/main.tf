variable "aws_vpc_id" {
  type    = string
  default = "vpc-0020c7205c33581b3"
}

variable "igw_id" {
    type = string
    default = "igw-014c41a25e7c813f3"
}

resource "aws_default_route_table" "default-public_rt" {
    default_route_table_id = "rtb-0653c78269ac770db"

    route {
        cidr_block = "0.0.0.0/0"
        gateway_id = var.igw_id
    }

    tags = {
        Name = "default public route table"
    }
}

resource "aws_route_table" "order-dev-public-rtb" {
  vpc_id = var.aws_vpc_id
  
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = var.igw_id
  }

  tags = {
    Name = "order-dev-public-rtb"
  }
}

resource "aws_route_table" "order-dev-private-rtb" {
  vpc_id = var.aws_vpc_id

  tags = {
    Name = "example"
  }
}

resource "" "name" {
  
}