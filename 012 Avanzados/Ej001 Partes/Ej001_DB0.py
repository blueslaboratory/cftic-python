# Day 13 - 15/06/2023
# Ejercicios Mix

# Para mySQL todo dios utiliza WorkBench

import mysql.connector

conexion = mysql.connector.connect(
		host='localhost',
		user='HR',
		password='hr',
		database='HR',
		# Especifica la codificacion utf8mb4
		charset='utf8mb4'
)

cursor = conexion.cursor()

SQL = """
	SELECT COUNT(*) FROM information_schema.tables
	WHERE table_schema = 'HR' AND table_name = 'FICHERO'
"""


cursor.execute(SQL)

# Cuando devuelve una columna, devuelve una tupla siempre
# tablas = cursor.fetchall()
tablas = cursor.fetchone()
print(tablas[0])

if not tablas[0]:
	print('No existe la tabla')

	SQL = """
		CREATE TABLE IF NOT EXISTS fichero (
			id INT AUTO_INCREMENT PRIMARY KEY,
			nombre VARCHAR(45) NOT NULL,
			edad INT(2) NULL,
			genero INT(1) NULL,
			ocupacion VARCHAR(45) NULL
		)
	"""

	print(SQL)

	# esto es como hacer un flush
	# cursor.reset(): limpiar el buffer
	cursor.reset()

	cursor.execute(SQL)

else:
	print('Existe la tabla')



# Cerrar las conexiones
cursor.close()
conexion.close()