import paquete_cientifico as pc


class Inventario():

    flores_dict = {
    "floresChicas": {

    },
    "floresGrandes": {

    },
    }

    def __init__(self, nombre):
        self.nombre = nombre
        #self.agregar_flores_dict()
        self.flores_ref = pc.Flores()
        print("Inventario Creado")

    # Agregar una flor al azar
    def agregar_flor_inventario(self, tipo, letra_flor):
        self.flores_dict[tipo][letra_flor] += 1
        pc.update_Json_flores(tipo, letra_flor)
        print("La flor %s fue agregada con exito..." % letra_flor)

