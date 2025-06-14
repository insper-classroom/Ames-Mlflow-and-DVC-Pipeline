import boto3
import os
from dotenv import load_dotenv
import random
import string


load_dotenv()


lambda_function_name = "grupo_hardware_lambda"
lambda_arn = "arn:aws:lambda:us-east-2:820926566402:function:grupo_hardware_lambda"


api_gateway_name = "grupo_hardware_gateway"

id_num = "".join(random.choices(string.digits, k=7))

api_gateway = boto3.client(
    "apigatewayv2",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION"),
)

lambda_function = boto3.client(
    "lambda",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION"),
)

lambda_function_get = lambda_function.get_function(FunctionName=lambda_function_name)

print(lambda_function_get)

api_gateway_create = api_gateway.create_api(
    Name=api_gateway_name,
    ProtocolType="HTTP",
    Version="1.0",
    RouteKey="POST /predict", # Create a /polarity POST route
    Target=lambda_function_get["Configuration"]["FunctionArn"],
)

api_gateway_permissions = lambda_function.add_permission(
    FunctionName=lambda_function_name,
    StatementId="api-gateway-permission-statement-" + id_num, # Add a random ID
    Action="lambda:InvokeFunction",
    Principal="apigateway.amazonaws.com",
)

print("API Endpoint:", api_gateway_create["ApiEndpoint"])

# save the endpoint to a file
with open("api_endpoint.txt", "w") as f:
    f.write(api_gateway_create["ApiEndpoint"])

print("API Gateway created successfully")