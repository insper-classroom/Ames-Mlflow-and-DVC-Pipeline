import boto3
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Provide bucket name
bucket_name = "dvc-project-rodrigoap8"

# Initialize the S3 client
s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION"),
)

# Function to list bucket contents
def list_bucket_contents(bucket_name):
    try:
        # List objects in the bucket
        response = s3.list_objects_v2(Bucket=bucket_name)
        
        if 'Contents' in response:
            print(f"Contents of bucket '{bucket_name}':")
            for obj in response['Contents']:
                print(f" - {obj['Key']} (Size: {obj['Size']} bytes)")
        else:
            print(f"The bucket '{bucket_name}' is empty.")
    except Exception as e:
        print(f"Error listing bucket contents: {e}")

# Call the function
list_bucket_contents(bucket_name)
