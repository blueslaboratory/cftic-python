# 09/06/2023 - Day 9
# Ejercicios de Set

'''
Ejercicio 8
Escribe un programa que solicite al usuario ingresar un conjunto de números
separados por espacios y un número objetivo, y luego elimine el número objetivo
del conjunto.
'''

print('\n*** EJERCICIO 8 ***')

print('Conjunto de numeros separado por espacios: ')
print('E.g. 1 2 3 4')
numeros = input('> ')
listaNumeros = numeros.split()


numero = input('Numero a eliminar: ')

setNumeros = set(listaNumeros)
setActualizado = setNumeros.copy()

setActualizado.discard(numero)

print()
print('Set original:', setNumeros)
print('Set actualizado: ', setActualizado)