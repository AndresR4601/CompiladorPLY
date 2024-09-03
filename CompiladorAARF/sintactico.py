# Librerias o clases declaradas
from dirFunc import directorio_Funciones
from semantica import cubo_semantico
from cuadruplos import Cuadruplo
import ply.yacc as yacc
from lexico import tokens

# Traducción de operadores en los cuádruplos
'''
    +  -> 1
    -  -> 2
    *  -> 3
    /  -> 4

    >  -> 5
    <  -> 6
    != -> 7

    =  -> 8
    print -> 9
    GoToF -> 10
    GoToV -> 11
    GoTo -> 12
    
'''

# Manejo de memoria para los cuadruplos y Maquina Virtual
memoriaGlobalInt= iter(range(1000, 1099))
listMGI = []
memoriaGlobalFloat= iter(range(1100, 1199))
listMGF = []
memoriaTempInt = iter(range(2000, 2099))
listMTI = []
memoriaTempFloat = iter(range(2100, 2199))
listMTF = []
memoriaTempBool = iter(range(2200, 2299))
listMTB = []
memoriaCTEInt = iter(range(3000, 3099))
listMCI = []
memoriaCTEFloat = iter(range(3100, 3199))
listMCF = []
memoriaCTEString = iter(range(3200, 3299))
listMCS = []

# Pila auxiliar de ids para las tablas de variables
pilaID = []
# Diccionario de constantes 
constantesCTE = {}

# Pilas para la generación de cuádruplos
pilaO = []
pilaOperador = []
pilaTipos = []
pilaSalto = []

# Creación de estructura de cuádruplos
cuadruplo = Cuadruplo()

# Variable para saber sobre que tipo de función o variable al que me estoy refiriendo
current_Type = 'void'
# Variable para recordar las variables globales
current_Global = None

# Creación de directorio de funciones
DF = directorio_Funciones()

#Definición de la gramática formal
# ----------------------------------------------------------------------------------------------------------------------
#-----------------------program-----------------------#
def p_program(parse):
    'program : PROGRAMA ID pn1 P_COMA dec_Vars dec1_F MAIN Body END'
    
def p_dec_Vars(parse):
    '''dec_Vars : Vars 
                | epsilon'''

def p_dec1_F(parse):
    '''dec1_F : Funcs dec1_F 
              | epsilon'''
    
# Punto neurálgico para agregar función global al directorio
def p_pn1(parse):
    'pn1 : '
    current_Global = parse[-1]
    # Guardo el id global para poder buscar variables globales
    DF.set_global_ID(current_Global)
    DF.agregarADirectorio(current_Global, current_Type)
    
#-----------------------program-----------------------#
#-----------------------Vars-----------------------#

def p_Vars(parse):
    'Vars : VARIABLE mas_Vars'

def p_mas_Vars(parse):
    'mas_Vars : id_Vars P_PUNTO Type pn2 P_COMA rep_Vars'

def p_id_Vars(parse):
    'id_Vars : ID pn3 mas_id'

def p_mas_id(parse):
    '''mas_id : COMA id_Vars 
              | epsilon'''

def p_rep_Vars(parse):
    '''rep_Vars : mas_Vars 
                | epsilon'''

# Punto neurálgico para agregar variables guardadas en pilaID a la tabla de variables de la función correspondiente
def p_pn2(parse):
    'pn2 : '
    current_Type = parse[-1]
    while pilaID:
        ids = pilaID.pop()
        if(current_Type == 'int'):
            memoria = next(memoriaGlobalInt)
            # Agregamos a estructuras de memoria el id en indice respectivo al tipo
            listMGI.insert(memoria-1000, ids)
        else:
            memoria = next(memoriaGlobalFloat)
            listMGF.insert(memoria-1100, ids)
        DF.actualizar_tabla(ids, current_Type, memoria)

# Punto neuralgico para agregar los ids a la pilaID
def p_pn3(parse):  
    'pn3 : '
    pilaID.append(parse[-1])

#-----------------------Vars-----------------------#
#-----------------------Body-----------------------#

def p_Body(parse):
    'Body : K_IZQUIERDO dec_State K_DERECHO'

def p_dec_State(parse):
    '''dec_State : Statement dec_State 
                 | epsilon'''
    
#-----------------------Body-----------------------#
#-----------------------Statement-----------------------#

def p_Statement(parse):
    '''Statement : Assign 
                 | Condition 
                 | Cycle 
                 | F_Call 
                 | Print'''
    
#-----------------------Statement-----------------------#
#-----------------------Print-----------------------#

def p_Print(parse):
    'Print : PRINT P_IZQUIERDO dec_Expresion P_DERECHO P_COMA'

def p_dec_Expresion(parse):
    '''dec_Expresion : Expresion pn2p mas_Print
                     | CTE_STRING  pn1p mas_Print'''
    
def p_mas_Print(parse):
    '''mas_Print : COMA dec_Expresion 
                 | epsilon'''    
    
# Punto neurálgico para generar cuádruplo de print con la constante string
def p_pn1p(parse):
    'pn1p : '
    valor = next(memoriaCTEString)
    # Agregamos a estructuras de memoria la constante string en indice respectivo al tipo
    listMCS.insert(valor-3200, parse[-1])
    constantesCTE[parse[-1]] = ['string', valor]
    cuadruplo.agregarCuadruplo(9, -1, -1, valor)

# Punto neurálgico para generar cuádruplo de print con valor de la pilaO
def p_pn2p(parse):
    'pn2p : '
    aux = pilaO.pop()
    pilaTipos.pop()
    cuadruplo.agregarCuadruplo(9, -1, -1, aux)

#-----------------------Print-----------------------#
#-----------------------Cycle-----------------------#

def p_Cycle(parse):
    'Cycle : DO pn1c Body WHILE P_IZQUIERDO Expresion pn2c P_DERECHO P_COMA'   

# Punto neurálgico para guardar la migaja en la pilaSalto
def p_pn1c(parse):
    'pn1c : '
    pilaSalto.append(cuadruplo.indice)

# Punto neurálgico para generar cuádruplo en True para volver 
def p_pn2c(parse):
    'pn2c : '
    aux = pilaSalto.pop()
    resultado = pilaO.pop()
    pilaTipos.pop()
    cuadruplo.agregarCuadruplo(11, resultado, -1, aux)

#-----------------------Cycle-----------------------#
#-----------------------Condition-----------------------#

def p_Condition(parse):
    'Condition : IF P_IZQUIERDO Expresion pn1i P_DERECHO Body mas_if P_COMA pn2i '

def p_mas_if(parse):
    '''mas_if : ELSE pn3i Body 
              | epsilon'''

# Punto neurálgico para agregar cuádruplo de GoToF y la migaja en pilaSalto 
def p_pn1i(parse):
    'pn1i : '
    tipoExpresion = pilaTipos.pop()
    if tipoExpresion == 'bool':
        result = pilaO.pop()
        cuadruplo.agregarCuadruplo(10, result, -1, -1)
        pilaSalto.append(cuadruplo.indice-1)
    else:
        raise ValueError("Error: Type Mismatch -> ", tipoExpresion)

# Punto neurálgico para actualizar el cuádruplo GoToF 
def p_pn2i(parse):
    'pn2i : '
    end = pilaSalto.pop()
    cuadruplo.actualizarCuadruplo(end, cuadruplo.indice)

# Punto neurálgico para actualizar el cuádruplo GoToF y crear el GoTo de ser verdadero
def p_pn3i(parse):
    'pn3i : '
    cuadruplo.agregarCuadruplo(12, -1, -1, -1)
    false = pilaSalto.pop()
    pilaSalto.append(cuadruplo.indice-1)
    cuadruplo.actualizarCuadruplo(false, cuadruplo.indice)

#-----------------------Condition-----------------------#
#-----------------------Assign-----------------------#

def p_Assign(parse):
    'Assign : ID pn1a IGUAL pn2a Expresion pn3a P_COMA'

# Punto neurálgico para guardar operando y su tipo en las pilas
def p_pn1a(parse):
    'pn1a : '
    valor = DF.buscar_memoria_var(parse[-1])
    ty = DF.buscar_tipo_var(parse[-1])
    pilaO.append(valor)
    pilaTipos.append(ty)

# Punto neurálgico para guardar el operador en la pilaOperator
def p_pn2a(parse):
    'pn2a : '
    pilaOperador.append(parse[-1])

# Punto neurálgico para crear cuádruplo de asignación 
def p_pn3a(parse):
    'pn3a : '
    if len(pilaOperador) != 0:
        aux = pilaOperador.pop()
        if(aux == '='):
            operandoI = pilaO.pop()
            tipoOI = pilaTipos.pop()
            operandoD = pilaO.pop()
            tipoOD = pilaTipos.pop()
            type = cubo_semantico[tipoOI][tipoOD][aux]
            if type == 'error':
                raise ValueError('Error: Type mismatch -> ', tipoOI, tipoOD)
            else:
                cuadruplo.agregarCuadruplo(8, operandoI, -1, operandoD)
        else:
            pilaOperador.append(aux)

#-----------------------Assign-----------------------#
#-----------------------Expresion-----------------------#

def p_Expresion(parse):
    'Expresion : EXP mas_E'

def p_mas_E(parse):
    '''mas_E : operators pn8e EXP pn9e
             | epsilon'''
    
def p_operators(parse):
    '''operators : MAYOR  
                 | MENOR 
                 | DIFE'''
    parse[0] = parse[1]

def p_EXP(parse):
    'EXP : Termino pn4e mas_EXP'

def p_mas_EXP(parse):
    '''mas_EXP : SUMA pn3e EXP 
               | RESTA  pn3e EXP 
               | epsilon'''
    
# Punto neurálgico para guardar operador + o - en la pilaOperador
def p_pn3e(parse):
    'pn3e : '
    pilaOperador.append(parse[-1])   

# Punto neurálgico para hacer las sumas o restas pendientes en la pilaOperador y crear el cuádruplo
def p_pn4e(parse):
    'pn4e : '
    if len(pilaOperador) != 0:
        aux = pilaOperador.pop()
        if(aux == '+' or aux == '-'):
            operandoD = pilaO.pop()
            tipoD = pilaTipos.pop()
            operandoI  = pilaO.pop()
            tipoI = pilaTipos.pop()
            result_type = cubo_semantico[tipoI][tipoD][aux]

            if(result_type != 'error'):
                # Agregamos a estructuras de memoria temporal un 0 en indice respectivo al tipo
                if(result_type == 'float'):
                    result = next(memoriaTempFloat)
                    listMTF.insert(result-2100, 0)
                else:
                    result = next(memoriaTempInt)
                    listMTI.insert(result-2000, 0)
                if(aux == '+'):
                    aux = 1
                else:
                    aux = 2
                cuadruplo.agregarCuadruplo(aux, operandoI, operandoD, result)
                pilaO.append(result)
                pilaTipos.append(result_type)
            else:
                raise ValueError("Error: Type Mismatch", tipoI, tipoD)
        else:
            pilaOperador.append(aux)

# Punto neurálgico para guardar el operador <, > o != en la pilaOperador
def p_pn8e(parse):
    'pn8e : '
    pilaOperador.append(parse[-1]) 

# Punto neurálgico para hacer las comparaciones pendientes en la pilaOperador y crear el cuádruplo
def p_pn9e(parse):
    'pn9e : '
    if len(pilaOperador) != 0:
        aux = pilaOperador.pop()
        if(aux == '<' or aux == '>' or aux == '!='):
            operandoD = pilaO.pop()
            tipoD = pilaTipos.pop()
            operandoI  = pilaO.pop()
            tipoI = pilaTipos.pop()
            result_type = cubo_semantico[tipoI][tipoD][aux]

            if(result_type != 'error'):
                # Agregamos a estructuras de memoria temporal un 0 en indice respectivo al tipo
                result = next(memoriaTempBool)
                listMTB.insert(result-2200, 0)
                if(aux == '>'):
                    aux = 5
                elif(aux == '<'):
                    aux = 6
                else:
                    aux = 7
                cuadruplo.agregarCuadruplo(aux, operandoI, operandoD, result)
                pilaO.append(result)
                pilaTipos.append(result_type)
            else:
                raise ValueError("Error: Type Mismatch", tipoI, tipoD)
        else:
            pilaOperador.append(aux)

#-----------------------Expresion-----------------------#
#-----------------------Termino-----------------------#
def p_Termino(parse):
    'Termino : Factor pn5e mas_Term'    

def p_mas_Term(parse):
    '''mas_Term : MULT pn2e Termino 
                | DIV pn2e Termino 
                | epsilon'''

# Punto neurálgico para agregar operador de * o / a la pilaOperador
def p_pn2e(parse):
    'pn2e : '
    pilaOperador.append(parse[-1])

# Punto neurálgico hacer las multiplicaciones o divisiones pendientes en la pilaOperador y crear el cuádruplo
def p_pn5e(parse):
    'pn5e : '
    if len(pilaOperador) != 0:
        aux = pilaOperador.pop()
        if(aux == '*' or aux == '/'):
            operandoD = pilaO.pop()
            tipoD = pilaTipos.pop()
            operandoI  = pilaO.pop()
            tipoI = pilaTipos.pop()
            result_type = cubo_semantico[tipoI][tipoD][aux]

            if(result_type != 'error'):
                # Agregamos a estructuras de memoria temporal un 0 en indice respectivo al tipo
                if(result_type == 'float'):
                    result = next(memoriaTempFloat)
                    listMTF.insert(result-2100, 0)
                else:
                    result = next(memoriaTempInt)
                    listMTI.insert(result-2000, 0)
                if(aux == '*'):
                    aux = 3
                else:
                    aux = 4
                cuadruplo.agregarCuadruplo(aux, operandoI, operandoD, result)
                pilaO.append(result)
                pilaTipos.append(result_type)
            else:
                raise ValueError("Error: Type Mismatch", tipoI, tipoD)
        else:
            pilaOperador.append(aux)

#-----------------------Termino-----------------------#
#-----------------------Factor-----------------------#

def p_Factor(parse):
    '''Factor : P_IZQUIERDO pn6e Expresion pn7e P_DERECHO 
              | dec_Factor mas_Factor '''

def p_dec_Factor(parse):
    '''dec_Factor : SUMA 
                  | RESTA 
                  | epsilon'''

def p_mas_Factor(parse):
    '''mas_Factor : ID pn1e
                  | CTE pn1e2'''

# Punto neurálgico para guardar el operando
def p_pn1e(parse):
    'pn1e : '
    valor = DF.buscar_memoria_var(parse[-1])
    tipoV = DF.buscar_tipo_var(parse[-1])
    pilaO.append(valor)
    pilaTipos.append(tipoV)

# Punto neurálgico para guardar la constante
def p_pn1e2(parse):
    'pn1e2 : '
    valor = constantesCTE[parse[-1]][1]
    pilaO.append(valor)
    tipoV = constantesCTE[parse[-1]][0]
    pilaTipos.append(tipoV)

# Punto neurálgico para agregar un fondo falso en la pilaOperadores
def p_pn6e(parse):
    'pn6e : '
    pilaOperador.append('(')

# Punto neurálgico para quitar fondo falso de la pilaOperador
def p_pn7e(parse):
    'pn7e : '
    if len(pilaOperador) != 0:
        aux = pilaOperador.pop()
        if aux != '(':
            pilaOperador.append(aux)

#-----------------------Factor-----------------------#
#-----------------------CTE-----------------------#

def p_CTE(parse):
    '''CTE : CTE_FLOAT pnAux
           | CTE_INT pnAux2'''
    parse[0] = parse[1]

# Punto neurálgico de ayuda para guardar tipo de constante
def p_pnAux(parse):
    'pnAux : '
    aux = next(memoriaCTEFloat)
    listMCF.insert(aux-3100, parse[-1])
    constantesCTE[parse[-1]] = ['float', aux]

# Punto neurálgico de ayuda para guardar tipo de constante
def p_pnAux2(parse):
    'pnAux2 : ' 
    aux = next(memoriaCTEInt)
    listMCI.insert(aux-3000, parse[-1])
    constantesCTE[parse[-1]] = ['int', aux]

#-----------------------CTE-----------------------#
#-----------------------Funcs-----------------------#
    
def p_Funcs(parse):
    'Funcs : VOID ID pn4 P_IZQUIERDO mas_Func P_DERECHO B_IZQUIERDO dec_Vars Body pn6 B_DERECHO P_COMA'

def p_mas_Func(parse):
    '''mas_Func : ID P_PUNTO Type pn5 mas2_Func
                | epsilon '''
    
def p_mas2_Func(parse):
    '''mas2_Func : COMA mas_Func 
                 | epsilon'''

# Punto neurálgico para agregar función al directorio
def p_pn4(parse):
    'pn4 : '
    current_Type = 'void'
    DF.agregarADirectorio(parse[-1], current_Type)

# Punto neurálgico para agregar las variables de la función a la tabla de variables
def p_pn5(parse):
    'pn5 : '
    if(parse[-1] == 'int'):
        memoria = next(memoriaGlobalInt)
        listMGI.insert(memoria-1000, parse[-3])
    else:
        memoria = next(memoriaGlobalFloat)
        listMGF.insert(memoria-1100, parse[-3])
    DF.actualizar_tabla(parse[-3], parse[-1], memoria)

# Punto neurálgico para borrar tabla de variables
def p_pn6(parse):
    'pn6 : '
    DF.borrar_tabla()

#-----------------------Funcs-----------------------#
#-----------------------FCall-----------------------#

def p_F_Call(parse):
    'F_Call : ID P_IZQUIERDO mas_F P_DERECHO P_COMA'

def p_mas_F(parse):
    '''mas_F : Expresion mas2_F 
             | epsilon'''

def p_mas2_F(parse):
    '''mas2_F : COMA mas_F 
              | epsilon'''

#-----------------------FCall-----------------------#

def p_Type(parse):
    '''Type : ENTERO 
            | FLOTANTE'''
    parse[0] = parse[1]

def p_epsilon(parse):
    'epsilon : '
    pass

def p_error(parse):
    raise ValueError("ERROR de Parse")

# ----------------------------------------------------------------------------------------------------------------------

#Construcción del parser
parser = yacc.yacc()
