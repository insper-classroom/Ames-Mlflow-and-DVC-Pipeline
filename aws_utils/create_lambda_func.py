import boto3
import os
from dotenv import load_dotenv

load_dotenv()

# Provide function name
function_name = "grupo_hardware_lambda"

# Provide Image URI from before
image_uri = "820926566402.dkr.ecr.us-east-2.amazonaws.com/equipe_hardware_ecr:latest"

lambda_role_arn = os.getenv("AWS_LAMBDA_ROLE_ARN")

# Create a Boto3 client for AWS Lambda
lambda_client = boto3.client(
    "lambda",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION"),
)

response = lambda_client.create_function(
    FunctionName=function_name,
    PackageType="Image",
    Code={"ImageUri": image_uri},
    Role=lambda_role_arn,
    Timeout=900,  # Optional: function timeout in seconds
    MemorySize=512,  # Optional: function memory size in megabytes
)

print("Lambda function created successfully:")
print(f"Function Name: {response['FunctionName']}")
print(f"Function ARN: {response['FunctionArn']}")