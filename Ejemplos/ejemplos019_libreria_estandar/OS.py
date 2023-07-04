# Day 26 - 04/07/2023
# Librerías Estándar.docx
# Modulo OS

import os

ruta = os.path.join(".\\", "OS.py")

existe = os.path.exists(ruta)
size = os.path.getsize(ruta)

if existe:
	print(f"El archivo {ruta} existe y tiene un tamaño de {size} bytes.")
else:
	print(f"El archivo {ruta} no existe.")

directorio_actual = os.getcwd()
print(f"El directorio de trabajo actual es: {directorio_actual}")

archivos = os.listdir(directorio_actual)
print(f"Archivos en el directorio actual: {archivos}")



print('\nCrear y borrar directorios ')
# os.makedirs(path): Crea directorios recursivamente.
# os.makedirs('carpetita')
# os.remove('carpetita')