
def obtenerNumerosDiccionario(diccionario_numeros):
    lista_valores_ingresados = []
    for key in diccionario_numeros:
        unidad = diccionario_numeros[key]["unidades"]
        decena =  diccionario_numeros[key]["decena"]
        centena = diccionario_numeros[key]["centena"]
        u_mil = diccionario_numeros[key]["unidad_mil"]
        u_10_mil = diccionario_numeros[key]["unidad_10_mil"]
        u_100_mil = diccionario_numeros[key]["unidad_100_mil"]
        numero_string = str(u_100_mil) + str(u_10_mil) + str(u_mil) + str(centena) + str(decena) + str(unidad)
        lista_valores_ingresados.append(format(int(numero_string), ',d').replace(',','.'))
                    
    return lista_valores_ingresados