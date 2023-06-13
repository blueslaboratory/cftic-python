# Day 11 - 13/06/2023
# Ejercicios de MySQL

'''
Ejercicio 7
Insertar una nueva region en el esquema HR y después mostrar todas
las regiones
'''

import mysql.connector

print('\n*** EJERCICIO 7 ***')

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



cursor = mydb.cursor()

print('\nINSERT: ')

# region_id es primary key, no se puede hacer 2 veces el commit
datos = [101, 'Pais Vasco']
insert = cursor.execute('INSERT INTO HR.REGIONS (REGION_ID, REGION_NAME) '
                        'VALUES(%s,%s)', datos)

# obligatorio hacer el commit para que se grabe en la BBDD
# mydb.commit()
# print(insert)

cursor.execute('SELECT * FROM REGIONS')

for fila in cursor:
	print(fila)

# print(cursor.fetchall())

cursor.close()
mydb.close()