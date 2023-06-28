# Ejercicios de Bucles
# Day 6 - 06/06/2023

'''
Ejercicio 6
Escribir un programa que pida al usuario un número entero y muestre por pantalla
un triángulo rectángulo como el de más abajo, de altura el número introducido.

*
**
***
****
*****
'''

print('\n*** EJERCICIO 6 ***')

altura = int(input('Altura: '))
base = ''

print('\nTriangulo rectangulo de', altura, 'plantas de altura')
for i in range(1, altura+1):
	base += '*'
	print('Fila', i, ':\t', base)



print('\n*** EJERCICIO 6 - SOLUCION PROFE ***')

numero = int(input("Dame numero entero positivo: "))
cadena = "&"
for i in range(1,numero+1):
	print(cadena*i)