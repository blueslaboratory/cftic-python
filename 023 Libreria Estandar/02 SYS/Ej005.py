# Day 25 - 03/07/2023
# Modulo SYS

'''
Ejercicio 5
Escribe un programa que reciba una cadena de texto como argumento de línea de
comandos y la muestre por pantalla en mayúsculas.
'''

# Para hacer funcionar este ejercicio hay que navegar desde la consola
# (cd, ls, tab) hasta la ruta donde se encuentra el ejercicio:

# (venv) PS E:\CFTIC\Python\Pycharm Projects\023 Libreria Estandar\02 SYS>

# Ejecutar python 'nombre del archivo' 'argumentos'
# python .\Ej005.py hola_cara_bola



import sys

cadena = sys.argv[1]

print('Cadena en mayusculas:', cadena.upper())