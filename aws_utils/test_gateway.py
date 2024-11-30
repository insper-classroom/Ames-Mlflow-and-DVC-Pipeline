import requests

import json

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

# API Gateway endpoint
url_endpoint = "https://al4qlura5d.execute-api.us-east-2.amazonaws.com"

url = f"{url_endpoint}/predict"

# send the request
response = requests.post(url, json=body_content)
print(response.json())