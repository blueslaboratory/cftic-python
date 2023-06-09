# 09/06/2023 - Day 9
# Ejercicios de Funciones

'''
Ejercicio 2
Escribir una función a la que se le pase una cadena <nombre> y muestre por
pantalla el saludo ¡hola <nombre>!.
'''

print('\n*** EJERCICIO 2 ***')

def hola(nombre):
	print('¡Hola ', nombre, '!', sep='')

nombre = input('Nombre: ')
hola(nombre)