# Ejercicios de Condicionales
# Day 4 - 02/06/2023

'''
Ejercicio 3
Escribir un programa que pida al usuario dos números y muestre por pantalla su división.
Si el divisor es cero el programa debe mostrar un error.
'''

print('\n*** EJERCICIO 3 ***')

n1 = float(input('Numero 1: '))
n2 = float(input('Numero 2: '))

if (n2 == 0):
	print('Error: divisor 0')
else:
	print('Resultado:', str(n1/n2))