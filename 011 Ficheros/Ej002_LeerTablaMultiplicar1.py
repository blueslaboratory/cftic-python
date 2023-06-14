# Day 12 - 14/06/2023
# Ejercicios de Ficheros


'''
Ejercicio 2
Escribir una función que pida un número entero entre 1 y 10, lea el fichero 
tabla-n.txt con la tabla de multiplicar de ese número, done n es el número 
introducido, y la muestre por pantalla. Si el fichero no existe debe 
mostrar un mensaje por pantalla informando de ello.
'''



print('\n*** EJERCICIO 2 - CHATGPT & MODS ***')

def pedir_numero():
	while True:
		try:
			numero = int(input('Numero entero [1,10]: '))
			if (numero >= 1 or numero <= 10):
				return numero
			else:
				print('Numero fuera del rango [1,10]')
		except ValueError:
			print('ValueError - caracteres no validos')


def mostrar_tabla_multiplicar():

	# Pedir al usuario un número entero entre 1 y 10
	numero = pedir_numero()

	# Leer el archivo tabla-n.txt y mostrar la tabla de multiplicar
	nombre_fichero = f"tabla-{numero}.txt"

	try:
		# Lo hacemos con with para ahorrarnos el close()
		with open(nombre_fichero, 'r') as fichero:
			contenido = fichero.read()
			print(f"Tabla de multiplicar del número {numero}:\n{contenido}")
	except FileNotFoundError:
		print(f"El archivo '{nombre_fichero}' no existe.")


# Llamar a la funcion para mostrar la tabla de multiplicar
mostrar_tabla_multiplicar()