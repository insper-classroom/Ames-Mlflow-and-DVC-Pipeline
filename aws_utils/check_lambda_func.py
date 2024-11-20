import boto3
import os
import io
from dotenv import load_dotenv
import json

load_dotenv()

# Lambda function name
function_name = "grupo_hardware_lambda"

# the body of the request to the lambda function
body_content = {
    "age": 59,
    "job": "admin",
    "marital": "married",
    "education": "secondary",
    "balance": 2343,
    "housing": "yes",
    "duration": 1042,
    "campaign": 1
}

lambda_event = {
    "body": json.dumps(body_content)
}

# Create a Boto3 client for AWS Lambda
lambda_client = boto3.client(
    "lambda",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION"),
)


try:
    # Invoke the function sending the body
    response = lambda_client.invoke(
        FunctionName=function_name,
        Payload=json.dumps(lambda_event),
        InvocationType='RequestResponse',  # Ensure it's a synchronous request
        LogType='Tail'
    )

    payload = response["Payload"]

    txt = io.BytesIO(payload.read()).read().decode("utf-8")
    print(f"Response:\n{txt}")
except Exception as e:
    print(e)