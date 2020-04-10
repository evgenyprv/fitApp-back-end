import psycopg2
import random

from sql_statement import core_type_query, core_exercise_query

def get_core(conn):
    cursor = conn.cursor()
    core_types = fetch_core_type(cursor)

    return generate_random_core_exercises(cursor, core_types)
    
def fetch_core_type(cursor):
    result = {}
    
    cursor.execute(core_type_query)
    
    raw = cursor.fetchall()
    for line in raw:
        result[str(line[0])] = line[1]
    
    return result
    
def generate_random_core_exercises(cursor, core_types):
    core_types_keys = list(core_types.keys())
    result = []

    count = 0
    while count < 3:
        single_core_exercise_object = {}
        random_core_part = random.choice(core_types_keys)
        exercise_name,sets,reps = fetch_core_exercise(cursor, random_core_part)
        if len(exercise_name) > 1:
            core_part = core_types.get(random_core_part)
            single_core_exercise_object["body_part"] = core_part
            single_core_exercise_object["exercise_name"] = exercise_name
            single_core_exercise_object["image"] = None
            single_core_exercise_object["reps"] = reps
            single_core_exercise_object["sets"] = sets
            core_types_keys.remove(random_core_part)
            result.append(single_core_exercise_object)
            count += 1
            
    
    return result
    
def fetch_core_exercise(cursor, core_pard_id):
    cursor.execute(core_exercise_query.format(core_pard_id))
    
    result = cursor.fetchall()

    if len(result) == 0:
        return '', None, None
    else:
        return result[0][0], result[0][1], result[0][2]