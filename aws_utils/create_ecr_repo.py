import boto3
import os
from dotenv import load_dotenv

load_dotenv()

repository_name = "equipe_hardware_ecr"

# Create a Boto3 client for ECR
ecr_client = boto3.client(
    "ecr",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION"),
)

response = ecr_client.create_repository(
    repositoryName=repository_name,
    imageScanningConfiguration={"scanOnPush": True},
    imageTagMutability="MUTABLE",
)

print(response)

print(f"\nrepositoryArn: {response['repository']['repositoryArn']}")
print(f"repositoryUri: {response['repository']['repositoryUri']}")