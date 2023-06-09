# 09/06/2023 - Day 9
# Ejercicios de Set

'''
Ejercicio 9
Escribe un programa que solicite al usuario ingresar dos conjuntos de números
separados por espacios y luego determine si los conjuntos son disjuntos, es decir,
si no tienen elementos en común.
'''

print('\n*** EJERCICIO 9***')


print('Conjunto de numeros 1 separado por espacios: ')
print('E.g. 1 2 3 4')
numeros1 = input('> ')
listaNumeros1 = numeros1.split()

print('Conjunto de numeros 2 separado por espacios: ')
print('E.g. 5 6 7')
numeros2 = input('> ')
listaNumeros2 = numeros2.split()

setNumeros1 = set(listaNumeros1)
setNumeros2 = set(listaNumeros2)

isSetsDisjoints = setNumeros1.isdisjoint(setNumeros2)

print()
print('setNumeros1 y setNumeros2 son disjuntos:', isSetsDisjoints)