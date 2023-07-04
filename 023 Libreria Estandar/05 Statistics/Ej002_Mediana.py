# Day 26 - 04/07/2023
# Ejercicios Librerias Estandar.docx
# Modulo Statistics

'''
Ejercicio 2
Escribe un programa que calcule la mediana de una lista de números.
'''

# SOLUCION PROFE

import statistics


def calcular_mediana(datos):
    mediana = statistics.median(datos)
    return mediana


numeros = [3, 1, 4, 1, 5, 9, 2]

mediana = calcular_mediana(numeros)
print(f"La mediana de la lista {numeros} es: {mediana}")