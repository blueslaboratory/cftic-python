# Ejercicios Datos Simples
# Day 1 - 30/05/2023

"""
Ejercicio 9
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y
el número de años, y muestre por pantalla el capital obtenido en la inversión.

Capital final = Capital*(1 + Tasa de interés/100)^Tiempo
"""

print('\n *** EJERCICIO 9 ***')
cantidad = float(input('Cantidad a invertir: '))
interes = float(input('Interes anual (%): '))
years = int(input('Años de inversion: '))

capital = cantidad*(1+interes/100)**years

print('El capital obtenido en la inversion es: ', capital)


