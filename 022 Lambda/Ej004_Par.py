# Day 24 - 30/06/2023
# Ejercicios Lambda


# Nivel básico
'''
Ejercicio 4
Escribe una función lambda que reciba un número entero como parámetro y devuelva
True si el número es par, y False en caso contrario.
'''

n = 14

lambda num: num % 2 == 0
par = lambda num: num % 2 == 0

print(f'{n} es par:', (lambda num: num % 2 == 0)(n))
print(f'{n} es par:', par(n))