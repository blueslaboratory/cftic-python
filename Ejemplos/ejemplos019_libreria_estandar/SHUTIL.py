# Day 26 - 04/07/2023
# Librerías Estándar.docx
# Modulo SHUTIL

import shutil
import os

# Crear el directorio
os.makedirs('./folder')

# Crea un archivo comprimido de un directorio
shutil.make_archive("archivo", "zip", "./")

# Copia un archivo
shutil.copy("./archivo.zip", "./archivo_copia.zip")

# Mueve un archivo
shutil.move("./archivo.zip", "folder/archivo.zip")
shutil.move("./archivo_copia.zip", "folder/archivo_copia.zip")

# Elimina un directorio y su contenido de forma recursiva
# shutil.rmtree("./folder")