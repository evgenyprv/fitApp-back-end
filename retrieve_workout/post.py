import boto3
import json
import sys

def post(workout_location, workout_type, cardio, core):

    if(workout_type == "random"):
        invokeLambda = boto3.client('lambda', region_name='us-east-1')
        payload = {"cardio": cardio, "core": core}
        response = {}
        
        if workout_location == 'gym':
            response = invokeLambda.invoke(FunctionName = 'retrieve_random_gym_workout', 
                InvocationType = 'RequestResponse', Payload=json.dumps(payload))
        elif workout_location == 'home':
            response = invokeLambda.invoke(FunctionName = 'retrieve_random_home_workout', 
                InvocationType = 'RequestResponse', Payload=json.dumps(payload))
        
        response_payload = json.loads(response['Payload'].read().decode())
        
        if(list(response_payload.keys()).count('errorMessage') >= 1):
            raise 'LambdaException'
            
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