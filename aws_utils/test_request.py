# send a request with a json to the local server
#
# Used for testing the lambda function locally
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

# prepare the request
url = "http://localhost:9500/2015-03-31/functions/function/invocations" 
headers = {
    "Content-Type": "application/json",
}
body = {
    "body": json.dumps(body_content)
}

# send the request
response = requests.post(url, headers=headers, json=body)
print(response.json())

