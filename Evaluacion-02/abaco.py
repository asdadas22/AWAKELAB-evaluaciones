import time
import paquete_cientifico as pc

# diccionario del abaco
abaco_dict = {
}


if __name__ == "__main__":
    turno = 0
    while True:
        turno += 1
        lista_columnas = pc.imprimir_abaco(abaco_dict, turno)
        
        fila_lista = pc.ordenar_abaco(lista_columnas)

        for fila in fila_lista:
            print(fila)