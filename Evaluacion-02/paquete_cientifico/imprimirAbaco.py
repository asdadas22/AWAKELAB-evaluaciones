from .guardarNumeroDiccionario import *
from .obtenerDatosUsuario import *


def imprimir_abaco(abaco_dict, turno):

    top_abaco = " +--+ "
    bar_abaco = " |  | "
    util_abaco = "XXXXXX"
    lista_columnas = []

    entero_recibido = obtener_valor_usuario(abaco_dict)

    # Aca guardamos en el diccionario el numero descopuesto que el usuario
    # ingreso.
    print(guardar_numero_en_diccionario(abaco_dict, entero_recibido, turno))

    # obtengo una lista con los valores descompuestos del numero
    # por ejemplo 830 > lista_numero[8, 3, 0]
    numero_descompuesto = descomponer_valor_usuario(str(entero_recibido))

    for numero in numero_descompuesto:
        # siempre el abaco debe partir con el top.
        columna_completo = top_abaco
        for i in range(0, (9 - numero)):
            columna_completo = columna_completo + "\n" + bar_abaco
        for valor in range(0, numero):
            columna_completo = columna_completo + "\n" + util_abaco
        columna_completo = columna_completo + "\n" + top_abaco
        lista_columnas.append(columna_completo)
    #otro_string = otro_string + "  " + abaco_completo

    return lista_columnas


def ordenar_abaco(lista_columnas):
    lista_columnas_filas = []
    for columna in lista_columnas:
        filas_columna = columna.split("\n")
        lista_columnas_filas.append(filas_columna)

    abaco_filas = []
    for n in range(0, 11):
        fila = ""
        for columna in lista_columnas_filas:
            fila += "   " + columna[n]
        abaco_filas.append(fila)

    return abaco_filas
