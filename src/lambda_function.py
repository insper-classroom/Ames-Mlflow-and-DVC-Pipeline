import json
import pickle
import numpy as np
import pandas as pd


def predict(event, context):
    # load the model
    model = pickle.load(open("stack_reg.pkl", "rb"))
    # Provide a body for the request!
    if "body" not in event:
        return {"error": "No body provided (lambda_function)"}

    # Get the dumped JSON from the body
    raw_json = event["body"]

    # Load it into a Python dict
    body = json.loads(raw_json)

    # transform the dictionary into a dataframe
    df = pd.DataFrame([body])

    # make a prediction
    prediction = model.predict(df)

    # return the prediction
    return {
        "statusCode": 200,
        "body": json.dumps(prediction.tolist())
    }
