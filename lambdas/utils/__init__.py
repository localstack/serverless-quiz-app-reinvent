import json

def prepare_response(status_code, body):
    return {
        "statusCode": status_code,
        "body": json.dumps(body),
        "headers": {
            "Content-Type": "application/json",
        }
    }
