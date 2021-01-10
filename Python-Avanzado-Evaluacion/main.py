import paquete_cientifico as pc
import random
import time


if __name__ == "__main__":
    # Al crear flores y esta heredar de inventario solo me basta
    # con instanciar flores para poder crear un inventario.
    flores_01 = pc.Flores()
    ramos_01 = pc.Ramo()

    reseta_01 = pc.Reseta(flores_01, ramos_01)
    
    while True:
        tamanio_flores = random.choice(list(flores_01.flores_dict))
        flor_agregada = random.choice(list(flores_01.flores_dict[tamanio_flores]))
        flores_01.agregar_flor_inventario(tamanio_flores, flor_agregada)
        
        # Chequeo de los ramos existentes para hacer
        for ramoGrande in list(ramos_01.ramos_activos["ramoGrande"]):
            print("Chequeando el ramo: " + ramos_01.get_ramo("ramoGrande", ramoGrande))
            if reseta_01.chequear_reseta(ramos_01.get_ramo("ramoGrande", ramoGrande)):
                print("El ramo se creo con exito!")
            else:
                print("El ramo %s no pudo ser creado porque faltan flores" % ramos_01.get_ramo("ramoGrande", ramoGrande))

        for ramoChico in list(ramos_01.ramos_activos["ramoChico"]):
            print("Chequeando el ramo: " + ramos_01.get_ramo("ramoChico", ramoChico))
            if reseta_01.chequear_reseta(ramos_01.get_ramo("ramoChico", ramoChico)):
                print("El ramo se creo con exito!")
            else:
                print("El ramo %s no pudo ser creado porque faltan flores" % ramos_01.get_ramo("ramoChico", ramoChico))
        # delay de 1 segundo para que no explote.
        time.sleep(1)

    