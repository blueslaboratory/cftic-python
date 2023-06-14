# Day 12 - 14/06/2023
# Ejercicios de Ficheros


'''
Ejercicio 3
Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero 
tabla-n.txt con la tabla de multiplicar de ese número, y muestre por pantalla 
la línea m del fichero. Si el fichero no existe debe mostrar un mensaje por 
pantalla informando de ello.
'''

print('\n*** EJERCICIO 3 - SOLUCION PROFE ***')

# Ojo que m puede tener valores negativos y contaria desde el final hacia atras
n = int(input('Numero n [1,10]: '))
m = int(input('Numero m [1,10]: '))

nombre_fichero = 'tabla-'+str(n)+'.txt'

try:
	with open(nombre_fichero, 'r') as fichero:
		lineas = fichero.readlines()

		if m <= len(lineas):
			print(lineas[m - 1])
		else:
			print('No existe la linea ' +str(m))
except:
	print('No existe el fichero ' +nombre_fichero)
