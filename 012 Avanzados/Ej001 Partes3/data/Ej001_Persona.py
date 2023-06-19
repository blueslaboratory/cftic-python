# Day 15 - 19/06/2023
# Ejercicios Mix

class Persona:
	def __init__(self, id, nombre, edad, genero, profesion):
		self.id = id
		self.nombre = nombre
		self.edad = edad
		self.genero = genero
		self.profesion = profesion


	# Flechita: lambda, que la funcion devuelve un string
	def __str__(self) -> str:

		cadena = f'''Persona[
			id: {self.id},
			Nombre: {self.nombre},
			Edad: {self.edad},
			Genero: {self.genero},
			Profesion: {self.profesion}
		'''

		return cadena