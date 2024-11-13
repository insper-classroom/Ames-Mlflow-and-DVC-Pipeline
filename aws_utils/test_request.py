# send a request with a json to the local server
#
# Used for testing the lambda function locally
import requests
import json

# the body of the request to the lambda function
lambda_body = {

}

# prepare the request
url = "http://localhost:9500/2015-03-31/functions/function/invocations" 
headers = {
    "Content-Type": "application/json",
}
body = {
    "body": json.dumps(lambda_body)
}

# send the request
response = requests.post(url, headers=headers, json=body)
print(response.json())

