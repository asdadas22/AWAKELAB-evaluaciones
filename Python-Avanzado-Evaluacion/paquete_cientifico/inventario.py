import paquete_cientifico as pc


class Inventario():

    flores_dict = {
    "floresChicas": {

    },
    "floresGrandes": {

    },
    }

    cola_flores_descontar = []

    def __init__(self, nombre):
        self.nombre = nombre
        print("Inventario Creado")

    # Agregar una flor al azar
    def agregar_flor_inventario(self, tipo, letra_flor):
        self.flores_dict[tipo][letra_flor] += 1
        pc.update_Json_flores(tipo, letra_flor)
        print("La flor %s fue agregada con exito..." % letra_flor)

    # decuento las flores del inventario.
    def descontar_flor_inventario(self, tipo, letra_flor, cantidad):
        self.flores_dict[tipo][letra_flor] -= cantidad
        pc.update_Json_flores(tipo, letra_flor, False, cantidad)
        print("La flor %s fue descontada con exito..." % letra_flor)


    # Chequeo que la cantidad de flores me alcance de acuerdo al inventario.
    # para posteriormente poder hacer el descuento
    def chequear_cantidad_flores_inv(self, alcanza):
        self.cola_flores_descontar.append(alcanza)

    # Retorno la lista que chequea si se puede hacer el ramo
    def get_check_flores_inv(self):
        return self.cola_flores_descontar

    # Limpio la lista que chequea si se puede hacer el ramo.
    def clear_check_cola_flores(self):
        self.cola_flores_descontar.clear()

