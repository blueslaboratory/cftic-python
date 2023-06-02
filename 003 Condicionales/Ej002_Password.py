# Ejercicios de Condicionales
# Day 4 - 02/06/2023

'''
Ejercicio 2
Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña e imprima por pantalla si la contraseña
introducida por el usuario coincide con la guardada en la variable sin tener en
cuenta mayúsculas y minúsculas.
'''

print('\n*** EJERCICIO 2 ***')

flag = False
pw = 'qwerty'
pwUser = input('Password: ')


if(pw == pwUser.lower()):
	flag = True

if(flag):
	print('Las passwords coinciden')


