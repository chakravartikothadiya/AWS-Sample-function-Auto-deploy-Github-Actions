import requests
import os

def lambda_handler(event, context):

    var1_value = os.environ.get('Var1')
    if var1_value:
        print(f"Value of Var1: {var1_value}")
    else:
        print("Var1 environment variable not set.")

    response = requests.get("https://www.example.com")
    return {"statusCode": 200, "body": "Hello, world! This is through Github Actionss"}

