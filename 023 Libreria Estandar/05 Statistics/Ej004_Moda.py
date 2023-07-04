# Day 26 - 04/07/2023
# Ejercicios Librerias Estandar.docx
# Modulo Statistics

'''
Ejercicio 4
Escribe un programa que calcule la moda de una lista de números.
'''

# SOLUCION PROFE

import statistics


def calcular_moda(datos):
    moda = statistics.mode(datos)
    return moda


numeros = [2, 3, 2, 4, 1, 5, 2, 6, 2]

moda = calcular_moda(numeros)
print(f"La moda de la lista {numeros} es: {moda}")