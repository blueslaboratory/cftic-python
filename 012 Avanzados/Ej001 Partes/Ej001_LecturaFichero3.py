# Day 13 - 15/06/2023
# Ejercicios Mix


# Funcion leer fichero
def leer_fichero(nombre):
	try:
		# Abrir el fichero con with: no hace falta el finally con .close()
		with open(nombre, 'r', encoding='UTF-8') as fichero:
			# Leemos contenido

			print('\n*** fichero.readlines() ***')
			lineas = fichero.readlines()
			print(lineas)

			# Quitar el /n
			datos = []
			for i, linea in enumerate(lineas):
				# Quitamos la primera linea
				if i > 0:
					datos.append(linea.strip())

			print(datos)

			return datos

	except FileNotFoundError:
		print('FileNotFoundError - Fichero no encontrado')


datos = leer_fichero('datos.csv')
print(datos)