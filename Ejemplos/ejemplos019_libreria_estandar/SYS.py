# Day 26 - 04/07/2023
# Librerías Estándar.docx
# Modulo SYS

# Para hacer funcionar estos ejemplos (el nº1) hay que navegar desde la consola
# (cd, ls, tab) hasta la ruta donde se encuentra el ejercicio:

# (venv) PS E:\CFTIC\Python\Pycharm Projects\Ejemplos\ejemplos019_libreria_estandar>

# Ejecutar python 'nombre del archivo' 'argumentos'
# python .\SYS.py argumento1 argumento2


import sys


print('\n*** 1.Argumentos de linea de comandos ***')

for arg in sys.argv:
	print(arg)



print('\n*** 2.Rutas de búsqueda de módulos ***')
# sys.path: es una lista que contiene las rutas de búsqueda de módulos de Python

for path in sys.path:
	print(path)



print('\n*** 3.Salida estandar y salida de error estandar ***')

sys.stdout.write("Este es un mensaje en la salida estándar.\n")
sys.stderr.write("Este es un mensaje de error en la salida estándar de error.\n")



print('\n*** 4.Finalización del programa ***')
# Esto NUNCA SE HACE porque te cargas la aplicacion
respuesta = input("¿Desea salir del programa? (s/n): ")

if respuesta.lower() == "s":
	sys.exit(0)
else:
	print("Continuando con la ejecucion del programa...")



print('\n*** 5.Funcionalidades del intérprete ***')
print('sys.version:', sys.version)
print('sys.platform:', sys.platform)
print('sys.stdin:', sys.stdin)