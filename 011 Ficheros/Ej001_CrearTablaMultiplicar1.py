# Day 12 - 14/06/2023
# Ejercicios de Ficheros


'''
Ejercicio 1
Escribir una función que pida un número entero entre 1 y 10 y guarde en un
fichero con el nombre tabla-n.txt la tabla de multiplicar de ese número,
donde n es el número introducido.
'''


print('\n*** EJERCICIO 1 - CHATGPT & MODS ***')

def pedir_numero():
	while True:
		try:
			numero = int(input('Numero entero [1,10]: '))
			if (numero >= 1 or numero <= 10):
				return numero
			else:
				print('Numero fuera del rango [1,10]')
		except ValueError:
			print('ValueError - caracteres no validos')
		except:
			print('Error general')

def generar_tabla_multiplicar():

	# Pedir al usuario un numero entero entre 1 y 10
	numero = pedir_numero()

	# Generar la tabla de multiplicar y guardarla en un archivo
	nombre_fichero = f"tabla-{numero}.txt"

	# El fichero se cierra automaticamente al salir del bloque with
	with open(nombre_fichero, 'w') as fichero:
		for i in range(1, 11):
			resultado = numero * i
			linea = f"{numero} x {i} = {resultado}\n"
			fichero.write(linea)

	print(f"La tabla de multiplicar del numero {numero} "
			f"ha sido generada y guardada en el archivo '{nombre_fichero}'")


# Llamar a la funcion para generar la tabla de multiplicar
generar_tabla_multiplicar()