# Day 11 - 13/06/2023
# Ejercicios de MySQL

'''
Ejercicio 2
Conectarse con Usuario: HR, Password: HR y mostrar las bases de datos a las
que puede acceder.
'''

import mysql.connector

print('\n*** EJERCICIO 2 ***')

# esto en si es un diccionario, estoy creando un diccionario
mydb = mysql.connector.connect(
	# localhost identifica la propia maquina, ip local: 127.0.0.1
	# si quisieramos acceder a otra maquina tendriamos que poner su ip
	host = 'localhost',
	user='HR',
	password='hr'
)

print('\nDatabases a las que se puede acceder: ')
cursor = mydb.cursor()
cursor.execute('SHOW DATABASES')
# print(cursor)

for database in cursor:
	print(database)


cursor.close()
mydb.close()