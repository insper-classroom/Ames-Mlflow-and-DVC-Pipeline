# send a request with a json to the local server
#
# Used for testing the lambda function locally
import requests
import json

# the body of the request to the lambda function
lambda_body = {
    
  "Mas_Vnr_Area": 1,
  "Foundation_Other": True,
  "Fireplaces": 4,
  "Remod_Age": 0,
  "Kitchen_Qual": 3,
  "Garage_Age": 0,
  "Lot_Area": 1,
  "Garage_Cars": 4,
  "X1st_Flr_SF": 1,
  "BsmtFin_SF_1": 1,
  "Exter_Qual": 3,
  "Total_Bsmt_SF": 1,
  "Garage_Area": 1,
  "Gr_Liv_Area": 1,
  "Overall_Qual": 10

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

