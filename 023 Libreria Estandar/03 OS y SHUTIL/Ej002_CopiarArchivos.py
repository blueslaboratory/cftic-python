# Day 25 - 03/07/2023
# Modulo OS y SHUTIL

'''
Ejercicio 2
Escribe un programa que copie todos los archivos de una carpeta a otra carpeta
de destino.
'''

# CHATGPT


import os
import shutil


def copiar_archivos(origen, destino):
    # Obtener la lista de archivos en la carpeta de origen
    archivos = os.listdir(origen)

    # Copiar cada archivo a la carpeta de destino
    for archivo in archivos:
        ruta_origen = os.path.join(origen, archivo)
        ruta_destino = os.path.join(destino, archivo)

        # Verificar si el elemento actual es un archivo
        if os.path.isfile(ruta_origen):
            shutil.copy2(ruta_origen, ruta_destino)


# Carpeta de origen y carpeta de destino
carpeta_origen = "E:\\IMAGES\\Margaritas\\"
print(carpeta_origen)
carpeta_destino = "E:\\IMAGES\\copy\\"
print(carpeta_destino)


# Llamar a la funcion para copiar los archivos
copiar_archivos(carpeta_origen, carpeta_destino)