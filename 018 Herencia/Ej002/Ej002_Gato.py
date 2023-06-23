# Day 19 - 23/06/2023
# Ejercicios Herencia.docx

'''
Ejercicio 2
Crear una clase Animal con un método hacer_sonido() que imprima
"Sonido del animal". Luego, crear una clase Perro que herede de Animal y
sobrescriba el método hacer_sonido() para imprimir "Guau guau".
'''

from Ej002_Animal import Animal

class Gato(Animal):

	def hacerSonido(self):
		return 'Miau Meow Lmeow'