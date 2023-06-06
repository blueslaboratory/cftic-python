# Ejercicios de Bucles
# Day 6 - 06/06/2023

'''
Ejercicio 1
Escribir un programa que pida al usuario una palabra y la muestre por pantalla
10 veces.
'''

print('*** EJERCICIO 1 ***')

palabra = input('Palabra: ')

repetir = 1

while (repetir <= 10):
	print('Repetir -', repetir,
	      '\tPalabra:', palabra)
	repetir += 1