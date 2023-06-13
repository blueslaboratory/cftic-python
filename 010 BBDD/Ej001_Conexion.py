# Day 11 - 13/06/2023
# Ejercicios de MySQL

'''
Ejercicio 1
Conectarse en  la máquina local con el usuario: HR, Password: HR
'''

import mysql.connector

print('\n*** EJERCICIO 1 ***')

# esto en si es un diccionario, estoy creando un diccionario
mydb = mysql.connector.connect(
	# localhost identifica la propia maquina, ip local: 127.0.0.1
	# si quisieramos acceder a otra maquina tendriamos que poner su ip
	host = 'localhost',
	user='HR',
	password='hr'
)

print('Objeto conexion:', mydb)

mydb.close()