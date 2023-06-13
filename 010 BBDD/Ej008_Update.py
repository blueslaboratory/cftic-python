# Day 11 - 13/06/2023
# Ejercicios de MySQL

'''
Ejercicio 8
Modificar la  region creada en el Ejercicio 7 y después mostrar todas las
regiones del esquema HR
'''

import mysql.connector

print('\n*** EJERCICIO 8 ***')

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

print('\nUPDATE: ')

# region_id es primary key, no se puede hacer 2 veces el commit
datos = [99, 'MADRID', 100]
update = cursor.execute('UPDATE HR.REGIONS '
                        'SET REGION_ID = %s, '
                        'REGION_NAME = %s '
                        'WHERE REGION_ID = %s', datos)


# obligatorio hacer el commit para que se grabe en la BBDD
# mydb.commit()
# print(insert)


cursor.execute('SELECT * FROM HR.REGIONS')

for fila in cursor:
	print(fila)


cursor.close()
mydb.close()