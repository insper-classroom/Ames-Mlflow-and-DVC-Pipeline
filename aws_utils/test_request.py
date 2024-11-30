# send a request with a json to the local server
#
# Used for testing the lambda function locally
import requests
import json

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

