# Day 16 - 20/06/2023

import sqlite3

# lugar donde me crea la BBDD
conexion = sqlite3.connect('./Ejemplos/ejemplos014_sqlite/db/HR.db')

cursor = conexion.cursor()

SQL = """
		CREATE TABLE IF NOT EXISTS persona (
			id INT AUTO_INCREMENT PRIMARY KEY,
			nombre VARCHAR(45) NOT NULL,
			edad INT(2) NULL,
			genero INT(1) NULL,
			ocupacion VARCHAR(45) NULL
		)
	"""

cursor.execute(SQL)
cursor.close()
conexion.close()