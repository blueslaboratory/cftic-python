# Day 25 - 03/07/2023
# Modulo OS y SHUTIL

'''
Ejercicio 1
Escribe un programa que recorra todos los archivos de una carpeta y muestre
por pantalla aquellos archivos cuyo tamaño sea mayor a 1MB.
'''


import os


def mostrar_archivos_grandes(ruta):

	# Itera sobre los elementos (archivos y carpetas) dentro de la ruta especificada
	for archivo in os.listdir(ruta):

		# Construye la ruta completa del archivo
		ruta_archivo = os.path.join(ruta, archivo)

		# Verifica si el elemento actual es un archivo y si su tamaño es mayor a 1MB
		if os.path.isfile(ruta_archivo) and os.path.getsize(ruta_archivo) > 1024*1024:

			# Imprime un mensaje indicando el archivo encontrado
			print(f"El archivo {archivo} es mayor a 1MB.")


ruta_carpeta = "E:\\VIDEO"
print('Ruta carpeta:', ruta_carpeta)

mostrar_archivos_grandes(ruta_carpeta)