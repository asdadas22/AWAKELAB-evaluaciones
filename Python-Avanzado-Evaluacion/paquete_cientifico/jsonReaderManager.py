import string
import io
import os
import json

pathjson = "data/flores.json"

# Funcion que chequea si existe o no el json
def start_up_check_json():
    return os.path.isfile(pathjson) and os.access("data/", os.R_OK)

# Funcion para obtener los datos del json.
def get_json_info(pathJson):
    try:
        a_file = open(pathjson, "r")

        json_object = json.load(a_file)

        a_file.close()
        return json_object
    except FileNotFoundError as ex:
        print(type(ex).__name__, ex)

def chequear_Json_flores(diccionario_ref):
    try:
        if os.path.isfile(pathjson) and os.access("data/", os.R_OK):
            # checks if file exists
            print ("File exists and is readable")
            return True
        else:
            print ("Either file is missing or is not readable, creating file...")
            with io.open(os.path.join("data/", 'flores.json'), 'w') as db_file:
                db_file.write(json.dumps(diccionario_ref))
                db_file.close()
            return False
    except Exception as ex:
        print(type(ex).__name__, ex)

# funcion para actualizar el json de las flores.
def update_Json_flores(tipo_flor, letra_flor):
    a_file = open(pathjson, "r")

    json_object = json.load(a_file)

    a_file.close()

    json_object[tipo_flor][letra_flor] += 1


    a_file = open(pathjson, "w")

    json.dump(json_object, a_file)

    a_file.close()
