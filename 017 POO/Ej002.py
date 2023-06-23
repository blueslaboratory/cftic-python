# Day 19 - 23/06/2023
# Ejercicios POO.docx

'''
Ejercicio 2
Realizar un programa que tenga una clase Persona con las siguientes
características. La clase tendrá como atributos el nombre y la edad de
una persona. Implementar los métodos necesarios para inicializar los
atributos, mostrar los datos e indicar si la persona es mayor de edad o no.
'''


class Persona:

	def __init__(self, nombre, edad):
		self.nombre = nombre
		self.edad = edad

	def infoPersona(self):
		print('*** Metodo infoPersona(self) ***')
		print('Nombre:', self.nombre)
		print('Edad:', self.edad)

	def mayorEdad(self):
		print('*** Metodo mayorEdad(self) ***')
		bool = False

		if self.edad >= 18:
			bool = True

		return bool

	# el toString de java seria asi:
	def __str__(self):
		print('*** Metodo __str__(self) ***')
		return f'Nombre: {self.nombre}' \
				f'\nEdad: {self.edad}'



persona = Persona('Blue', 33)
print(f'\n*** {persona.nombre.upper()} ***')
persona.infoPersona()
print(persona)
print(f'Mayor de edad (+18):', persona.mayorEdad())


persona0 = Persona('Red', 69)
print(f'\n*** {persona0.nombre.upper()} ***')
persona0.infoPersona()
print(persona0)
print(f'Mayor de edad (+18):', persona0.mayorEdad())


persona1 = Persona('Green', 9)
print(f'\n*** {persona1.nombre.upper()} ***')
persona1.infoPersona()
print(persona1)
print(f'Mayor de edad (+18):', persona1.mayorEdad())