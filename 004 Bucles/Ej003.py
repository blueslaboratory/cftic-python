# Ejercicios de Bucles
# Day 6 - 06/06/2023

'''
Ejercicio 3
Escribir un programa que pida al usuario un número entero positivo y muestre por
pantalla todos los números impares desde 1 hasta ese número separados por comas.
'''

print('*** EJERCICIO 3 ***')

entero = int(input('Entero: '))
counter = 1


while (counter <= entero):

	if(counter%2 != 0):
		print(counter)

	counter += 1