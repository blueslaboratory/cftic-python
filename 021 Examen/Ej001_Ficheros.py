# Day 23 - 29/06/2023

'''
1.Ejercicio de ficheros, funciones y excepciones

Supongamos que estás trabajando en un programa de gestión de notas de estudiantes.
Quieres implementar una función que lea un archivo de texto que contiene las
notas de los estudiantes y calcule el promedio de cada estudiante.
Luego, quieres escribir los promedios calculados en otro archivo de texto.
Implementa la función calcular_promedios() que reciba el nombre del archivo
de entrada y el nombre del archivo de salida, y realice las siguientes tareas:

* Leer el archivo de entrada, que tiene el siguiente formato:
	- Cada línea contiene el nombre del estudiante, seguido de dos números
	enteros separados por espacios que representan las notas obtenidas por el
	estudiante en dos exámenes.
	- Ejemplo: "Estudiante1 80 90"
* Calcular el promedio de las notas para cada estudiante.
* Escribir en el archivo de salida, una línea por cada estudiante, con el
siguiente formato:
	- El nombre del estudiante, seguido de dos números decimales separados por
	espacios que representan las notas promedio obtenidas por el estudiante en
	los exámenes.
	- El promedio debe tener dos decimales de precisión.
	- Ejemplo: "Estudiante1 85.00"

La solución debe contener gestión de excepciones.
'''


def calcular_promedios(fichero_entrada, fichero_salida):

	try:
		print('\n*** 1. ABRIR EL FICHERO PARA LECTURA ***')
		with open(fichero_entrada, 'r') as archivo_entrada:
			lineas = archivo_entrada.readlines()

		# Calcular los promedios
		promedios = []
		for linea in lineas:
			elementos = linea.split()
			estudiante = elementos[0]

			# Objeto de tipo map que aplica la funcion int()
			# a cada elemento de la lista elementos[1:]
			# elementos[1:] toma todos los elementos desde 1 hasta el final
			notas = list(map(int, elementos[1:]))

			promedio = sum(notas) / len(notas)
			# append de una tupla (estudiante, promedio)
			promedios.append((estudiante, promedio))

		print('\n*** 2. ABRIR EL FICHERO PARA ESCRITURA ***')
		with open(fichero_salida, 'w') as archivo_salida:
			# Escribir los promedios en el archivo de salida

			for estudiante, promedio in promedios:
				linea = f'{estudiante} {promedio:.2f}\n'
				archivo_salida.write(linea)

		print('Calculo de promedios completado')

	except FileNotFoundError:
		print('No se encontro el archivo de entrada')

	except Exception as e:
		print(f'Error: {str(e)}')


calcular_promedios('notas_entrada.txt', 'notas_salida.txt')