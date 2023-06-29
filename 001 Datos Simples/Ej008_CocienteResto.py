# Ejercicios Datos Simples
# Day 1 - 30/05/2023

"""
Ejercicio 8
Escribir un programa que pida al usuario dos números enteros y muestre por pantalla
“La división de <n> entre <m> da un cociente <c> y un resto <r>” donde <n> y <m> son
los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división
entera respectivamente.
"""

print('\n *** EJERCICIO 8 ***')

n1 = int(input('Numero entero 1: '))
n2 = int(input('Numero entero 2: '))

cociente = int(n1/n2)
resto = n1%n2

print('La division de ' +str(n1) +' entre ' +str(n2)
      +' da un cociente ' +str(cociente)
      +' y un resto de ' +str(resto))