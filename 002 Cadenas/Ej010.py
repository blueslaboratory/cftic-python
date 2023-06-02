# Ejercicios de Cadenas
# Day 2 - 31/05/2023

'''
Ejercicio 10
Escribir un programa que pregunte por consola por los productos de una cesta de la
compra, separados por comas, y muestre por pantalla cada uno de los productos en una
línea distinta.
'''
print('\n *** EJERCICIO 10 ***')
cesta = input('Cesta (e.g. baguette,croisant,dinosaurus...): ')
cestaList = cesta.split(',')
for producto in cestaList:
	print('\t' +producto)

