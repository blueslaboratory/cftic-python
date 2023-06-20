# Day 14 - 16/06/2023
# Ejercicios Mix


from mysql.connector.errors import DatabaseError
from dao.Ej001_ConnectionManager import ConexionMySQL
from dao.errors.Ej001_ErrorsDAO import ErrorDAO
class PersonaDAO:

	def crear_tabla(n_tabla):
		try:
			miConexion = ConexionMySQL
			bbdd = miConexion.abrir_conexion()
			cursor = bbdd.cursor()

			sql = f"""
					SELECT COUNT(*) FROM information_schema.tables 
					WHERE table_schema = 'HR' AND table_name = '{n_tabla}'
				"""
			cursor.execute(sql)
			valor = cursor.fetchone()

			if not valor[0]:
				sql = f"""
					CREATE  TABLE IF NOT EXISTS `{n_tabla}` (
					`id` INT NOT NULL AUTO_INCREMENT,
					`nombre` VARCHAR(45) NOT NULL,
					`edad` INT(2) NULL,
					`genero` INT(1) NULL,
					`ocupacion` VARCHAR(45) NULL,
					PRIMARY KEY (`id`))"""

				##### Es conveniente resetearlo para que ocurran errores indeterminado
				cursor.reset()
				cursor.execute(sql)

			cursor.close()

		except DatabaseError:
			# print('Se ha producido un error de base de datos')
			# Lanzamos la excepcion con ErrorDAO
			# raise no te crea la excepcion, te la lanza
			raise ErrorDAO('Se ha producido un error de base de datos')

			miExcepcion = ErrorDAO('Se ha producido un error de base de datos')
			raise miExcepcion
		except:
			raise ErrorDAO('Se ha producido un error general')
		finally:
			miConexion.cerrar_conexion()


	# Que datos sea opcional:
	# datos = None
	# SIEMPRE QUE SON METODOS DE UNA CLASE TIENES QUE PONERLE EL SELF
	# EN CASO CONTRARIO LO TOMA COMO UNA FUNCION

	def insertar_datos(self, datos=None):
		try:
			miConexion = ConexionMySQL()
			bbdd = miConexion.abrir_conexion()
			cursor = bbdd.cursor()

			sql ='''
				INSERT INTO persona (nombre,edad,genero,ocupacion)
				VALUES (%s,%s,%s,%s)
				'''

			# Para tuplas
			'''
			for dato in datos:
				cursor.execute(sql,dato)
				print('Se han insertado',cursor.rowcount,'registros')
				cursor.reset()
			'''

			# Para Objetos de tipo persona
			for persona in datos:
				cursor.execute(sql, (persona.nombre, persona.edad, persona.genero, persona.profesion))
				persona.id = cursor.lastrowid # Para conseguir el id de persona

				print('Se han insertado', cursor.rowcount, 'registros')
				print(persona)
				cursor.reset()


			# bbdd.commit()
			cursor.close()


		except DatabaseError:
			# print('Se ha producido un error de base de datos')
			# Lanzamos la excepcion con ErrorDAO
			# raise no te crea la excepcion, te la lanza
			raise ErrorDAO('Se ha producido un error de base de datos')

			miExcepcion = ErrorDAO('Se ha producido un error de base de datos')
			raise miExcepcion
		except:
			raise ErrorDAO('Se ha producido un error general')

		finally:
			miConexion.cerrar_conexion()


# Forzando el error DataBaseError
# personaDAO = PersonaDAO()
# datos = [('JesuCristo Garcia', 33, 1, 'Masculino')]
# personaDAO.insertar_datos(datos)