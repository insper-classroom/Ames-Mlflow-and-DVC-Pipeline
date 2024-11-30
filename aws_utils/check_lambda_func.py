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
  "Kitchen.Qual": 2,
  "Remod.Age": 50,
  "Open.Porch.SF": 62,
  "Garage.Age": 50,
  "Lot.Area": 10.37,
  "Full.Bath": 1,
  "BsmtFin.SF.1": 639,
  "Garage.Cars": 2,
  "X1st.Flr.SF": 1656,
  "Exter.Qual": 2,
  "Total.Bsmt.SF": 1080,
  "Garage.Area": 528,
  "Gr.Liv.Area": 1656,
  "Overall.Qual": 3
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