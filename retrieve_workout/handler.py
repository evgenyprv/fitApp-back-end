import json
import get
import post
import validation
import sys

from message import Message

def lambda_handler(event, context):
    result = {}

    try:
        queryValues = list(json.loads(event['body']).values())

        validation.query_values_validation(queryValues[1])
        
        httpMethod = event['httpMethod']
        if(httpMethod == "POST"):
            result = post.post(queryValues[0], queryValues[1], queryValues[2],queryValues[3])
    except ValueError:
        return Message(400, {"message": "Invalid request body"}).generate_response_message()
    except:
        return Message(400, {"error":'Unknown Error'}).generate_response_message()
    else: 
        return Message(200, result).generate_response_message()
