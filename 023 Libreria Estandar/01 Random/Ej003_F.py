# Day 25 - 03/07/2023
# Modulo Random

'''
Ejercicio 3
Escribe una función que tome como parámetro una lista y devuelva un elemento
aleatorio de la lista.
'''

# SOLUCION PROFE

import random


def obtener_elemento_aleatorio(lista):
	return random.choice(lista)


nombres = ["Juan", "Maria", "Pedro", "Ana", "Luis"]
print("El elemento aleatorio es:", obtener_elemento_aleatorio(nombres))