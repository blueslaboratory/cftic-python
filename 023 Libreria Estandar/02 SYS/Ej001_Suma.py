# Day 25 - 03/07/2023
# Modulo SYS

'''
Ejercicio 1
Escribe un programa que reciba dos números enteros como argumentos de línea de
comandos y muestre por pantalla su suma.
'''

# Para hacer funcionar este ejercicio hay que navegar desde la consola
# (cd, ls, tab) hasta la ruta donde se encuentra el ejercicio:

# (venv) PS E:\CFTIC\Python\Pycharm Projects\023 Libreria Estandar\02 SYS>

# Ejecutar python 'nombre del archivo' 'argumentos'
# python .\Ej001_Suma.py 5 5

# Suma: 10


import sys

n1 = int(sys.argv[1])
n2 = int(sys.argv[2])

suma = n1+n2

print('Suma:', suma)