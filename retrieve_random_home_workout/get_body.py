import psycopg2
import random

from sql_statement import body_type_query,body_exercise_query

def get_body(conn):
    cursor = conn.cursor()
    body_parts = fetch_body_type(cursor)

    return generate_random_body_exercises(cursor, body_parts)
    
def fetch_body_type(cursor):
    result = {}
    
    cursor.execute(body_type_query)

    raw = cursor.fetchall()
    
    for line in raw:
        result[str(line[0])] = line[1]
    
    return result

def generate_random_body_exercises(cursor, body_types):
    body_types_keys = list(body_types.keys())
    body_exercises = []
    count = 0
    
    while count < 4:
        single_body_exercise_object = {}
        random_part_choice = random.choice(body_types_keys)
        exercise_name,sets,reps = fetch_body_exercise(cursor, random_part_choice)
        if len(exercise_name) > 1:
            body_part = body_types.get(random_part_choice)
            single_body_exercise_object["body_part"] = body_part
            single_body_exercise_object["exercise_name"] = exercise_name
            single_body_exercise_object["image"] = None
            single_body_exercise_object["reps"] = reps
            single_body_exercise_object["sets"] = sets
            body_types_keys.remove(random_part_choice)
            body_exercises.append(single_body_exercise_object)
            count += 1
    
    return body_exercises
    
def fetch_body_exercise(cursor, body_type_id):
    cursor.execute(body_exercise_query.format(body_type_id))
    
    result = cursor.fetchall()
    
    if len(result) == 0:
        return '', None, None
    else:
        return result[0][0], result[0][1], result[0][2]