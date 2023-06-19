# Day 14 - 16/06/2023
# Ejercicios Mix
def leer_fichero(nombre):
	try:
		# Abrir el fichero
		with open(nombre, 'r', encoding='UTF-8') as fichero:
			# Leemos contenido
			lineas = fichero.readlines()
			datos = []
			for i, linea in enumerate(lineas):
				if i > 0:
					datos.append(linea.strip())

			return datos
	except FileNotFoundError:
		print('El fichero no se ha encontrado')


datos = leer_fichero('datos.csv')
print(datos)
