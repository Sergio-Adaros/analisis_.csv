from pathlib import Path 

# Organización del archivo
def organizar_archivo(nombre_archivo):
    # Definiendo la ruta donde se encuentra el archivo a analizar.
    current_path = Path.cwd()
    current_path = current_path / nombre_archivo

    # Abriendo el archivo.
    with open(current_path) as file: 
        datos_ion = file.readlines() 

    # Organizando los datos en un arreglo
    arreglo = []

    for linea in datos_ion:  
        line_in_list = linea.split(',')
        arreglo.append(line_in_list)
    
    return arreglo

def solicitud_datos():
            
            global columna_id_usuario, id_usuario, datos_usuario

            datos_usuario = str(input("\nCual es el nombre del dato que necesita analizar?: "))
            id_usuario = str(input("\nIngrese el dato referencia: "))
            columna_id_usuario = str(input("\nCuál es el nombre del dato de referencia?: "))


class Objeto_ion():

    def __init__(self, id, nombre_columna_id, nombre_columna) -> None:
        self.id = id
        self.nombre_columna_id = nombre_columna_id
        self.nombre_columna = nombre_columna

    def obtencion_nombre_columna(self, arreglo) -> None:

        self.todas_las_columnas = arreglo.pop(0)

        for num, columna in enumerate(self.todas_las_columnas):
            if columna.lower() == self.nombre_columna.lower(): 
                self.columna_numero = num 
                print(f"La columna seleccionada es {num}")
            elif columna.lower() == self.nombre_columna_id.lower():
                self.numero_columna_id = num

    def organizar_datos(self, arreglo):
    
        lista_datos = []

        for fila in arreglo:
            busqueda_id = fila[self.numero_columna_id]

            recorrido = 1
            while recorrido <= len(busqueda_id):
                encontrando_id = busqueda_id[0:recorrido]
                if encontrando_id == self.id:
                    lista_datos.append(float(fila[self.columna_numero])) #! DATOS SOLICITADOS
                recorrido += 1
                
                
        
        #print(lista_datos)


#! BORRAR
arreglo = organizar_archivo('Revenue Log for PJ-1108A337-02.csv') #* NOMBRE DEL ARCHIVO A ANALIZAR
solicitud_datos()
objeto_prueba = Objeto_ion(id_usuario, columna_id_usuario, datos_usuario) #* NOMBRE_IDENTIFICADOR, COLUMNA_EN_LA_QUE_SE_ENCUENTRA_EL_IDENTIFICADOR, NOMBRE_COLUMNA_A_ANALIZAR

objeto_prueba.obtencion_nombre_columna(arreglo)
objeto_prueba.organizar_datos(arreglo)
