# Day 14 - 16/06/2023
class Auto:

	# el constructor con parametros por defecto
	def __init__(self, marca, modelo):
		self.marca = 'Tesla'
		self.modelo = 'Cybertruck'
		print('Estoy en el constructor, me han pasado los parametros: ')
		print('\t* Marca:', marca)
		print('\t* Modelo:', modelo)

	def ponerMarcaModelo(self, marca, modelo):
		self.marca = marca
		self.modelo = modelo
		print('\nEstoy en ponerModelo(self, marca, modelo)')


	def mostrarMarcaModelo(self):
		print('\nEstoy en ostrarModeloMarca(self)')
		print('\t* Marca:', self.marca)
		print('\t* Modelo:', self.modelo)


miAuto = Auto('Nissan', 'Skyline')

# print(miAuto)
print('Objeto miAuto creado:')
print('\t* miAuto.marca', miAuto.marca)
print('\t* miAuto.marca', miAuto.modelo)


miAuto.ponerMarcaModelo('Nissan', 'Skyline')
# print(miAuto)
print('\t* miAuto.marca', miAuto.marca)
print('\t* miAuto.marca', miAuto.modelo)


miAuto.mostrarMarcaModelo()