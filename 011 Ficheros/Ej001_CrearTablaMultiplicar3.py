# Day 12 - 14/06/2023
# Ejercicios de Ficheros


'''
Ejercicio 1
Escribir una función que pida un número entero entre 1 y 10 y guarde en un
fichero con el nombre tabla-n.txt la tabla de multiplicar de ese número,
donde n es el número introducido.
'''

print('\n*** EJERCICIO 1 - CLASE BIS ***')


def crear_fichero(num):
	try:
		resultado = 0
		# Primero validamos el numero
		# Comprobamos que verdaderamente viene un numero
		if (not isinstance(num, int)):
			raise ValueError
		# num = int(num) # Va a admitir valores '0' '1' '223'

		# Despues se trabaja con el fichero teniendo en cuenta su excepcion:FileNotFoundError
		# fichero = open(f'tabla-{num}', 'w')
		with open(f'tabla-{num}.txt', 'w') as fichero:
			lineas = []
			for numero in range(1, 11):
				resultado = num * numero
				lineas.append(f'{num} x {numero} = {resultado}')
			fichero.writelines(lineas)

		# fichero.close()

	except ValueError as ve:
		print('El numero no es valido')
	except FileNotFoundError:
		print('El fichero no se ha podido crear')


def pedir_numero():
	numero = int(input('Dame numero: '))
	return numero


try:
	numero = pedir_numero()
	crear_fichero(numero)
except Exception as e:
	print('No se ha podido generar la tabla de multiplicar')
