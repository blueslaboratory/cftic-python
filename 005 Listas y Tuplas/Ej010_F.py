# Ejercicios de Listas y Tuplas
# Day 4 - 02/06/2023

'''
Ejercicio 10
Escribir un programa que almacene en una lista los siguientes precios:
50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.
'''


print('\n*** EJERCICIO 10 - SOLUCION PROFE ***')

precios = [50, 75, 46, 22, 80, 65, 8]
precios.sort()

print("El precio menor es: "+str(precios[0]))
print("El precio mayor es: " + str(precios[len(precios)-1]))