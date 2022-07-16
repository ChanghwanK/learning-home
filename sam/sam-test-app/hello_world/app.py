import json
import traceback

# import requests


def lambda_handler(event, context):
    for i in range(1, 11):
        try:
            check_num(i)
        except ValueError:
            print("value error raised")
            
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
        }),
    }

def check_num(num):
    if (num is 5):
        raise ValueError(f"{num} is invalid")
    else:
        print(f"{num} is valid")

    