# Day 13 - 15/06/2023
# Ejercicios Mix

# Para mySQL todo dios utiliza WorkBench

import mysql.connector
from  mysql.connector.errors import DatabaseError

def crear_tabla(n_tabla):
	try:
		bbdd = mysql.connector.connect(
			host='localhost',
			port='3306',
			database='hr',
			user='HR',
			password='hr'
		)

		cursor = bbdd.cursor()
		sql = f"""
			SELECT COUNT(*) FROM information_schema.tables 
			WHERE table_schema = 'HR' AND table_name = '{n_tabla}'
		"""

		cursor.execute(sql)
		valor = cursor.fetchone()

		if not valor[0]:
			sql=f"""
			CREATE  TABLE IF NOT EXISTS `{n_tabla}` (
			`id` INT NOT NULL AUTO_INCREMENT,
			`nombre` VARCHAR(45) NOT NULL,
			`edad` INT(2) NULL,
			`genero` INT(1) NULL,
			`ocupacion` VARCHAR(45) NULL,
			PRIMARY KEY (`id`))"""

		### Es conveniente resetearlo para que ocurran errores indeterminado
		cursor.reset()

		cursor.execute(sql)

	except DatabaseError:
		print('Se ha producido un error de base de datos')

	finally:
		cursor.close()
		bbdd.close()

crear_tabla('fichero')




