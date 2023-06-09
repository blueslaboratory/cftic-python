# 09/06/2023 - Day 9
# Ejercicios de Set

'''
Ejercicio 3
Escribe un programa que solicite al usuario ingresar dos conjuntos de números
separados por espacios y luego muestre los números que están presentes en ambos
conjuntos.
'''

print('\n*** EJERCICIO 3 ***')

print('Conjunto de numeros 1 separado por espacios: ')
print('E.g. 3 4 5 6')
numeros1 = input('> ')
listaNumeros1 = numeros1.split()

print('Conjunto de numeros 2 separado por espacios: ')
print('E.g. 1 2 3 4 5 6')
numeros2 = input('> ')
listaNumeros2 = numeros2.split()

setNumeros1 = set(listaNumeros1)
setNumeros2 = set(listaNumeros2)

setIntersect = setNumeros1.intersection(setNumeros2)

print('\nInterseccion de los sets:')
print(setIntersect)