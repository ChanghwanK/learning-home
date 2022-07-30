output "vpc_id" {
  value = aws_vpc.main.id
}

output "public_subnet_id" {
  value = aws_subnet.public.id
}

output "private_subnet_id" {
  value = aws_subnet.private.id
}

output "enable_dns_hostnames" {
  value = aws_vpc.main.enable_dns_hostnames
}

output "enable_dns_support" {
  value = aws_vpc.main.enable_dns_support
}

output "tags" {
  value = aws_vpc.main.tags
}