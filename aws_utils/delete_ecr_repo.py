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

try:
    response = ecr_client.delete_repository(
        repositoryName=repository_name,
        force=True  # Set to True to delete a repository even if it contains images
    )
    print(f"Repository '{repository_name}' deleted successfully.")
    print(response)
except ecr_client.exceptions.RepositoryNotFoundException:
    print(f"Repository '{repository_name}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
