# Day 25 - 03/07/2023
# Modulo OS y SHUTIL

'''
Ejercicio 4
Escribe un programa que cree una copia de seguridad de una carpeta,
comprimiéndola en un archivo ZIP.
'''

# SOLUCION PROFE

import shutil


def crear_copia_seguridad(ruta_carpeta, ruta_archivo_zip_destino):
	shutil.make_archive(ruta_archivo_zip_destino, 'zip', ruta_carpeta)


ruta_carpeta_origen = "E:\\IMAGES\\Margaritas"
ruta_archivo_zip_destino = "E:\\IMAGES\\copy\\margaritas"
crear_copia_seguridad(ruta_carpeta_origen, ruta_archivo_zip_destino)