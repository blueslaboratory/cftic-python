# Day 24 - 30/06/2023
# Ejercicios Lambda


# Nivel intermedio
'''
Ejercicio 9
Escribe una función lambda que tome una lista de números como parámetro y
devuelva el producto de todos los números en la lista.(Es necesario importar
la función reduce del módulo functools para utilizarla).
'''

from functools import reduce

listaNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]


lambda numeros: reduce(lambda x, y: x * y, numeros)
productoNumeros = lambda numeros: reduce(lambda x, y: x * y, numeros)


print((lambda numeros: reduce(lambda x, y: x * y, numeros))(listaNumeros))
print(productoNumeros(listaNumeros))