# Day 11 - 13/06/2023

'''
Ejercicio 5 Acceso a diccionarios
Escribe una función llamada obtener_valor que reciba un diccionario y una clave,
y devuelva el valor correspondiente. La función debe manejar la excepción en
caso de que la clave no exista y devolver un mensaje de error adecuado.
'''

print('\n*** EJERCICIO 5 - SOLUCION PROFE ***')

def obtener_valor(diccionario, clave):
	try:
		valor = diccionario[clave]
		return valor
	except KeyError:
		return "KeyError: Clave no encontrada"


# Ejemplo de uso diccionario = {'a': 1, 'b': 2, 'c': 3}
diccionario = {'a': 1, 'b': 2, 'c': 3}
clave = 'd'
resultado = obtener_valor(diccionario, clave)
print(resultado)