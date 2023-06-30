# Day 24 - 30/06/2023
# Ejercicios Lambda


# Nivel básico
'''
Ejercicio 3
Escribe una función lambda que tome una lista de números como parámetro y devuelva
la lista ordenada de forma ascendente.
'''

listaNumeros = [9, 8, 7, 6, 5, 4, 3, 2, 1]

lambda lista: sorted(lista)
ordenar = lambda lista: sorted(lista)

print((lambda lista: sorted(lista))(listaNumeros))
print(ordenar(listaNumeros))