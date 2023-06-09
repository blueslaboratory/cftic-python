# 09/06/2023 - Day 9
# Ejercicios de Set

'''
Ejercicio 4
Escribe un programa que solicite al usuario ingresar dos conjuntos de números
separados por espacios y luego muestre los números que están en el primer conjunto
pero no en el segundo conjunto.
'''

print('\n*** EJERCICIO 4 ***')

print('Conjunto de numeros 1 separado por espacios: ')
print('E.g. 1 2 3 4')
numeros1 = input('> ')
listaNumeros1 = numeros1.split()

print('Conjunto de numeros 2 separado por espacios: ')
print('E.g. 2 3 4')
numeros2 = input('> ')
listaNumeros2 = numeros2.split()

setNumeros1 = set(listaNumeros1)
setNumeros2 = set(listaNumeros2)

setDifference = setNumeros1.difference(setNumeros2)

print('\nDiferencias entre los sets:')
print(setDifference)