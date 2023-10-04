# Ejercicios de Diccionarios
# Day 6 - 06/06/2023

'''
Ejercicio 2
Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y
lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre>
tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
'''

print('\n*** EJERCICIO 2 ***')

nombre = input('Nombre: ')
edad = input('Edad: ')
direccion = input('Direccion: ')
telefono = input('Telefono: ')


fichaPersona = {
	'nombre': nombre,
	'edad': edad,
	'direccion': direccion,
	'telefono': telefono
}


print(fichaPersona)
print(fichaPersona['nombre'], 'tiene', fichaPersona['edad'],
      'años, vive en', fichaPersona['direccion'],
      'y su numero de telefono es', fichaPersona['telefono'])