data "aws_ami" "latest-ubuntu" {
  most_recent = true

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  owners = ["099720109477"] # Canonical
}

resource "aws_instance" "single-instance-01" {
  instance_type = "t2-micro"
  ami           = data.aws_ami.latest-ubuntu.image_id

  tags = {
    "name"  = "test"
    "owner" = "changhwan"
    "env"   = "dev"
  }
}