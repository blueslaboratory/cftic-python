# Day 26 - 04/07/2023
# Ejercicios Librerias Estandar.docx
# Modulo Math

'''
Ejercicio 5
Escribe un programa que calcule la hipotenusa de un triángulo rectángulo
dados los catetos.
'''

# SOLUCION PROFE


import math


def calcular_hipotenusa(cateto1, cateto2):
    hipotenusa = math.sqrt(math.pow(cateto1, 2) + math.pow(cateto2, 2))
    return hipotenusa


cateto1 = 3
cateto2 = 4

hipotenusa = calcular_hipotenusa(cateto1, cateto2)
print(f"La hipotenusa del triángulo rectángulo con catetos {cateto1} y {cateto2} es: {hipotenusa}")