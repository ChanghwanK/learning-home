output "vpc_id" {
  value = module.vpc.vpc_id
}

output "public_subnet_id" {
  value = module.vpc.public_subnet_id
}

output "private_subnet_id" {
  value = module.vpc.private_subnet_id
}

output "vpc_enable_dns_hostnames" {
  value = module.vpc.enable_dns_hostnames
}

output "enable_dns_support" {
  value = module.vpc.enable_dns_support
}