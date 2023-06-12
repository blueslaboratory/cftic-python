# Day 10 - 12/06/2023

'''
Ejercicio 2 Conversión de tipo de dato
Escribe una función llamada convertir_a_entero que reciba un valor y lo convierta
a entero. La función debe manejar la excepción en caso de que el valor no sea
numérico y devolver un mensaje de error adecuado.
'''

print('\n*** EJERCICIO 2 ***')

def convertirEntero(stringNumber):
	try:
		entero = int(stringNumber)
		return entero
	except ValueError:
		return 'ValueError - Valor no numerico'


stringNumber = input('Numero entero: ')

print('Resultado:', convertirEntero(stringNumber))