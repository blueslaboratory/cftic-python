# Ejercicios de Bucles
# Day 7 - 07/06/2023


'''
Ejercicio 11
Escribir un programa que pida al usuario una palabra y luego muestre por pantalla
una a una las letras de la palabra introducida empezando por la última.
'''

print('\n*** EJERCICIO 11 - SOLUCION PROFE ***')


palabra = input("Dame palabra: ")

for i in range(len(palabra)-1, -1, -1):
    print(palabra[i])
