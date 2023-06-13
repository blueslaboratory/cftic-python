# Day 11 - 13/06/2023
# Ejercicios de MySQL

'''
Ejercicio 4
Mostrar todos los datos que contiene la tabla Empleados del esquema HR
'''

import mysql.connector

print('\n*** EJERCICIO 4 ***')

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


# El cursor solo lo puede recoger 1 vez, se recorre 1 unica vez
# en la que el cursor llega al fondo
print('\nTablas que contiene: ')
sql = 'SELECT * FROM HR.EMPLOYEES LIMIT 10'
cursor = mydb.cursor()
cursor.execute(sql)

for table in cursor:
	print(table)



# Hay que volver a hacer un cursor.execute('SELECT * FROM HR.EMPLOYEES')
# si quieres volver a cargar el cursor (porque antes ha llegado al final)
print('\n*** fetchall() ***')
cursor.execute(sql)
rows = cursor.fetchall()

for row in rows:
	print(row)



cursor.close()
mydb.close()