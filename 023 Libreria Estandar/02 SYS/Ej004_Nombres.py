# Day 25 - 03/07/2023
# Modulo SYS

'''
Ejercicio 4
Escribe un programa que reciba una serie de nombres como argumentos de línea de
comandos y los muestre por pantalla en orden inverso.
'''

# Para hacer funcionar este ejercicio hay que navegar desde la consola
# (cd, ls, tab) hasta la ruta donde se encuentra el ejercicio:

# (venv) PS E:\CFTIC\Python\Pycharm Projects\023 Libreria Estandar\02 SYS>

# Ejecutar python 'nombre del archivo' 'argumentos'
# python .\Ej004_Nombres.py Ana Bruno Cecilia David Elena Francisco Gandhi Hilda Iñaki

# nombresReverse:
# ['Iñaki', 'Hilda', 'Gandhi', 'Francisco', 'Elena', 'David', 'Cecilia', 'Bruno', 'Ana']


import sys

# Obtener todos los argumentos excepto el primer elemento (nombre del script)
argumentos = sys.argv[1:]

# Darle la vuelta
argumentos.reverse()

print('Nombres en orden inverso:')
print(argumentos)