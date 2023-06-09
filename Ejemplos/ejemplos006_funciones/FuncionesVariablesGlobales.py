# Day 9 - 09/06/2023

############################
# Variable local
############################
def sumarLocal(n1, n2):
    resultado = n1 + n2
    return resultado

resultado=15
valor = sumarLocal(1,2)

print('El resultado es:',resultado)
print('El valor es:',valor)


############################
# Variable global
############################

resultado=15
def sumarGlobal(n1, n2):
    global resultado

	# estas modificando la de arriba
    resultado = n1 + n2

	# el return no hace falta
    return resultado

valor = sumarGlobal(1,2)

print('El resultado es:', resultado)
print('El valor es:', valor)