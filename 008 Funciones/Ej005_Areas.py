# 12/06/2023 - Day 10
# Ejercicios de Funciones

'''
Ejercicio 5
Escribir una función que calcule el área de un círculo y otra que calcule el
volumen de un cilindro usando la primera función.
'''

import math

print('\n*** EJERCICIO 5 ***')

def areaCirculo(radio):
	pi = math.pi
	# print('pi:', pi)

	return pi*(radio**2)

def volCilindro(radio, altura):
	return areaCirculo(radio)*altura


radio = float(input('Radio (cm): '))
altura = float(input('Altura (cm): '))


print()
print('Area circulo (cm**2):', areaCirculo(radio))
print('Volumen cilindro (cm**2):', volCilindro(radio, altura))