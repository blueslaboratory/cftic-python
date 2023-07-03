# Day 25 - 03/07/2023
# Modulo SYS

'''
Ejercicio 2
Escribe un programa que reciba una cadena de texto como argumento de línea de
comandos y muestre por pantalla su longitud.
'''

# Para hacer funcionar este ejercicio hay que navegar desde la consola
# (cd, ls, tab) hasta la ruta donde se encuentra el ejercicio:

# (venv) PS E:\CFTIC\Python\Pycharm Projects\023 Libreria Estandar\02 SYS>

# Ejecutar python 'nombre del archivo' 'argumentos'
# python .\Ej002_CopiarArchivos.py hola_carabola

# Longitud cadena: 13


import sys

cadena = str(sys.argv[1])

print('Longitud cadena:', len(cadena))