provider "aws" {
  region = "ap-northeast-2"
}


data "aws_ami" "amazon-linux-2" {
  most_recent = true

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-ebs"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  owners = ["amazon"]
}


resource "aws_instance" "ec2-was" {
  ami = data.aws_ami.amazon-linux-2.id
  instance_type = "t2.micro"
}
