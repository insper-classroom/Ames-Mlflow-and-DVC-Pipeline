import requests

import json

# the body of the request to the lambda function
body_content = {

}

# API Gateway endpoint
url_endpoint = ""

url = f"{url_endpoint}/aps3"

# send the request
response = requests.post(url, json=body_content)
print(response.json())