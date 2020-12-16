from .obtenerNumeroIngresados import *

# obtengo el numero que el usuario me entregara mediante consola.
def obtener_valor_usuario(abaco_dict):
    while True:
        # verifico efectivamente si el numero ingresado es un entero.
        try:
            print ("Si desea terminar la operacion ingrese 'salir'")
            valor_recibido = input("Ingrese un numero entero: ")
            if valor_recibido == "salir" or valor_recibido == "Salir":
                # Muestro todos los numeros que el usuario digito.
                print(obtenerNumerosDiccionario(abaco_dict))
                exit()
            elif not valor_recibido.isdigit():
                print("No es un entero. Intentelo nuevamente")
            elif int(valor_recibido) <= 0:
                print("El valor tiene que ser mayor a 0")
                continue
            else:
                break
        except ValueError:
            print("No es un entero. Intentelo nuevamente")
            continue

    return int(valor_recibido)

# retorna el numero como lista
def descomponer_valor_usuario(numero):
    tmp_valor_lista = list(numero)
    lista_entera = [int(i) for i in tmp_valor_lista]
    while len(lista_entera) < 6:
        lista_entera.insert(0, 0)
    return lista_entera