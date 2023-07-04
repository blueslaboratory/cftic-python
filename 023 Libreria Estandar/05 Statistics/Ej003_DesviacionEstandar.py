# Day 26 - 04/07/2023
# Ejercicios Librerias Estandar.docx
# Modulo Statistics

'''
Ejercicio 3
Escribe un programa que calcule la desviación estándar de una lista de números.
'''

# SOLUCION PROFE

import statistics


def calcular_desviacion_estandar(datos):
    desviacion_estandar = statistics.stdev(datos)
    return desviacion_estandar


numeros = [2, 4, 6, 8, 10]

desviacion = calcular_desviacion_estandar(numeros)
print(f"La desviación estándar de la lista {numeros} es: {desviacion}")