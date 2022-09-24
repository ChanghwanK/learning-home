output "aws_ami_id" {
  value = aws_instance.example.ami
}

output "aws-instance-public-ip" {
  value = aws_instance.example.public_ip
}