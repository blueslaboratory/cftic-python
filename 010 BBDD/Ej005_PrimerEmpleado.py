# Day 11 - 13/06/2023
# Ejercicios de MySQL

'''
Ejercicio 5
Mostrar el primer empleado que contiene la tabla Empleados del esquema HR
'''

import mysql.connector

print('\n*** EJERCICIO 5 ***')

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


print('\nPrimer empleado de HR: ')
cursor = mydb.cursor()
cursor.execute('SELECT * FROM HR.EMPLOYEES ORDER BY EMPLOYEE_ID LIMIT 1')

for table in cursor:
	print(table)


print('\n*** fetchone: ')
cursor.execute('SELECT * FROM HR.EMPLOYEES ORDER BY EMPLOYEE_ID LIMIT 1')
rows = cursor.fetchone()

for row in rows:
	print(row)

cursor.close()
mydb.close()