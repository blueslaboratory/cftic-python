# Ejercicios de Bucles
# Day 6 - 06/06/2023


'''
Ejercicio 8
Escribir un programa que pida al usuario un número entero y muestre por pantalla
un triángulo rectángulo como el de más abajo.

1
3 1
5 3 1
7 5 3 1
9 7 5 3 1
'''

print('*** EJERCICIO 8 ***')

numero = int(input('Numero entero: '))
base = ''

print('\nTriangulo rectangulo')
for i in range(1, altura+1):
	base += '*'
	print('Fila', i, ':\t', base)