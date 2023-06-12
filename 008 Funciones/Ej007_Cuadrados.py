# 12/06/2023 - Day 10
# Ejercicios de Funciones

'''
Ejercicio 7
Escribir una función que reciba una muestra de números en una lista y devuelva
otra lista con sus cuadrados.
'''


print('\n*** EJERCICIO 7 ***')

def cuadrados(listaNumeros):

	cuadrados = []

	for n in listaNumeros:
		cuadrados.append(float(n)**2)

	return cuadrados


def cuadradosParametros(*listaNumeros):

	cuadrados = []

	for n in listaNumeros:
		cuadrados.append(n ** 2)

	return cuadrados



print('Lista de numeros (e.g. 3,3,4,2,5,1,6,0)')
listaNumeros = list(input('> ').split(','))

print('Lista funcion cuadrados:', cuadrados(listaNumeros))
print('Lista cuadradosParametros:', cuadradosParametros(3,3,4,2,5,1,6,0))

