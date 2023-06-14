# Day 12 - 14/06/2023
# Ejercicios de Ficheros


'''
Ejercicio 2
Escribir una función que pida un número entero entre 1 y 10, lea el fichero 
tabla-n.txt con la tabla de multiplicar de ese número, done n es el número 
introducido, y la muestre por pantalla. Si el fichero no existe debe 
mostrar un mensaje por pantalla informando de ello.
'''


print('\n*** EJERCICIO 2 - SOLUCION PROFE ***')


n = int(input('Numero [1,10]:'))
nombre_fichero = 'tabla-'+str(n)+'.txt'

try:
	fichero = open(nombre_fichero, 'r')
except:
	print('El fichero '+nombre_fichero+' no existe')
else:
	print(fichero.read())
	fichero.close()