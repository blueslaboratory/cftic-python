# Day 14 - 16/06/2023
# Ejercicios Mix

from ln.errors.Ej001_ErrorsLN import ErrorLN

class LecturaFichero:

	# Constructor
	def __init__(self, nombre):
		self.nombre = nombre

	# Convertir una funcion a metodo, agregar self: OBLIGATORIO
	def leer_fichero(self):
		try:
			#Abrir el fichero
			with open(self.nombre,'r',encoding='UTF-8') as fichero:
				#Leemos contenido
				lineas = fichero.readlines()
				datos = []
				for i,linea in enumerate(lineas):
					if i> 0:
						datos.append(linea.strip())

				return datos

		except FileNotFoundError:
			print('El fichero no se ha encontrado')

		except:
			raise ErrorLN('ErrorLN - Se ha producido un error general')