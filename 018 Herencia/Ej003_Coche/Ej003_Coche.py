# Day 19 - 23/06/2023
# Ejercicios Herencia.docx

'''
Ejercicio 3
Crear una clase Vehiculo con un atributo velocidad y un método mostrar_velocidad()
que imprima la velocidad del vehículo. Luego, crear una clase Coche que herede
de Vehiculo y tenga un método adicional acelerar() que aumente la velocidad
en 10 unidades.
'''

from Ej003_Vehiculo import Vehiculo

class Coche(Vehiculo):

	def acelerar(self):
		print('*** Aaaaaaaacelerandoo +10km/h ***')
		self.velocidad += 10
		print('Velocidad:', self.velocidad, 'km/h')