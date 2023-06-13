# Day 11 - 13/06/2023
# Ejercicios de MySQL

'''
Ejercicio 3
Conectarse con Usuario: HR, Password: HR, a la base de datos ‘HR’ y mostrar
las tablas que contiene
'''

import mysql.connector

print('\n*** EJERCICIO 3 v0 ***')

# esto en si es un diccionario, estoy creando un diccionario
mydb = mysql.connector.connect(
	# localhost identifica la propia maquina, ip local: 127.0.0.1
	# si quisieramos acceder a otra maquina tendriamos que poner su ip
	host = 'localhost',
	user='HR',
	password='hr',

	# FORMA 1 - Conectarse a la database
	database='HR'
)

# FORMA 2 - Conectarse a la database
mydb.connect(database='HR')

print('\nTablas que contiene: ')
cursor = mydb.cursor()
cursor.execute('SHOW TABLES FROM HR')

for table in cursor:
	print(table)

cursor.close()
mydb.close()