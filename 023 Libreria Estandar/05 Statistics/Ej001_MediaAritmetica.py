# Day 26 - 04/07/2023
# Ejercicios Librerias Estandar.docx
# Modulo Statistics

'''
Ejercicio 1
Escribe un programa que calcule la media aritmética de una lista de números.
'''

# SOLUCION PROFE

import statistics


def calcular_media(datos):
    media = statistics.mean(datos)
    return media


numeros = [2, 4, 6, 8, 10]

media = calcular_media(numeros)
print(f"La media de la lista {numeros} es: {media}")