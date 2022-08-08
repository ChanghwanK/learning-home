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
  instance_type          = "t2.micro"
  ami                    = data.aws_ami.latest-ubuntu.image_id
  vpc_security_group_ids = [aws_security_group.test-sg1.id]

  user_data = <<-EOF
              #!/bin/bash
              echo "hellow world" > index.html
              nohub busybox httpd -f -p 8080 &
              EOF


  tags = {
    "name"  = "test"
    "owner" = "changhwan"
    "env"   = "dev"
  }
}

resource "aws_security_group" "test-sg1" {
  name = "sigle-instance-sg1"

  ingress {
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    "name" = "test-sg1"
  }
}

