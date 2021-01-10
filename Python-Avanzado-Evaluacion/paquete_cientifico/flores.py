import string
import paquete_cientifico as pc

class Flores(pc.Inventario):

    def __init__(self):
        self.agregar_flores_invitario()
        super().__init__("Inventario_01")


    def creando_inventario_flores(self, tamaño_flor, letra_flor):
        super().flores_dict[tamaño_flor].update({letra_flor: 0})
    
    # Este metodo se ejecuta solo una vez al momento de inicializar por primera vez el programa.
    def agregar_flores_invitario(self):
        # Agrego las flores  al diccionario.
        if not pc.jsonReaderManager.start_up_check_json("data/flores.json"):
            
            for index, valor in enumerate(string.ascii_lowercase):
                self.creando_inventario_flores("floresChicas", (valor + "S"))
                self.creando_inventario_flores("floresGrandes", (valor + "L"))
            pc.jsonReaderManager.chequear_Json_files("data/flores.json", super().flores_dict, "flores.json")
        else:
            pc.Inventario.flores_dict = pc.get_json_info("data/flores.json")