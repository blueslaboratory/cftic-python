# Day 13 - 15/06/2023
# Ejercicios Mix


# Funcion leer fichero
def leer_fichero(nombre):
	try:

		# Abrir el fichero cada que se lee
		fichero = open(nombre, 'r', encoding='utf-8')

		print('\n*** fichero.readlines() ***')
		lineas = fichero.readlines()
		print(lineas)

		# Quitar el /n
		datos = []

		for i, linea in enumerate(lineas):
			# Quitamos la primera linea
			if i>0:
				datos.append(linea.strip())

		print(datos)

		return datos

	except FileNotFoundError:
		print('FileNotFoundError - Fichero no encontrado')

	finally:
		# Cerrar fichero
		fichero.close()