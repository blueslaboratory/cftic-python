# 09/06/2023 - Day 9
# Ejercicios de Set

'''
Ejercicio 1
Escribe un programa que solicite al usuario ingresar una lista de números
separados por espacios y luego muestre una lista sin elementos duplicados.
'''

print('\n*** EJERCICIO 1 ***')

print('Lista de numeros separados por espacios')
print('E.g. 1 2 3 3 7 7 9 9 13 14')
listStrNumeros = input('> ').split()

# Esto te devolveria una lista de numeros en formato string:
# listNumeros = numeros.split()

# convertir strings de una lista en ints
mapaNumeros = map(int, listStrNumeros)
listIntNumeros = list(mapaNumeros)

print('\nLista de numeros con duplicados')
print(listIntNumeros)

# Los conjuntos no tienen duplicados, si metes un valor duplicado pasa de ti
setNumeros = set(listIntNumeros)
listSinDuplicados = list(setNumeros)

print('\nLista de numeros sin duplicados')
print(listSinDuplicados)



print('\n*** EJERCICIO 1 - SOLUCION PROFE ***')

numeros = input("Ingresa una lista de números separados por espacios: ")
lista_numeros = numeros.split()
conjunto_numeros = set(lista_numeros)
lista_sin_duplicados = list(conjunto_numeros)
print("Lista sin elementos duplicados:", lista_sin_duplicados)