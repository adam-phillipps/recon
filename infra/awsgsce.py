import json
import webrecon.gcse as gcse


def handler(context, event):
    return build_response(gsce.search(event))

def build_response(body=[], status=200):
    response_object = {
        "isBase64Encoded": "false",
        "statusCode": status,
        "body": json.dumps(body),
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods":
                "DELETE,GET,HEAD,OPTIONS,PATCH,POST,PUT",
            "Access-Control-Allow-Headers":
                "Content-Type,Authorization,X-Amz-Date,X-Api-Key,X-Amz-Security-Token"}}

    return response_object
