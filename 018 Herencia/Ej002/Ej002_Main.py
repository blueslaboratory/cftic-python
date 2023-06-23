# Day 19 - 23/06/2023
# Ejercicios Herencia.docx

'''
Ejercicio 2
Crear una clase Animal con un método hacer_sonido() que imprima
"Sonido del animal". Luego, crear una clase Perro que herede de Animal y
sobrescriba el método hacer_sonido() para imprimir "Guau guau".
'''

from Ej002_Animal import Animal
from Ej002_Perro import Perro
from Ej002_Gato import Gato

# Crear los objetos
perro = Perro()
gato = Gato()

listaAnimales = [perro, gato, Perro(), Animal(), Gato()]
# listaAnimales = [perro, gato]
# listaAnimales = [Perro(), Animal(), Gato()]

for animal in listaAnimales:
	print('El animal:', type(animal), 'Hace sonido:', animal.hacerSonido())




# Experimentos
print('\n\n\n*** Experimentos ***')
class MiClase:
	def __init__(self, animal):
		self.animal = animal

	def dameSonido(self):
		return self.animal.hacerSonido()


miClase = MiClase(Gato())
listaAnimales = [miClase, MiClase(Gato()), MiClase(Perro()), MiClase(Gato())]
for mc in listaAnimales:
	print('El animal: ', mc, 'Hace sonido', mc.dameSonido())