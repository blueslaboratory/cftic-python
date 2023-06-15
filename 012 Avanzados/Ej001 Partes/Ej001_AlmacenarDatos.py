# Day 13 - 15/06/2023
# Ejercicios Mix

import mysql.connector

datos = [('Juan Pérez',30,1,'Ingeniero'), ('María García',25,0,'Doctora')]

myDB = mysql.connector.connect(
	host='localhost',
	port='3306',
	database='hr',
	user='HR',
	password='hr'
)

cursor = myDB.cursor()


SQL = """
	INSERT INTO fichero (nombre, edad, genero, ocupacion)
	VALUES (%s, %s, %s, %s)
	"""

for dato in datos:
	cursor.execute(SQL, dato)
	print("Se han insertado", cursor.rowcount, 'registros')
	cursor.reset()
	print(datos)
