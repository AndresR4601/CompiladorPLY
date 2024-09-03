# Importamos las estructuras de memoria y el main para que corra el lexer y parser
from main import lexer, parser
from sintactico import cuadruplo, listMGI, listMGF, listMTI, listMTF, listMTB, listMCI, listMCF, listMCS

# Función de switch para realizar la operaciones o saltos por quadruplo de entrada
def switch_Cuadruplo(caso):
    # Variable para tener control del indice de los Saltos entre cuadruplos
    global apuntador

    if caso[1] == 1:
        resultado = getMemoria(caso[2]) + getMemoria(caso[3])
        setMemoria(caso[4], resultado)
    elif caso[1] == 2:
        resultado = getMemoria(caso[2]) - getMemoria(caso[3])
        setMemoria(caso[4], resultado)
    elif caso[1] == 3:
        resultado = getMemoria(caso[2]) * getMemoria(caso[3])
        setMemoria(caso[4], resultado)
    elif caso[1] == 4:
        resultado = getMemoria(caso[2]) / getMemoria(caso[3])
        setMemoria(caso[4], resultado)
    elif caso[1] == 5:
        resultado = getMemoria(caso[2]) > getMemoria(caso[3])
        setMemoria(caso[4], resultado)
    elif caso[1] == 6:
        resultado = getMemoria(caso[2]) < getMemoria(caso[3])
        setMemoria(caso[4], resultado)
    elif caso[1] == 7:
        resultado = getMemoria(caso[2]) != getMemoria(caso[3])
        setMemoria(caso[4], resultado)
    elif caso[1] == 8:
        valor = getMemoria(caso[2])
        setMemoria(caso[4], valor)
    elif caso[1] == 9:
        resultado = getMemoria(caso[4])
        print(resultado) 
    elif caso[1] == 10:
        aux = getMemoria(caso[2])
        if aux==False:
            apuntador = caso[4]
    elif caso[1] == 11:
        aux = getMemoria(caso[2])
        if aux==True:
            apuntador = caso[4]
    elif caso[1] == 12:
            apuntador = caso[4]
    else:
        return "Error"
    
# Función para traer de las estrucutras de memoria los datos correspondientes
def getMemoria(memoria):
    if memoria >= 1000 and memoria < 1099:
        aux = memoria - 1000
        valor = listMGI[aux]
        return valor
    elif memoria >= 1100 and memoria < 1199:
        aux = memoria - 1100
        valor = listMGF[aux]
        return valor
    elif memoria >= 2000 and memoria < 2099:
        aux = memoria - 2000
        valor = listMTI[aux]
        return valor
    elif memoria >= 2100 and memoria < 2199:
        aux = memoria - 2100
        valor = listMTF[aux]
        return valor
    elif memoria >= 2200 and memoria < 2299:
        aux = memoria - 2200
        valor = listMTB[aux]
        return valor
    elif memoria >= 3000 and memoria < 3099:
        aux = memoria - 3000
        valor = listMCI[aux]
        return valor
    elif memoria >= 3100 and memoria < 3199:
        aux = memoria - 3100
        valor = listMCF[aux]
        return valor
    elif memoria >= 3200 and memoria < 3299:
        aux = memoria - 3200
        valor = listMCS[aux]
        return valor[1:-1]
    else:
        print("Error en memoria")

# Función para actualizar en las estructuras de memoria las variables temporales y globales
def setMemoria(memoria, valor):
    if memoria >= 1000 and memoria < 1099:
        listMGI[memoria-1000] = valor
    elif memoria >= 1100 and memoria < 1199:
        listMGF[memoria-1100] = valor
    elif memoria >= 2000 and memoria < 2099:
        listMTI[memoria-2000] = valor
    elif memoria >= 2100 and memoria < 2199:
        listMTF[memoria-2100] = valor
    elif memoria >= 2200 and memoria < 2299:
        listMTB[memoria-2200] = valor
    else:
        print("Error en set memoria")

apuntador = 0
#print('Cuádruplos \n')
#cuadruplo.printC()
#print('-------------------------------')
#print('Resultado maquina virtual \n')
# While loop para recorrer todos los cuadruplos hasta que el indice sea mayor al número de cuadruplos
while apuntador < len(cuadruplo.cuadruplo):
    caso = cuadruplo.cuadruplo[apuntador]
    apuntador += 1
    switch_Cuadruplo(caso)