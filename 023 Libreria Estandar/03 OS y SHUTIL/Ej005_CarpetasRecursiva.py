# Day 25 - 03/07/2023
# Modulo OS y SHUTIL

'''
Ejercicio 5
Escribe un programa que muestre por pantalla la estructura de directorios de
una carpeta de forma recursiva.
'''



import os


# CHATGPT
def mostrar_estructura_directorios(carpeta, nivel=0):
	# Obtener la lista de elementos (archivos y carpetas) en la carpeta
	elementos = os.listdir(carpeta)

	# Iterar sobre cada elemento
	for elemento in elementos:
		# Construir la ruta completa del elemento
		ruta_elemento = os.path.join(carpeta, elemento)

		# Imprimir el elemento con indentacion segun el nivel
		print("  " * nivel + "|-- " + elemento)

		# Verificar si el elemento es una carpeta
		if os.path.isdir(ruta_elemento):
			# Llamar recursivamente a la funcion para mostrar la estructura dentro de la carpeta
			mostrar_estructura_directorios(ruta_elemento, nivel + 1)




# SOLUCION PROFE
def mostrar_estructura_directorios1(ruta):

	# Utiliza la función os.walk para recorrer de forma recursiva los directorios
	# y archivos de la ruta especificada
	for raiz, directorios, archivos in os.walk(ruta):

		# Calcula el nivel de indentacion basado en la cantidad de separadores de
		# ruta (os.sep) en la ruta actual
		nivel = raiz.replace(ruta, '').count(os.sep)

		# Crea una cadena de espacios en blanco para la indentacion segun el nivel
		espacio = ' ' * 4 * (nivel)

		# Imprime el nombre del directorio actual entre corchetes, con la
		# indentacion correspondiente
		print(f"{espacio}[{os.path.basename(raiz)}]")

		# Itera sobre los archivos en el directorio actual y los imprime con la
		# indentacion correspondiente
		for archivo in archivos:
			print(f"{espacio}|- {archivo}")




# Carpeta raiz de la estructura de directorios a mostrar
carpeta_raiz = "E:\\DOCUMENTS"

# Llamar a la funcion para mostrar la estructura de directorios de forma recursiva
print(('\n*** CHATGPT ***'))
mostrar_estructura_directorios(carpeta_raiz)
print(('\n*** SOLUCION PROFE ***'))
mostrar_estructura_directorios1(carpeta_raiz)