import requests

import json

# the body of the request to the lambda function
body_content = {

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

# API Gateway endpoint
url_endpoint = "https://5itfjdzqi1.execute-api.us-east-2.amazonaws.com"

url = f"{url_endpoint}/predict"

# send the request
response = requests.post(url, json=body_content)
print(response.json())