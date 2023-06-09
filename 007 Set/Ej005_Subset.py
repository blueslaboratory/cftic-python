# 09/06/2023 - Day 9
# Ejercicios de Set

'''
Ejercicio 5
Escribe un programa que solicite al usuario ingresar dos conjuntos de números
separados por espacios y luego determine si el primer conjunto es un subconjunto
del segundo conjunto.
'''

print('\n*** EJERCICIO 5 ***')

print('Conjunto de numeros 1 separado por espacios: ')
print('E.g. 1 2')
numeros1 = input('> ')
listaNumeros1 = numeros1.split()

print('Conjunto de numeros 2 separado por espacios: ')
print('E.g. 1 2 3 4')
numeros2 = input('> ')
listaNumeros2 = numeros2.split()

setNumeros1 = set(listaNumeros1)
setNumeros2 = set(listaNumeros2)

isSubset1 = setNumeros1.issubset(setNumeros2)
isSubset2 = setNumeros2.issubset(setNumeros1)

print()
print('setNumeros1 es subset de setNumeros2:', isSubset1)
print('setNumeros2 es subset de setNumeros1:', isSubset2)
