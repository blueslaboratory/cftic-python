# Day 11 - 13/06/2023

'''
Ejercicio 8  Cálculo de raíz cuadrada
Escribe una función llamada raiz_cuadrada que reciba un número y calcule su
raíz cuadrada. La función debe manejar la excepción en caso de que se
proporcione un número negativo y devolver un mensaje de error adecuado.
'''

print('\n*** EJERCICIO 7 - SOLUCION PROFE ***')

import math
def raiz_cuadrada(numero):
	try:
		resultado = math.sqrt(numero)
		return resultado
	except ValueError:
		return "ValueError - no se puede calcular la raíz cuadrada de un número negativo"


# Ejemplo de uso numero = -9
numero = -9
resultado = raiz_cuadrada(numero)

print(resultado)