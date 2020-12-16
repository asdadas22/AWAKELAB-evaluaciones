
# funcion que divide el numero en unidad, decena, etc.
# y lo guarda en el diccionario
def guardar_numero_en_diccionario(abaco_dict, numero, turno):

    cien_mil = numero / 100000
    tmp =  numero % 100000

    diez_mil = tmp / 10000
    tmp =  numero % 10000

    umil = tmp / 1000
    tmp = numero % 1000

    centenas = tmp / 100
    tmp = tmp % 100

    decenas = tmp / 10
    unidades = tmp % 10


    nuevo_item = "turno_" + str(turno)
    abaco_dict[nuevo_item] = {
        "unidades": int(unidades),
        "decena": int(decenas),
        "centena": int(centenas),
        "unidad_mil": int(umil),
        "unidad_10_mil": int(diez_mil),
        "unidad_100_mil": int(cien_mil),
    }

    return abaco_dict