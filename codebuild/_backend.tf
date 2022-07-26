terraform {
  backend "s3" {
    bucket      = "dev-apne2-backend-bucket"
    key         = "dev/apne2/codebuild/terraform.tfstate"
    region      = "ap-northeast-2"
#    role_arn    = "{ASSUMED_ROLE}"
    max_retries = 3
  }
}
