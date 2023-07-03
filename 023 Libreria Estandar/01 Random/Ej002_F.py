# Day 24 - 30/06/2023
# Modulo Random

'''
Ejercicio 2
Escribe una función que genere una contraseña aleatoria con una longitud
específica. La contraseña debe estar compuesta por letras mayúsculas, letras
minúsculas y dígitos numéricos.
'''

# SOLUCION PROFE

import random
import string

def generar_contrasena(longitud):
	# conjunto de caracteres a partir del cual se generara la pw
	caracteres = string.ascii_letters + string.digits
	# seleccionar caracteres aleatorios 
	contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
	return contrasena

longitud_contrasena = 8
contrasena_generada = generar_contrasena(longitud_contrasena)
print("La contraseña generada es:", contrasena_generada)