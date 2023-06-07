# Ejercicios de Listas y Tuplas
# Day 4 - 02/06/2023

'''
Ejercicio 11
Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas
y muestre por pantalla su producto escalar.
'''

print('\n*** EJERCICIO 10 - SOLUCION PROFE ***')

vector1 = [1, 2, 3]
vector2 = [-1, 0, 2]
producto = 0

for i in range(len(vector1)):
    producto += vector1[i]*vector2[i]

print("El producto escalar es: "+str(producto))