import paquete_cientifico as pc

class Reseta(pc.Ramo):

    def __init__(self, flores):
        self.flores = flores


    def chequear_reseta(self, reseta, first_loop=True, count=0, tamanio_reseta=None):
        
        count = count
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

        if tamanio_reseta == "L":
            print(self.flores.flores_dict["floresGrandes"][flor_obtenida + tamanio_reseta])
        else:
            print(self.flores.flores_dict["floresChicas"][flor_obtenida + tamanio_reseta])

        result = lista_filtrada[0]
        if len(lista_filtrada) > 1:
            result = int(lista_filtrada[0] + lista_filtrada[1])
        
        print(str(result) + "/" + flor_obtenida + "/" + tamanio_reseta)
        # Vuelvo la receta a str para poder re leerla
        reseta_nueva = "".join(lista_reseta)
        # condicionador para que no se caiga el programa xD
        if count < 2:
            count += 1
            print(reseta_nueva)
            self.chequear_reseta(reseta_nueva, False, count, tamanio_reseta)
        
        


    
        '''
        print(lista_reseta[2].isdigit())
        print(lista_txt[3].isdigit())
        print(int(lista_txt[2] + lista_txt[3]))
        lista_txt.remove("1")
        lista_txt.remove("0")
        lista_txt.remove("d")
        print(lista_txt[4].isdigit())
        print(lista_txt)
        print(lista_txt[2].isdigit())
        print(lista_txt[3].isdigit())
        print(int(lista_txt[2]))
        lista_txt.remove("5")
        lista_txt.remove("r")
        print(lista_txt)
        '''