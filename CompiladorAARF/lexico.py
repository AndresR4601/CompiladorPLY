#Libreria
import ply.lex as lex

#Definición de palabras reservadas
reservadas = {
    'program' : 'PROGRAMA',
    'main' : 'MAIN',
    'print' : 'PRINT',
    'int' : 'ENTERO',
    'float' : 'FLOTANTE',
    'var' : 'VARIABLE',
    'if' : 'IF',
    'else' : 'ELSE',
    'while' : 'WHILE', 
    'do' : 'DO',
    'void' : 'VOID',
}

#Definición de Tokens
tokens = ['ID', 'CTE_FLOAT', 'CTE_INT', 'CTE_STRING', 
         'SUMA', 'RESTA', 'MULT', 'DIV', 
         'MAYOR', 'MENOR', 'IGUAL', 'DIFE',
         'P_IZQUIERDO', 'P_DERECHO', 'B_IZQUIERDO', 'B_DERECHO', 'K_IZQUIERDO', 'K_DERECHO', 
         'P_PUNTO', 'P_COMA', 'COMA', 'END'] + list(reservadas.values())

t_SUMA = r'\+'
t_RESTA = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_MAYOR = r'>'
t_MENOR = r'<'
t_IGUAL = r'='
t_DIFE = r'!='
t_P_IZQUIERDO = r'\('
t_P_DERECHO = r'\)'
t_B_IZQUIERDO = r'\['
t_B_DERECHO = r'\]'
t_K_IZQUIERDO = r'\{'
t_K_DERECHO = r'\}'
t_P_PUNTO = r':'
t_P_COMA = r';'
t_COMA = r','
t_END = r'\$'

def t_ID(tok):
    r'[A-Za-z][A-Za-z0-9]*'
    tok.type = reservadas.get(tok.value, "ID")
    return tok

def t_CTE_FLOAT(tok):
    r'-?[0-9]+\.[0-9]+'
    tok.value = float(tok.value)
    return tok

def t_CTE_INT(tok):
    r'-?[0-9]+'
    tok.value = int(tok.value)
    return tok

def t_CTE_STRING(tok):
    r'\".*?\"'
    return tok

t_ignore = ' \t\r\n'

#Handler de errores
def t_error(tok):
    print(f"Error de token: '{tok.value[0]}'")
    tok.lexer.skip(1)

#Construcción del lexer
lexer = lex.lex()