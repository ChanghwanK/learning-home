data "aws_ami" "amzn2_latest" {
  most_recent = true
  filter {
    name   = "name"
    values = ["*amzn2-ami-hvm*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  filter {
    name   = "architecture"
    values = ["x86_64"]
  }

  owners = ["amazon"]
}

data "aws_vpc" "default" {
  default = true
}

resource "aws_instance" "example" {
  ami                    = data.aws_ami.amzn2_latest.id
  instance_type          = "t2.micro"
  vpc_security_group_ids = [aws_security_group.sg_example.id]
  key_name               = aws_key_pair.example_server_key_pair.key_name

  user_data = <<-EOF
              #!/bin/bash
              echo "Hello, World" > index.html
              nohup busybox httpd -f -p 8080 &
              EOF

  tags = {
    "name" = "test-amzn2"
  }

  depends_on = [
    aws_key_pair.example_instance_key_pair
  ]
}

resource "aws_key_pair" "example_instance_key_pair" {
  key_name   = "example-key-pair"
  public_key = file("~/.ssh/id_rsa.pub")
}

resource "aws_security_group" "sg_example" {
  vpc_id = data.aws_vpc.default.id
  name   = "sg_example"
  ingress {
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  tags = {
    "name" = "test-sg-01"
  }
}

resource "aws_security_group_rule" "example-sg-rule" {
  security_group_id = aws_security_group.sg_example.id
  type              = "ingress"
  from_port         = 22
  to_port           = 22
  protocol          = "TCP"
  cidr_blocks       = ["0.0.0.0/0"]

  lifecycle {
    create_before_destroy = true
  }
}