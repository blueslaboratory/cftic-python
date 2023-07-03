# Day 25 - 03/07/2023
# Modulo SYS

'''
Ejercicio 3
Escribe un programa que reciba una lista de números enteros como argumento de
línea de comandos y muestre por pantalla el número más grande de la lista.
'''

# Para hacer funcionar este ejercicio hay que navegar desde la consola
# (cd, ls, tab) hasta la ruta donde se encuentra el ejercicio:

# (venv) PS E:\CFTIC\Python\Pycharm Projects\023 Libreria Estandar\02 SYS>

# Ejecutar python 'nombre del archivo' 'argumentos'
# python .\Ej003_Lista.py 1 2 3 4 5 6 7 8 9 14

# Maximo: 14


import sys

# Obtener todos los argumentos excepto el primer elemento (nombre del script)
argumentos = sys.argv[1:]

# Convertir los elementos de la lista en enteros
numeros = [int(arg) for arg in argumentos]

# Obtener el maximo
print('Maximo:', max(numeros))