# Day 26 - 04/07/2023
# Ejercicios Librerias Estandar.docx
# Modulo Math

'''
Ejercicio 1
Escribe un programa que calcule el área de un círculo dado su radio.
'''

# SOLUCION PROFE

import math


def calcular_area_circulo(radio):
    area = math.pi * math.pow(radio, 2)
    return area


radio = 5

area_circulo = calcular_area_circulo(radio)
print(f"El área del círculo con radio {radio} es: {area_circulo}")