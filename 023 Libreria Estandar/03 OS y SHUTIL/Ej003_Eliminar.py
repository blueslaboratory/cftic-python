# Day 25 - 03/07/2023
# Modulo OS y SHUTIL

'''
Ejercicio 3
Escribe un programa que elimine todos los archivos con una extensión específica
de una carpeta.
'''

# CHATGPT


import os


def eliminar_archivos_extension(ruta, extension):
    # Obtener la lista de archivos en la carpeta
    archivos = os.listdir(ruta)

    # Eliminar los archivos con la extension especifica
    for archivo in archivos:
        if archivo.endswith(extension):
            ruta_archivo = os.path.join(ruta, archivo)
            os.remove(ruta_archivo)

# Carpeta y extensión de los archivos a eliminar
ruta_carpeta = "E:\\IMAGES\\copy\\"
extension = ".jpg"

# Llamar a la funcion para eliminar los archivos con la extensión especificada
eliminar_archivos_extension(ruta_carpeta, extension)