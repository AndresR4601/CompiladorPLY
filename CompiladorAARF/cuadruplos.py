# Definición para la estructura de cuadruplos
class Cuadruplo:
    # Método defaul para crea estructura
    def __init__(self):
        self.cuadruplo = []
        self.indice = 0

    # Método para agregar registro de cuádruplo
    def agregarCuadruplo(self, operador, operandoI, operandoD, resultado):
        cuadruplo = (self.indice, operador, operandoI, operandoD, resultado)
        self.cuadruplo.append(cuadruplo)
        self.indice += 1

    # Método print para la visualización de los cuádruplos
    def printC(self):
        for x in self.cuadruplo:
            print(f'{x[0]}: ({x[1]}, {x[2]}, {x[3]}, {x[4]})')

    # Método para actualizar los cuádruplos de tipo GoTo
    def actualizarCuadruplo(self, indice, resultado):
        for i, x in enumerate(self.cuadruplo):
            if x[0] == indice:
                self.cuadruplo[i] = (x[0], x[1], x[2], x[3], resultado)