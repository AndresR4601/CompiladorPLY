# Definición de tabla de Variables con diccionario 
# Key = nombre, value = type
class tabla_Variables(dict):
    # Método default para creación del diccionario como tabla de variables
    def __init__(self):
        self.tabla_Variables = {}

    # Método para agregar nuevo registro a la tabla
    def agregarATabla(self, nombre, tipo, memoria):
        if nombre not in self.tabla_Variables:
            self.tabla_Variables[nombre] = [tipo, memoria]
        else:
            print("Este nombre para función ya existe")
    
    # Método para obtener el tipo de una variable
    def buscarTipo(self, nombre):
        if nombre in self.tabla_Variables:
            return self.tabla_Variables[nombre][0]
        else:
            return False
        
    # Método para obtener el espacio de memoria asignado en una variable
    def buscarMemoria(self, nombre):
        if nombre in self.tabla_Variables:
            return self.tabla_Variables[nombre][1]
        else:
            return False

    # Método print para vizualización
    def printVar(self):
        if self.tabla_Variables != {}:
            for key, value in self.tabla_Variables.items():
                print(key, ' : Tipo', value[0], ', Memoria ', value[1] )
