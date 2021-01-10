import paquete_cientifico as pc

class Reseta(pc.Ramo):

    tamanio_dict = {
        "L": "floresGrandes",
        "S": "floresChicas"
    }

    __flores_a_descontar = []

    def __init__(self, flores, ramos):
        self.flores = flores
        self.ramos = ramos


    def chequear_reseta(self, reseta, first_loop=True, count=0, tamanio_reseta=None):
        
        count = count
        reseta_original = reseta
        lista_reseta = list(reseta)
        lista_filtrada = []
        flor_obtenida = None
        if first_loop:
            tamanio_reseta = lista_reseta[1]
            lista_reseta.remove(lista_reseta[0])
            lista_reseta.remove(lista_reseta[0])

        # Obtengo la cantidad de flores y la flor que necesita el ramo
        for i in range(3,):
            if lista_reseta[i].isdigit():
                lista_filtrada.append(lista_reseta[i])
                continue
            else:
                flor_obtenida = lista_reseta[i]
                break
        
        # limpio la reseta para poder re leerla.
        for i in lista_filtrada:
            lista_reseta.remove(i)
        
        lista_reseta.remove(flor_obtenida)

        # obtengo la cantidad de flores que necesito.
        cantidad_flores_necesarias = lista_filtrada[0]
        if len(lista_filtrada) > 1:
            cantidad_flores_necesarias = int(lista_filtrada[0] + lista_filtrada[1])
        
        #print(str(cantidad_flores_necesarias) + "/" + flor_obtenida + "/" + tamanio_reseta)

        # Obtengo la cantidad de flores requeridas del inventario.
        cantidad_flores_inv = self.flores.flores_dict[self.tamanio_dict[tamanio_reseta]][flor_obtenida + tamanio_reseta]
        # agrego un true si me alcanza o false si no, para el posterior descuento.
        if cantidad_flores_inv >= int(cantidad_flores_necesarias):
            self.flores.chequear_cantidad_flores_inv(True)
            # agrego la flor a la cola para luego descontarla del inventario.
            self.__flores_a_descontar.append([self.tamanio_dict[tamanio_reseta], 
                                                flor_obtenida + tamanio_reseta, int(cantidad_flores_necesarias)])
        else:
            self.flores.chequear_cantidad_flores_inv(False)
            if count == 0:
                self.flores.clear_check_cola_flores()
                self.__flores_a_descontar.clear()
                return False
        

        # Vuelvo la receta a str para poder re leerla
        reseta_nueva = "".join(lista_reseta)
        # condicionador para que no haga un loop demas
        if count < 2:
            count += 1
            print(reseta_nueva + " count: " + str(count))
            self.chequear_reseta(reseta_nueva, False, count, tamanio_reseta)
        
        # Se que la primera vuelta de la recursividad es count = 1
        # asi fuerzo el chequeo una vez termine el proceso de verificacion.
        if count == 1:
            if len(self.flores.get_check_flores_inv()) >= 3:
                if False in self.flores.get_check_flores_inv():
                    self.flores.clear_check_cola_flores()
                    self.__flores_a_descontar.clear()
                    return False
                else:
                    
                    for valor in self.__flores_a_descontar:
                        # Descuento las flores del inventario.
                        self.flores.descontar_flor_inventario(valor[0], valor[1], valor[2])
                    self.flores.clear_check_cola_flores()
                    self.__flores_a_descontar.clear()
                     
                    self.ramos.entregar_ramo(reseta_original)
                    
                    
                    return True
            else:
                return False