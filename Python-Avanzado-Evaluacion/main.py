import paquete_cientifico as pc
import random
import time


if __name__ == "__main__":
    # creo el inventario.
    inventario_01 = pc.Inventario("Inventario_Grupo_03")

    reseta_01 = pc.Reseta(inventario_01.flores_ref)
    reseta_01.chequear_reseta("AL8d10r5t30")
    '''
    while True:
        tamanio_flores = random.choice(list(inventario_01.flores_dict))
        flor_agregada = random.choice(list(inventario_01.flores_dict[tamanio_flores]))
        inventario_01.agregar_flor_inventario(tamanio_flores, flor_agregada)
        time.sleep(1)

    '''
    