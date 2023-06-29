# Ejercicios Datos Simples
# Day 1 - 30/05/2023


"""
Ejercicio 6
Escribir un programa que lea un entero positivo, introducido por el usuario y después muestre
en pantalla la suma de todos los enteros desde 1 hasta n..
La suma de los primeros enteros positivos puede ser calculada de la siguiente forma:
suma = n(n+1)/2
"""

print('\n *** EJERCICIO 6 ***')

n = int(input('Introduce un entero positivo: '))

# division entera 1
suma = int(n*(n+1)/2)

# division entera 2
suma = n*(n+1)//2

print('Suma de los primeros enteros positivos de 1 hasta ' +str(n) +': ' +str(suma))