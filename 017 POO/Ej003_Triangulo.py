# Day 19 - 23/06/2023
# Ejercicios POO.docx

'''
Ejercicio 3
Desarrollar un programa que cargue los datos de un triángulo. Implementar
una clase con los métodos para inicializar los atributos, imprimir el
valor del lado con un tamaño mayor y  el tipo de triángulo que es
(equilátero, isósceles o escaleno).
'''

class Triangulo:

	def __init__(self, cateto1, cateto2, cateto3):
		self.cateto1 = cateto1
		self.cateto2 = cateto2
		self.cateto3 = cateto3

	def medidasTriangulo(self):
		print('Metodo medidasTriangulo(self)')
		print('\tcateto1:', self.cateto1, 'cm')
		print('\tcateto2:', self.cateto2, 'cm')
		print('\tcateto3:', self.cateto3, 'cm')

	def ladoMayor(self):
		maximo = max(self.cateto1, self.cateto2, self.cateto3)
		# print('Lado mayor:', maximo, 'cm')
		return maximo

	def tipoTriangulo(self):
		if self.cateto1 == self.cateto2 == self.cateto3:
			return "Equilatero"
		elif self.cateto1 == self.cateto2 or self.cateto1 == self.cateto3 or self.cateto2 == self.cateto3:
			return "Isosceles"
		else:
			return "Escaleno"

	# el toString de java seria asi:
	def __str__(self):
		print('Metodo __str__(self)')
		return f'\tcateto1: {self.cateto1}cm' \
				f'\n\tcateto2: {self.cateto2}cm' \
				f'\n\tcateto3: {self.cateto3}cm'



t0 = Triangulo(1,1,1)
print(f'\n*** Triangulo 0 ***')
# t0.medidasTriangulo()
print(t0)
print('Lado mayor: ', t0.ladoMayor(), 'cm')
print('Tipo:', t0.tipoTriangulo())


t1 = Triangulo(1,3,3)
print(f'\n*** Triangulo 1 ***')
# t1.medidasTriangulo()
print(t1)
print('Lado mayor: ', t1.ladoMayor(), 'cm')
print('Tipo:', t1.tipoTriangulo())


t2 = Triangulo(1,2,3)
print(f'\n*** Triangulo 2 ***')
# t2.medidasTriangulo()
print(t2)
print('Lado mayor: ', t2.ladoMayor(), 'cm')
print('Tipo:', t2.tipoTriangulo())