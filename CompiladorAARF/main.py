# Andrés Ramírez A00831316

# Importación del lexer y parser
from lexico import lexer
from sintactico import parser, DF, pilaOperador, pilaO, pilaTipos, pilaSalto, cuadruplo, constantesCTE
from cuadruplos import Cuadruplo

# Lectura de datos de prueba
with open('test.txt', 'r') as file:
    entrada = file.read()

# Introducimos los datos en el lexer y parse
lexer.input(entrada)
parser.parse(entrada)
#print('Directorio Funciones y Tabla Variables \n')
#DF.prinT()
#print('-------------------------------')

'''program prueba4;
var x, y: int; a, b, result: float;
main {

    x = 5;
    y = 10;
    x = x + y;

    a = 12.5;
    b = 4.2;
    result = a - b;

    if(result != 5.0){
        print("Success: ", x, result);
    } else {
        print("Failure");
    };

}
$'''