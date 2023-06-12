# Day 9 - 09/06/2023

############################
# Variable local
############################

resultado=15

def sumarLocal(n1, n2):
	# Variable local dentro de la función
	resultado = n1 + n2
	return resultado

# Variable global
resultado=15
valor = sumarLocal(1,2)

# Imprime el valor global (15)
print('El resultado es:',resultado)
# Imprime el valor devuelto por la funcion (3)
print('El valor es:',valor)


############################
# Variable global
############################

# Variable global
resultado=15
def sumarGlobal(n1, n2):
	# Indica que se utilizara la variable global resultado
	global resultado

	# estas modificando la de arriba
	resultado = n1 + n2

	# el return no hace falta
	return resultado

valor = sumarGlobal(1,2)

# Imprime el nuevo valor global (3)
print('El resultado es:', resultado)
# Imprime None ya que la funcion no devuelve ningun valor
print('El valor es:', valor)