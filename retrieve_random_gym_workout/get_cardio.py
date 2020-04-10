import psycopg2
import random

from sql_statement import *

def get_cardio(conn):
    cursor = conn.cursor()
    
    return fetch_cardio_exercises(cursor)
    
def fetch_cardio_exercises(cursor):
    result = []
    
    cursor.execute(cardio_exercise_query)
    
    raw = cursor.fetchall()

    for exercise in raw:
        print(exercise)
        single_body_exercise_object = {}
        single_body_exercise_object["body_part"] = "Cardio"
        single_body_exercise_object["exercise_name"] = exercise[0]
        single_body_exercise_object["image"] = None
        single_body_exercise_object["reps"] = exercise[2]
        single_body_exercise_object["sets"] = exercise[1]
        result.append(single_body_exercise_object)

    return result
    