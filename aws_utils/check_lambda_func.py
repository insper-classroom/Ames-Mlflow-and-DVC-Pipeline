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
  "Fireplaces": 2,
  "Kitchen_Qual": 2,
  "Remod_Age": 50,
  "Open_Porch_SF": 62,
  "Garage_Age": 50,
  "Lot_Area": 10.37,
  "Full_Bath": 1,
  "BsmtFin_SF_1": 639,
  "Garage_Cars": 2,
  "X1st_Flr_SF": 1656,
  "Exter_Qual": 2,
  "Total_Bsmt_SF": 1080,
  "Garage_Area": 528,
  "Gr_Liv_Area": 1656,
  "Overall_Qual": 3
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