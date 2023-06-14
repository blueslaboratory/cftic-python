# Day 12 - 14/06/2023
# Ejercicios de Ficheros


'''
Ejercicio 3
Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero 
tabla-n.txt con la tabla de multiplicar de ese número, y muestre por pantalla 
la línea m del fichero. Si el fichero no existe debe mostrar un mensaje por 
pantalla informando de ello.
'''

print('\n*** EJERCICIO 3 - CHATGPT & MODS ***')


def pedir_numero(num):
	while True:
		try:
			numero = int(input(f'Numero {num} [1,10]: '))
			if (numero >= 1 or numero <= 10):
				return numero
			else:
				print('Numero fuera del rango [1,10]')
		except ValueError:
			print('ValueError - caracteres no validos')



def mostrar_linea_tabla():

	# Pedir al usuario dos numeros enteros entre 1 y 10
	# Ojo que m puede tener valores negativos y contaria desde el final hacia atras
	n = pedir_numero('n')
	m = pedir_numero('m')


	# Leer el archivo tabla-n.txt y mostrar la línea m
	nombre_fichero = f"tabla-{n}.txt"
	try:
		with open(nombre_fichero, 'r') as fichero:
			lineas = fichero.readlines()
			if m <= len(lineas):
				linea_m = lineas[m - 1]
				print(f"Linea {m} de la tabla de multiplicar del numero {n}:")
				print(f"{linea_m}")
			else:
				print(f"No existe la linea {m} en la tabla de multiplicar")
	except FileNotFoundError:
		print(f"El archivo '{nombre_fichero}' no existe")


mostrar_linea_tabla()