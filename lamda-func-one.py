import requests

def lambda_handler(event, context):
    response = requests.get("https://www.example.com")
    return {"statusCode": 200, "body": "Hello, world! This is through Github Actionss"}

