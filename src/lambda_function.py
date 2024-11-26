import json
import pickle
import numpy as np
import pandas as pd
import logging

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def predict(event, context):
    logger.info("Lambda function invoked")
    
    try:
        # Load the model
        logger.info("Loading the model...")
        model = pickle.load(open("stack_reg.pkl", "rb"))
        logger.info("Model loaded successfully")
        
        # Check for body in event
        if "body" not in event:
            logger.error("No body provided in the event")
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "No body provided (lambda_function)"})
            }
        
        # Parse the input data
        raw_json = event["body"]
        logger.info("Received raw JSON: %s", raw_json)
        body = json.loads(raw_json)
        
        # Transform input into DataFrame
        df = pd.DataFrame([body])
        logger.info("Input transformed into DataFrame: %s", df)
        
        # Make a prediction
        prediction = model.predict(df)
        logger.info("Prediction made: %s", prediction.tolist())
        
        # Return the prediction
        return {
            "statusCode": 200,
            "body": json.dumps(prediction.tolist())
        }
        
    except Exception as e:
        logger.error("An error occurred: %s", e, exc_info=True)
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Internal server error"})
        }
