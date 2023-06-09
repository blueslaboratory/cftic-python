# 09/06/2023 - Day 9
# Ejercicios de Set

'''
Ejercicio 2
Escribe un programa que solicite al usuario ingresar dos conjuntos de números
separados por espacios y luego muestre la unión de ambos conjuntos.
'''

print('\n*** EJERCICIO 2 ***')

print('Conjunto de numeros 1 separado por espacios: ')
print('E.g. 5 6 7 8 9')
numeros1 = input('> ')
listaNumeros1 = numeros1.split()

print('Conjunto de numeros 2 separado por espacios: ')
print('E.g. 1 2 3 4 5 6')
numeros2 = input('> ')
listaNumeros2 = numeros2.split()

# Trabajando con Strings
# setNumeros1 = set(listaNumeros1)
# setNumeros2 = set(listaNumeros2)

# Trabajando con ints
setNumeros1 = set(list(map(int, listaNumeros1)))
setNumeros2 = set(list(map(int, listaNumeros2)))


union = setNumeros1.union(setNumeros2)


# Solo se puede ordenar una lista:
# 1. Pasamos el set a lista: list(union)
# 2. Ordenamos la lista: sorted(list(union))
# 3. Pasamos la lista a set: set(sorted(list(union)))
# 4. Da =, porque al meterlo en un set lo desordena
unionOrdenada = set(sorted(list(union)))


print('\nUnion conjuntos')
print(union)

print('\nUnion conjuntos ordenado (no ordena)')
print(unionOrdenada)

print('\nLista ordenada')
print(sorted(list(union)))




print('\n*** EJERCICIO 2 - SOLUCION PROFE ***')

conjunto1 = set(input("Ingresa el primer conjunto de números separados por espacios: ").split())
conjunto2 = set(input("Ingresa el segundo conjunto de números separados por espacios: ").split())
union = conjunto1.union(conjunto2)
print("Unión de conjuntos: ", union)