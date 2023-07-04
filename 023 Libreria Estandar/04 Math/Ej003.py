# Day 26 - 04/07/2023
# Ejercicios Librerias Estandar.docx
# Modulo Math

'''
Ejercicio 3
Escribe un programa que convierta grados Celsius a grados Fahrenheit.
Fahrenheit = (Celsius*9/5)+32
'''

# SOLUCION PROFE


def convertir_celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


celsius = 30

fahrenheit = convertir_celsius_a_fahrenheit(celsius)
print(f"{celsius} grados Celsius equivale a {fahrenheit} grados Fahrenheit")