# Ejercicios de Listas y Tuplas
# Day 4 - 02/06/2023

'''
Ejercicio 5
Escribir un programa que almacene en una lista los números del 1 al 10 y los
muestre por pantalla en orden inverso separados por comas.
'''

print('\n*** EJERCICIO 5 ***')

numeros = []

# Cargar la lista con los numeros
# [1,10]
for i in range(1,11):
	numeros.append(i)

# Imprimir en inverso
print(numeros[::-1])

# Solucion
for i in range(1,11):
	print(numeros[-i], end=',')