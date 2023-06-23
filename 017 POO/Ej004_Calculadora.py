# Day 19 - 23/06/2023
# Ejercicios POO.docx

'''
Ejercicio 4
Realizar un programa en el cual se declaren dos valores enteros por teclado
utilizando el método __init__. Calcular después la suma, resta,
multiplicación y división. Utilizar un método para cada una e imprimir los
resultados obtenidos. Llamar a la clase Calculadora.
'''

class Calculadora:

	# Nunca meter una funcion dentro de un constructor
	def __init__(self, n1, n2):
		self.n1 = n1
		self.n2 = n2

	def suma(self):
		s = self.n1 + self.n2
		return s

	def resta(self):
		r = self.n1 - self.n2
		return r

	def multiplicacion(self):
		m = self.n1 * self.n2
		return m

	def division(self):
		d = self.n1 / self.n2
		return d

	# para ver la funcion eval
	def operar(self, operacion):
		return eval(operacion)

	# el toString de java seria asi:
	def __str__(self):
		return f'\tn1: {self.n1}' \
				f'\n\tn2: {self.n2}'


# Control de flujo: controlamos que los numeros son validos
flag = True

while flag:
	try:
		n1 = int(input('Numero 1: '))
		n2 = int(input('Numero 2: '))

		flag = False

		c = Calculadora(n1, n2)

		print('\n*** Calculadora ***')
		print('\tSuma: ', c.suma())
		print('\tResta: ', c.resta())
		print('\tMultiplicacion: ', c.multiplicacion())

		if (n2 == 0):
			raise ZeroDivisionError

		print('\tDivision: ', c.division())

		print('\n *** Operacion a realizar: eval ***')
		print('E.g. 4*1+14-3+6')
		operacion = input('Operacion: ')
		print(c.operar(operacion))

	# Poner varias excepciones: hay que ponerlas entre ()
	except (ValueError, ZeroDivisionError):
		print('El valor introducido no es valido')