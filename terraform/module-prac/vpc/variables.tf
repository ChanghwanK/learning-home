variable "vpc_cidr_block" {
  type = string
}

variable "public_subnet_cidr_block" {
  type = string
}

variable "private_subnet_cidr_block" {
  type = string
}

variable "enable_dns_hostnames" {
  type = bool
}

variable "enable_dns_support" {
  type = bool
}

variable "service" {
  type = string
}

variable "owner" {
  type = string
}

variable "name" {
  type = string
}