resource "aws_s3_bucket" "_dev_apne2_backend_bucket" {
  bucket = "dev-apne2-backend-bucket"

  tags = {
    Name        = "Backend Bucket"
    Environment = "Dev"
  }
}

resource "aws_s3_bucket_acl" "_dev_apne2_backend_bucket_acl" {
  bucket = aws_s3_bucket._dev_apne2_backend_bucket.id
  acl    = "private"
}