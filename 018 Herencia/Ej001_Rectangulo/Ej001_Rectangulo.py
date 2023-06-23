# Day 19 - 23/06/2023
# Ejercicios Herencia.docx

'''
Ejercicio 1
Crear una clase Figura con un metodo calcular_area() que imprima
"Metodo calcular_area() de la clase Figura". Luego, crear una clase
Rectangulo que herede de Figura y sobrescriba el metodo calcular_area()
para calcular y mostrar el área de un rectangulo.
'''

from Ej001_Figura import Figura

class Rectangulo(Figura):

	def __init__(self, base, altura):
		self.base = base
		self.altura = altura

	# este calcularArea es independiente del de Figura
	def calcularArea(self):
		area = self.base * self.altura
		print('Area rectangulo:', area)

		print('\n*** Llamando al padre con super().calcularArea() ***')
		super().calcularArea()