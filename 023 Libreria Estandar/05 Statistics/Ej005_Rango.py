# Day 26 - 04/07/2023
# Ejercicios Librerias Estandar.docx
# Modulo Statistics

'''
Ejercicio 5:
Escribe un programa que calcule el rango de una lista de números.
'''

# SOLUCION PROFE

import statistics


def calcular_rango(datos):
    rango = max(datos) - min(datos)
    return rango


numeros = [5, 3, 8, 1, 9, 2]

rango = calcular_rango(numeros)
print(f"El rango de la lista {numeros} es: {rango}")