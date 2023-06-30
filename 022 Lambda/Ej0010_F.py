# Day 24 - 30/06/2023
# Ejercicios Lambda


# Nivel intermedio
'''
Ejercicio 10
Escribe una función lambda que tome dos listas como parámetros y devuelva
una lista con los elementos comunes entre ambas listas.
'''


l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [2, 4, 6, 8]


lambda lista1, lista2: list(filter(lambda x: x in lista1, lista2))
elementosComunes = lambda lista1, lista2: list(filter(lambda x: x in lista1, lista2))


print((lambda lista1, lista2: list(filter(lambda x: x in lista1, lista2)))(l1, l2))
print(elementosComunes(l1, l2))