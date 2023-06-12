# Day 10 - 12/06/2023

'''
Ejercicio 3 Acceso a elementos de una lista
Escribe una función llamada obtener_elemento que reciba una lista y un índice y
devuelva el elemento correspondiente. La función debe manejar la excepción en
caso de que el índice esté fuera del rango y devolver un mensaje de error adecuado.
'''

print('\n*** EJERCICIO 3 ***')

def obtenerElemento(lista, indice):
	try:
		elemento = lista[indice]
		return elemento
	except ValueError:
		return 'IndexError - Fuera de rango'


# lista = [0,1,2,3,4,5,6,7,8,9,10]

print('Introduzca una lista (e.g. 0,1,2,3,4,5,6,7,8,9,10)')
lista = input('> ').split(',')
indice = int(input('Indice: '))

print('Resultado:', obtenerElemento(lista, indice))