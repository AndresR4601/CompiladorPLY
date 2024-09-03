#Definición de cubo semantico
cubo_semantico = {
    'int' : {
        'int' : {
            '+' : 'int',
            '-' : 'int',
            '*' : 'int',
            '/' : 'float',
            '<' : 'bool',
            '>' : 'bool',
            '=' : 'int',
            '!=' : 'bool'
        },
        'float' : {
            '+' : 'float',
            '-' : 'float',
            '*' : 'float',
            '/' : 'float',
            '<' : 'bool',
            '>' : 'bool',
            '=' : 'float',
            '!=' : 'bool'
        }, 
        'bool' : {
            '=' : 'error'
        }
    }, 
    'float' : {
        'int' : {
            '+' : 'float',
            '-' : 'float',
            '*' : 'float',
            '/' : 'float',
            '<' : 'bool',
            '>' : 'bool',
            '=' : 'error',
            '!=' : 'bool'
        },
        'float' : {
            '+' : 'float',
            '-' : 'float',
            '*' : 'float',
            '/' : 'float',
            '<' : 'bool',
            '>' : 'bool',
            '=' : 'float',
            '!=' : 'bool'
        }, 
        'bool' : {
            '=' : 'error'
        }
    }, 
    'bool' : {
        'int' : {
            '=' : 'error'
        },
        'float' : {
            '=' : 'error'
        }
    }
}