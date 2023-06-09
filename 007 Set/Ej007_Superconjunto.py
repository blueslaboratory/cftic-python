# 09/06/2023 - Day 9
# Ejercicios de Set

'''
Ejercicio 7
Escribe un programa que solicite al usuario ingresar dos conjuntos de números
separados por espacios y luego determine si el primer conjunto es un superconjunto
del segundo conjunto.

P.D.
Si el primer conjunto es un superconjunto del segundo conjunto, significa que todos
los elementos del segundo conjunto están presentes en el primer conjunto, pero el
primer conjunto puede contener elementos adicionales.
'''


print('\n*** EJERCICIO 7 ***')

print('Conjunto de numeros 1 separado por espacios: ')
print('E.g. 1 2 3 4')
numeros1 = input('> ')
listaNumeros1 = numeros1.split()

print('Conjunto de numeros 2 separado por espacios: ')
print('E.g. 1 2')
numeros2 = input('> ')
listaNumeros2 = numeros2.split()

setNumeros1 = set(listaNumeros1)
setNumeros2 = set(listaNumeros2)

isSuperSet = setNumeros1.issuperset(setNumeros2)

print()
print('setNumeros1 es superset de setNumeros2:', isSuperSet)