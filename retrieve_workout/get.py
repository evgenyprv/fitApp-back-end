import boto3
import json
import sys

def get(workout_type):

    if(workout_type == "random"):
        invokeLambda = boto3.client('lambda', region_name='us-east-1')
        response = invokeLambda.invoke(FunctionName = 'retrieveRandomWorkout', InvocationType = 'RequestResponse')

        response_payload = json.loads(response['Payload'].read().decode())

        return {"exercises" : response_payload}
    else:
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('Workout')
        
        response = table.get_item(
            Key={
                'workout_type': workout_type,
            }
        )
        
        return {"exercises": response['Item']['exercises']}
