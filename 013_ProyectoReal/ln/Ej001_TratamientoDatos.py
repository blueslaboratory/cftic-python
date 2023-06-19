# Day 14 - 16/06/2023
# Ejercicios Mix

from ln.errors.Ej001_ErrorsLN import ErrorLN
from data.Ej001_Persona import Persona

class TratamientoDatos:

	# Convertir una funcion a metodo, agregar self: OBLIGATORIO
	def tratar_datos(self, datos_iniciales):

		try:
			datos_finales = []

			for dato in datos_iniciales:
				campos = dato.split(';')
				campos[2] = 0 if campos[2] == 'Masculino' else 1
				campos[3] = campos[3].upper()
				# datos_finales.append(tuple(campos))

				persona = Persona(None, campos[0], campos[1], campos[2], campos[3])
				datos_finales.append(persona)

				print(persona)

			return datos_finales

		except:
			raise ErrorLN('ErrorLN - Se ha producido un error general')

