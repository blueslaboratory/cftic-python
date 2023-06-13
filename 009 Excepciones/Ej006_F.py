# Day 11 - 13/06/2023

'''
Ejercicio 6  Conversión de cadena a número
Escribe una función llamada convertir_a_numero que reciba una cadena y la
convierta a un número flotante. La función debe manejar la excepción en
caso de que la cadena no sea numérica y devolver un mensaje de error adecuado.
'''

print('\n*** EJERCICIO 6 - SOLUCION PROFE ***')

def convertir_a_numero(cadena):
	try:
		numero = float(cadena)
		return numero
	except ValueError:
		return "ValueError: cadena no numérica"


# Ejemplo de uso cadena = "3.14"
cadena = 'mesopotamia'
# cadena = "3.14"
resultado = convertir_a_numero(cadena)
print(resultado)