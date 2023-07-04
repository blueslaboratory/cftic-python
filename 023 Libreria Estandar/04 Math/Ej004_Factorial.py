# Day 26 - 04/07/2023
# Ejercicios Librerias Estandar.docx
# Modulo Math

'''
Ejercicio 4
Escribe un programa que calcule el factorial de un número dado.
'''

# SOLUCION PROFE


import math


def calcular_factorial(numero):
    factorial = math.factorial(numero)
    return factorial


numero = 5

factorial = calcular_factorial(numero)
print(f"El factorial de {numero} es: {factorial}")