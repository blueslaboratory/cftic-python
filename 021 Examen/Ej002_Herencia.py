# Day 23 - 29/06/2023

'''
2.Ejercicio de Herencia

Supongamos que estás construyendo un programa para administrar una biblioteca.
Tienes una clase base llamada Libro que representa un libro genérico.
Quieres crear una clase hija llamada LibroDigital que herede de Libro y
agregue funcionalidades específicas para los libros digitales.

La clase Libro tiene los siguientes atributos:

* titulo: una cadena que representa el título del libro.
* autor: una cadena que representa el autor del libro.
* genero: una cadena que representa el género del libro.

La clase Libro tiene los siguientes métodos:

* obtener_info(): imprime la información del libro en el siguiente formato:
"Título: {titulo}, Autor: {autor}, Género: {genero}".

La clase LibroDigital hereda todos los atributos y métodos de la clase Libro
y agrega el siguiente atributo:

* formato: una cadena que representa el formato del libro digital (por
ejemplo, PDF, EPUB).

La clase LibroDigital también agrega el siguiente método:

* obtener_info(): sobrescribe el método obtener_info() de la clase padre e
imprime la información del libro digital en el siguiente formato:
"Título: {titulo}, Autor: {autor}, Género: {genero}, Formato: {formato}".
'''


class Libro:
	def __init__(self, titulo, autor, genero):
		self.titulo = titulo
		self.autor = autor
		self.genero = genero

	def obtener_info(self):
		print(f'Titulo: {self.titulo}, Autor: {self.autor}, Genero: {self.genero}')


class LibroDigital(Libro):
	def __init__(self, titulo, autor, genero, formato):
		super().__init__(titulo, autor, genero)
		self.formato = formato


	def obtener_info(self):
		print(f'Titulo: {self.titulo}, Autor: {self.autor}, Genero: {self.genero}, Formato: {self.formato}')


# Libro
libro = Libro("El Gran Gatsby", "F. Scott Fitzgerald", "Ficcion")
libro.obtener_info()

# LibroDigital
libroDigital = LibroDigital("Orgullo y prejuicio", "Jane Austen", "Romance", "PDF")
libroDigital.obtener_info()