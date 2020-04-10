import psycopg2
import get
import os
import json

from message import Message

db_host = os.environ['DB_HOST']
db_port = os.environ['DB_PORT']
db_name = os.environ['DB_NAME']
db_user = os.environ['DB_USERNAME']
db_pass = os.environ['DB_PASSWORD']

def lambda_handler(event, context):
    result={}
    conn = None
    
    try: 
        conn = psycopg2.connect("dbname='%s' user='%s' host='%s' password='%s'" % (db_name, db_user, db_host, db_pass))
    except:  
        return Message(400, {"error":'Something went wrong'}).generate_response_message()
    else:
        try:
            httpMethod = event['httpMethod']
            if(httpMethod == "GET"):
                result = get.get_workout_type(conn)
        except:
            return Message(400, {"error":'Something went wrong with values.'}).generate_response_message()
        else:
            return Message(200, {"workout_type": result}).generate_response_message()
            
        conn.close()