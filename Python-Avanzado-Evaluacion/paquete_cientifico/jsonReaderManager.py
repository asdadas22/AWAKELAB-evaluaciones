import string
import io
import os
import json



# Funcion que chequea si existe o no el json
def start_up_check_json(pathJson):
    return os.path.isfile(pathJson) and os.access("data/", os.R_OK)

# Funcion para obtener los datos del json.
def get_json_info(pathJson):
    try:
        a_file = open(pathJson, "r")

        json_object = json.load(a_file)

        a_file.close()
        return json_object
    except FileNotFoundError as ex:
        print(type(ex).__name__, ex)

def chequear_Json_files(pathJson, diccionario_ref, new_json_name):
    try:
        if os.path.isfile(pathJson) and os.access("data/", os.R_OK):
            # checks if file exists
            print ("File exists and is readable")
            return True
        else:
            print ("Either file is missing or is not readable, creating file...")
            with io.open(os.path.join("data/", new_json_name), 'w') as db_file:
                db_file.write(json.dumps(diccionario_ref))
                db_file.close()
            return False
    except Exception as ex:
        print(type(ex).__name__, ex)

def update_Json_reseta_creados(ramos_dict):
    a_file = open("data/ramos_creados.json", "r")

    json_object = json.load(a_file)

    a_file.close()

    json_object = ramos_dict

    a_file = open("data/ramos_creados.json", "w")

    json.dump(json_object, a_file)

    a_file.close()    

# funcion para actualizar el json de las flores.
def update_Json_flores(tipo_flor, letra_flor, agregar = True, cantidad=0):
    a_file = open("data/flores.json", "r")

    json_object = json.load(a_file)

    a_file.close()
    if agregar:
        json_object[tipo_flor][letra_flor] += 1
    else:
        json_object[tipo_flor][letra_flor] -= cantidad

    a_file = open("data/flores.json", "w")

    json.dump(json_object, a_file)

    a_file.close()
