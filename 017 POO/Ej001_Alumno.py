# Day 19 - 23/06/2023
# Ejercicios POO.docx

'''
Ejercicio 1
Realizar un programa que conste de una clase llamada Alumno que tenga como 
atributos el nombre y la nota del alumno. Definir los métodos para 
inicializar sus atributos, imprimirlos y mostrar un mensaje con el 
resultado de la nota y si ha aprobado o no.
'''


'''
Funciones vs Metodos ChatGPT:

Los bloques:

	- codigo __init__(self, nombre, nota), 
	- infoAlumno(self), 
	- aprobado(self), 
	- __str__(self) 

Son metodos de la clase Alumno porque estan definidos dentro de esa clase 
y actuan sobre los objetos de esa clase.

Pueden acceder a los atributos de la clase utilizando la palabra clave self.

En resumen, las funciones son bloques de codigo independientes que pueden ser 
llamados directamente, mientras que los metodos son funciones asociadas a una 
clase y se acceden a traves de instancias de esa clase.
'''

class Alumno:

	# Puedes poner que devuelve un None
	def __init__(self, nombre, nota) -> None:
		self.nombre = nombre
		self.nota = nota

	# Puedes no poner lo que devuelve
	def infoAlumno(self):
		print('*** Metodo infoAlumno(self) ***')
		print('Nombre:', self.nombre)
		print('Note:', self.nota)

	def aprobado(self) -> str:
		print('*** Metodo aprobado(self) ***')
		mensaje = 'Suspendido'

		if self.nota >= 5:
			mensaje = 'Aprobado'

		return mensaje

	# En Python el toString de Java seria:
	def __str__(self):
		print('*** Metodo __str__(self) ***')
		return f'Alumno {self.nombre}\n' \
		       f'Nota: {self.nota}'



alumno = Alumno('Blue', 9.9)
print(f'\n*** {alumno.nombre.upper()} ***')
alumno.infoAlumno()
# Llamando al __str__(self)
print(alumno)
print(f'{alumno.nombre} - Aprobado:', alumno.aprobado())


alumno0 = Alumno('Red', 5.5)
print(f'\n*** {alumno0.nombre.upper()} ***')
alumno0.infoAlumno()
# Llamando al __str__(self)
print(alumno0)
print(f'{alumno0.nombre} - Aprobado:', alumno0.aprobado())


alumno1 = Alumno('Green', 4.9)
print(f'\n*** {alumno1.nombre.upper()} ***')
alumno1.infoAlumno()
# Llamando al __str__(self)
print(alumno1)
print(f'{alumno1.nombre} - Aprobado:', alumno1.aprobado())