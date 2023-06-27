# Ejercicios de Cadenas
# Day 2 - 31/05/2023

'''
Ejercicio 2
Escribir un programa que pregunte el nombre completo del usuario en la consola y
después muestre por pantalla el nombre completo del usuario tres veces, una con
todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con
la primera letra del nombre y de los apellidos en mayúscula. El usuario puede
introducir su nombre combinando mayúsculas y minúsculas como quiera.
'''

print('\n *** EJERCICIO 2 ***')

nombre = input('Nombre completo: ')

print('Nombre en minusculas: ')
print(nombre.lower())
print('Nombre en mayusculas: ')
print(nombre.upper())
print('Nombre con iniciales en mayusculas: ')
print(nombre.title())

# En una linea
print('\nEn una linea: ')
print(nombre.lower(), nombre.upper(), nombre.title(), sep='\n')

