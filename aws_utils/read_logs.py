import boto3
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Provide the function name
function_name = "grupo_hardware_lambda"
log_group_name = f"/aws/lambda/{function_name}"

# Create a CloudWatch Logs client
logs_client = boto3.client(
    "logs",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION"),
)

# Fetch log streams
def get_log_streams(log_group_name):
    response = logs_client.describe_log_streams(
        logGroupName=log_group_name,
        orderBy="LastEventTime",
        descending=True,
        limit=5  # Fetch the latest 5 log streams
    )
    return response.get("logStreams", [])

# Fetch log events from a log stream
def get_log_events(log_group_name, log_stream_name):
    response = logs_client.get_log_events(
        logGroupName=log_group_name,
        logStreamName=log_stream_name,
        startFromHead=True
    )
    return response.get("events", [])

# Main function to fetch and print logs
def fetch_lambda_logs():
    try:
        log_streams = get_log_streams(log_group_name)
        if not log_streams:
            print(f"No log streams found for log group: {log_group_name}")
            return
        
        for stream in log_streams:
            log_stream_name = stream["logStreamName"]
            print(f"\nFetching logs from stream: {log_stream_name}")
            events = get_log_events(log_group_name, log_stream_name)
            for event in events:
                print(event["message"])
    except Exception as e:
        print(f"Error fetching logs: {e}")

# Fetch and print the logs
fetch_lambda_logs()
