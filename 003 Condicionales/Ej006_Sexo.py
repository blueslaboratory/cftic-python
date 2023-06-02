# Ejercicios de Condicionales
# Day 4 - 02/06/2023


'''
Ejercicio 6
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el
nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los
hombres con un nombre posterior a la N y el grupo B por el resto.
Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla
el grupo que le corresponde.
'''

print('\n*** EJERCICIO 6 ***')

sexo = input('Sexo (M/F): ')
nombre = input('Nombre: ')

if(sexo.lower() == 'f'):
	if(nombre[0].upper()<='M'):
		print('Grupo A: mujer')
	else:
		print('Grupo B: mujer')
elif(sexo.lower() == 'm'):
	if (nombre[0].upper() >= 'N'):
		print('Grupo A: hombre')
	else:
		print('Grupo B: hombre')
else:
	print('Genero no reconocido')


