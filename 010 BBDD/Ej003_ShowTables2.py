# Day 11 - 13/06/2023
# Ejercicios de MySQL

'''
Ejercicio 3
Conectarse con Usuario: HR, Password: HR, a la base de datos ‘HR’ y mostrar
las tablas que contiene
'''

import mysql.connector

print('\n*** EJERCICIO 3 v2 ***')

CONFIG={'host':'localhost',
        'user':'HR',
        'password':'hr',
        'database':'HR',}

# meterlo mejor en un try
try:
	# esto en si es un diccionario, estoy creando un diccionario
	# **CONFIG: enlaza el diccionario
	# **CONFIG: voy a generar un diccionario con lo que me venga
	# ** en diccionarios porque es par (2) clave-valor
	# * si fuese una lista porque es solamente un (1) valor
	mydb = mysql.connector.connect(**CONFIG)
except:
	print('Ha ocurrido un error')
finally:
	mydb.close()


# FORMA 2 - Conectarse a la database
mydb.connect(database='HR')

print('\nTablas que contiene: ')
cursor = mydb.cursor()
cursor.execute('SHOW TABLES FROM HR')

for table in cursor:
	print(table)

cursor.close()
mydb.close()