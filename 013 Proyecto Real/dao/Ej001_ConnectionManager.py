# Day 14 - 16/06/2023
# Ejercicios Mix

import mysql.connector
from mysql.connector.errors import DatabaseError

class ConexionMySQL:

	# costructor de la clase
	# inicializa el atributo conexion a None
	# ver: ejemplos013_POO

	def __init__(self):
		# si la quieres privada habria que refactorizar conexion a __conexion
		self.conexion = None

	def abrir_conexion(self):
		self.conexion = mysql.connector.connect(host='localhost',
												port='3306',
												database='hr',
												user='HR',
												password='hr')
		return self.conexion
	def cerrar_conexion(self):
		self.conexion.close()



# Ejemplo de funcionamiento
miObjetoConexion = ConexionMySQL()
print(miObjetoConexion)
miObjetoConexion.abrir_conexion()
print(miObjetoConexion.conexion)
