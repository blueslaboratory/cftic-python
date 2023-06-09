# 09/06/2023 - Day 9
# Ejercicios de Set

'''
Ejercicio 10
Escribe un programa que solicite al usuario ingresar una lista de números
separados por espacios y luego muestre la cantidad de elementos únicos en el
conjunto.
'''

print('\n*** EJERCICIO 10***')


print('Conjunto de numeros separado por espacios: ')
print('E.g. 1 2 3 3 7 7 9 9 13 14')
numeros = input('> ')

listaNumeros = numeros.split()
setNumeros = set(listaNumeros)

print('\nNº de elementos unicos:', len(setNumeros))