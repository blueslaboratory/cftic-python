# Ejercicios de Diccionarios
# Day 7 - 07/06/2023

'''
Ejercicio 6
Escribir un programa que cree un diccionario vacío y lo vaya llenando con
información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo
electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo
dato debe imprimirse el contenido del diccionario.
'''

print('\n*** EJERCICIO 6 - CHATGPT ***')

# Diccionario vacio
persona = {}
continuar = True

# Solicitar informacion al usuario
while continuar:
	clave = input("Ingrese el nombre del dato (clave): ")
	valor = input("Ingrese el valor del dato (valor): ")

	# Almacenar el dato en el diccionario
	persona[clave] = valor

	# Imprimir el contenido del diccionario
	print(persona)

	# Preguntar al usuario si desea agregar más datos
	respuesta = input("\n¿Desea agregar mas datos? (s/n): ")

	# Salir del bucle si el usuario no desea agregar más datos
	if respuesta.lower() == "n":
		continuar = False
