import sql
import psycopg2
    
def get_workout_type(conn):
    cursor = conn.cursor()
 
    home_result = __get_home_type_workout(cursor)
    gym_result = __get_gym_type_workout(cursor)

    return {"home" : home_result, "gym": gym_result}

def __get_home_type_workout(cursor):
    cursor.execute(sql.sql_home_type_str)

    raw = cursor.fetchall()
        
    return __process_db_data(raw)

def __get_gym_type_workout(cursor):
    cursor.execute(sql.sql_gym_type_str)

    raw = cursor.fetchall()
        
    return __process_db_data(raw)

def __process_db_data(raw):
    result = []
    
    for line in raw:
        type_workout_obj = {'workout_type': line[0]}
        result.append(type_workout_obj)
        
    return result