# Day 11 - 13/06/2023
# Ejercicios de MySQL

'''
Ejercicio 6
Mostrar los empleados  que contiene la tabla Empleados del esquema HR y
que tienen 4800 de salario y su trabajo es IT_PROG
'''

import mysql.connector

print('\n*** EJERCICIO 6 ***')

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


print('\nTrabajadores con un salario de 4800 y de trabajo IT_Prog: ')
cursor = mydb.cursor()
cursor.execute('SELECT * FROM HR.EMPLOYEES WHERE SALARY = 4800 AND JOB_ID = \'IT_PROG\'')


for table in cursor:
	print(table)


cursor.close()
mydb.close()