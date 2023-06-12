# Day 8 - 08/06/2023

'''
Ejercicio 1  División segura
Escribe una función llamada dividir que reciba dos números y realice su división.
La función debe manejar la excepción en caso de que se proporcione un divisor
igual a cero y devolver un mensaje de error adecuado.
'''

print('\n*** EJERCICIO 1 ***')

def dividir(n1, n2):
	try:
		return n1/n2
	except ZeroDivisionError:
		return 'ZeroDivisionError: Se ha intentado dividir por 0'


n1 = int(input('Dame n1: '))
n2 = int(input('Dame n2: '))

print('Resultado:', dividir(n1, n2))