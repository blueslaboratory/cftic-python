# Day 11 - 13/06/2023

'''
Ejercicio 7 Extracción de datos de una lista
Escribe una función llamada extraer_elemento que reciba una lista y un índice,
y devuelva el elemento correspondiente. La función debe manejar la excepción
en caso de que el índice no sea válido y devolver un mensaje de error adecuado.
'''

print('\n*** EJERCICIO 7 - SOLUCION PROFE ***')

def extraer_elemento(lista, indice):
	try:
		elemento = lista.pop(indice)
		return elemento
	except IndexError:
		return "IndexError - indice invalido"


# Ejemplo de uso lista = [1, 2, 3, 4, 5]
lista = [1, 2, 3, 4, 5]
indice = 10
resultado = extraer_elemento(lista, indice)

print(resultado)