resource "aws_iam_role" "lambda_execution_role" {
  name = "lambda_execution_role"
  assume_role_policy = data.aws_iam_policy_document.lambda_trust_policy.json
}

data "aws_iam_policy_document" "lambda_trust_policy"{
  statement {
    effect = "Allow"
    principals {
      type = "Service"
      identifiers = [
        "lambda.amazonaws.com",
        "ec2.amazonaws.com"
      ]
    }
    actions = ["sts:AssumeRole"]
  }
}

data "aws_iam_policy_document" "lambda_execution_policy_document" {
  statement {
    sid = "ManageLambdaFunction"
    effect = "Allow"
    actions = [
      "lambda:*",
      "ec2:*",
      "cloudwatch:*",
      "logs:*",
      "s3:*"
    ]
    resources = ["*"]
  }
}

resource "aws_iam_policy" "lambda_execution_policy" {
  name = "lambda_execution_policy"
  policy = data.aws_iam_policy_document.lambda_execution_policy_document.json
}

resource "aws_iam_role_policy_attachment" "lambda_execution_attachment" {
  role = aws_iam_role.lambda_execution_role.name
  policy_arn = aws_iam_policy.lambda_execution_policy.arn
}
