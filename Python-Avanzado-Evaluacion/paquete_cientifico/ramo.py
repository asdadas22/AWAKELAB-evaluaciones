import paquete_cientifico as pc

class Ramo():

    ramos_dict_entregados = {
        
    }

    ramos_activos = {

    }

    def __init__(self):
        # Chequeo la existencia del "ramos historicos" si no lo creo.
        if not pc.jsonReaderManager.start_up_check_json("data/ramos_creados.json"):
            pc.jsonReaderManager.chequear_Json_files("data/ramos_creados.json", 
                                                        self.ramos_dict_entregados, "ramos_creados.json")
        else:
            self.ramos_dict_entregados = pc.jsonReaderManager.get_json_info("data/ramos_creados.json")

        self.ramos_activos = pc.jsonReaderManager.get_json_info("data/ramo_reseta.json")


    def entregar_ramo(self, ramo):
        try:
            valor_ramo = self.ramos_dict_entregados[ramo]
            self.ramos_dict_entregados.update({ramo: valor_ramo + 1})
        except Exception as ex:
            print(type(ex).__name__, ex)
            print("Agregando %s al diccionario" % ramo)
            self.ramos_dict_entregados.update({ramo: 1})
            
        pc.jsonReaderManager.update_Json_reseta_creados(self.ramos_dict_entregados)

    def get_ramo(self, tamanio_ramo, ramo):
        return self.ramos_activos[tamanio_ramo][ramo]