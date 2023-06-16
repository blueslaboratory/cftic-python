# Day 14 - 16/06/2023
# Ejercicios Mix

import mysql.connector
import mysql.connector.errors


def insertar_datos(datos):

	try:
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

		# myDB.commit()
		cursor.close()

	except mysql.connector.errors.DatabaseError:
		print('Se ha producido un erro en la base de datos')

	finally:
		myDB.close()


datos = [('Juan Pérez',30,1,'Ingeniero'), ('María García',25,0,'Doctora')]

insertar_datos(datos)