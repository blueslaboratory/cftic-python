# Day 11 - 13/06/2023

'''
Comandos a ejecutar desde el terminal:

(por si acaso desinstalar el de por defecto)
pip uninstall mysql-connector-python
pip install mysql-connector-python
'''


import mysql.connector

# esto en si es un diccionario, estoy creando un diccionario
mydb = mysql.connector.connect(
	# localhost identifica la propia maquina, ip local: 127.0.0.1
	# si quisieramos acceder a otra maquina tendriamos que poner su ip
	host = 'localhost',
	user='HR',
	password='hr',

	# FORMA 1 - Conectarse a la database
	# conectarse a la BBDD directamente desde el conector:
	database='HR'
)

# FORMA 2 - Conectarse a la database
mydb.connect(database='HR')

print(mydb)



print('\nDatabases en el WorkBench')
cursor = mydb.cursor()
print(cursor)
cursor.execute('show databases')
print(cursor)

for database in cursor:
	print(database)



print('\nTodos los empleados')
cursor.execute('select * from hr.employees')
for employee in cursor:
	print(employee)



print('\nInsert')

# region_id es primary key, no se puede hacer 2 veces el commit
datos = [101, 'Madrid']
# %s es en minusculas, sino no va!!
insert = cursor.execute('INSERT INTO HR.REGIONS (REGION_ID, REGION_NAME) VALUES(%s,%s)', datos)

# obligatorio hacer el commit para que se grabe en la BBDD
# mydb.commit()
print(insert)
print(cursor.rowcount)




# Cerrar la el cursor y la conexion
print('\nCerrar el cursor y la conexion')
mydb.close()