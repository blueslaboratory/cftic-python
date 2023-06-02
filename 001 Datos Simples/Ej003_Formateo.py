# Ejercicios Datos Simples
# Day 1 - 30/05/2023

"""
Ejercicio 3
Escribir un programa que pregunte el nombre del usuario en la consola
y después de que el usuario lo introduzca muestre por pantalla la cadena
¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.
"""

print('\n *** EJERCICIO 3 ***')
nombre = input('Introduce tu nombre: ')
print('¡Hola ' +nombre +'!')

# Varias soluciones
print('¡Hola ', nombre, '!', sep='')
print('¡Hola', nombre, end='!\n')
print(f'¡Hola {nombre}!')
print('¡Hola %s!' % nombre)
print('¡Hola {0}!'.format(nombre))


