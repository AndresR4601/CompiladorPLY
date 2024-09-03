# Importa clase de tabla de variables
from varTable import tabla_Variables

# Definición de la clase de directorio de funciones
class directorio_Funciones(dict):
    # Método default para crear directorio
    def __init__(self):
        self.directorio_funciones = {}
        self.current_ID = None
        self.global_ID = None

    # Método para set el ID para funcion de directorio
    def set_current_ID(self, nombre):
        self.current_ID = nombre

    # Método para set el ID para var global
    def set_global_ID(self, nombre):
        self.global_ID = nombre

    # Método para accesar el ID del directorio
    def get_current_ID(self):
        return self.current_ID

    # Método para agregar función a directorio
    def agregarADirectorio(self, nombre, tipo):
        if nombre in self.directorio_funciones:
            print("Este nombre para función ya existe: ", self.current_ID)
        self.directorio_funciones[nombre] = [tipo, tabla_Variables()] 
        self.current_ID = nombre

    # Método para agrega datos a la tabla
    def actualizar_tabla(self, nombreVar, tipoVar, memoria):
        if self.current_ID in self.directorio_funciones:
            self.directorio_funciones[self.current_ID][1].agregarATabla(nombreVar, tipoVar, memoria)
        else:
            print("La función no existe")

    # Método para buscar el tipo de variable por su nombre en tablaVar local o global
    def buscar_tipo_var(self, nombreVar):
        if self.current_ID in self.directorio_funciones:
            tipoVar = self.directorio_funciones[self.current_ID][1].buscarTipo(nombreVar)
            if tipoVar == False:
                tipoVar = self.directorio_funciones[self.global_ID][1].buscarTipo(nombreVar)
                if tipoVar == False:
                    print("Variable no declarada")
                else:
                    return tipoVar
            else:
                return tipoVar
        else:
            print("La función no existe")

    # Método para buscar el espacio de variable por su nombre en tablaVar local o global
    def buscar_memoria_var(self, nombreVar):
        if self.current_ID in self.directorio_funciones:
            tipoVar = self.directorio_funciones[self.current_ID][1].buscarMemoria(nombreVar)
            if tipoVar == False:
                tipoVar = self.directorio_funciones[self.global_ID][1].buscarMemoria(nombreVar)
                if tipoVar == False:
                    print("Variable no declarada")
                else:
                    return tipoVar
            else:
                return tipoVar
        else:
            print("La función no existe")
            
    # Método para borrar tabla
    def borrar_tabla(self):
        self.directorio_funciones[self.current_ID][1] = tabla_Variables()
            
    # Método para vizualizar datos 
    def prinT(self):
        for key, value in self.directorio_funciones.items():
            print(key + ':', value[0])
            tabla_vars = value[1]
            tabla_vars.printVar()
