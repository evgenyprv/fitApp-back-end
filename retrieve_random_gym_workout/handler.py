import sys
import psycopg2
import get_body
import get_core
import get_cardio
import os

db_host = os.environ['DB_HOST']
db_port = os.environ['DB_PORT']
db_name = os.environ['DB_NAME']
db_user = os.environ['DB_USERNAME']
db_pass = os.environ['DB_PASSWORD']

def lambda_handler(event, context):

    try:    
        conn = __make_conn()
        result = {}
        if event['cardio']:
            result['cardio'] = get_cardio.get_cardio(conn)
        result['body'] = get_body.get_body(conn)
        if event['core']:
            result['core'] = get_core.get_core(conn)
        
        return result
    except:
        raise 'Unknown error'
    finally:
        conn.close()
        
def __make_conn():
    conn = None
    try:
        conn = psycopg2.connect("dbname='%s' user='%s' host='%s' password='%s'" % (db_name, db_user, db_host, db_pass))
    except:
        raise 'Unable to connect to DB'
    return conn