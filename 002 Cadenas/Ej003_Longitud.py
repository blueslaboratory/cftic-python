# Ejercicios de Cadenas
# Day 2 - 31/05/2023

'''
Ejercicio 3
Escribir un programa que pregunte el nombre del usuario en la consola y después de
que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras,
donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras
que tiene el nombre.
'''

print('\n *** EJERCICIO 3 ***')

nombre = input('Nombre: ')

print('Nombre en MAYUS: ' +nombre.upper())

# Cuando concatenamos hay que poner str(): solo se pueden concatenar strings
print('Letras concatenar: ' +str(len(nombre)-1))
print('Letras con coma:', len(nombre)-1)