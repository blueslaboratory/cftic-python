# Day 13 - 15/06/2023
# Ejercicios Mix

# Si esto fuese un nuevo proyecto habria que instalar un conector:
# pip install mysql.connector.python

'''
Ejercicio 1
Consiste en coger los datos de un archivo .csv, insertarlos en un base de datos
HR, hay dos formas de hacerlo:

1. Leyendo todo el fichero e insertando en la base de datos
2. Ir leyendo cada linea del csv e ir insertando cada linea en la base de datos

Los campos del csv que se insertaran en la BBDD son:
nombre;edad;género;ocupación
nombre: varchar
edad: integer
género: valores 0 (femenino),1 (masculino), 2
ocupación: varchar

Un ejemplo de linea seria:
María García;25;0;Doctora

El programa debe crear la tabla llamada fichero, controlar si la tabla esta creada,
encapsular los datos lo maximo posible en funciones y realizar un control de
excepciones estricto.

La tabla se crea con la siguiente sentencia:

CREATE TABLE 'fichero' (
	'id' INT NOT NULL AUTO_INCREMENT,
	'nombre' VARCHAR(45) NOT NULL,
	'edad' INT(2) NULL,
	'genero' INT(1) NULL,
	'ocupacion' VARCHAR(45) NULL,
	PRIMARY KEY ('id')
);
'''

import csv
import mysql.connector


def crear_tabla(cursor):
	try:
		SQL = """
		DROP TABLE IF EXISTS fichero
		"""
		cursor.execute(SQL)

		SQL = """
		CREATE TABLE IF NOT EXISTS fichero (
			id INT AUTO_INCREMENT PRIMARY KEY,
			nombre VARCHAR(45) NOT NULL,
			edad INT(2),
			genero INT(1),
			ocupacion VARCHAR(45)
		)
		"""
		cursor.execute(SQL)
		print("Exito al crear la tabla fichero")

	except mysql.connector.Error as error:
		print("Error al crear la tabla fichero: ", error)


def insertar_datos(cursor, datos):
	try:
		SQL = """
		INSERT INTO fichero (nombre, edad, genero, ocupacion)
		VALUES (%s, %s, %s, %s)
		"""
		cursor.execute(SQL, datos)
		print("Exito al insertar datos")
		print(datos)
	except mysql.connector.Error as error:
		print("Error al insertar datos: ", error)


def leer_csv(nombre_archivo):
	datos_csv = []

	try:
		with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
			# Saltar la primera linea de encabezados
			next(archivo)

			for linea in archivo:
				# strip(): Eliminar espacios en blanco al principio y al final
				# strip(): No elimina los espacios en blanco de entremedias
				linea = linea.strip()
				datos = linea.split(';')
				datos_csv.append(datos)

		return datos_csv

	except FileNotFoundError:
		print("No existe el archivo")
		return []


# Utilizando la libreria que permite leer csvs
def leer_csv_import_csv(nombre_archivo):
	datos_csv = []

	try:
		with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
			lector_csv = csv.reader(archivo, delimiter=';')
			# Saltar la primera linea de encabezados
			next(lector_csv)

			for linea in lector_csv:
				datos_csv.append(linea)

		return datos_csv
	except FileNotFoundError:
		print("No existe el archivo")
		return []


def procesar_datos(datos):
	datos_procesados = []

	for linea in datos:

		# SIN UNPACKING:
		nombre = linea[0]
		edad = int(linea[1])
		genero = int(linea[2])
		ocupacion = linea[3]


		# UNPACKING VISUAL
		# Si linea es['María García', '25', '0', 'Doctora']
		# nombre, edad, genero, ocupacion = 'María García', '25', '0', 'Doctora'
		'''
		nombre, edad, genero, ocupacion = linea[0], linea[1], linea[2], linea[3]
		edad = int(edad)
		genero = int(genero)
		'''

		# UNPACKING:
		'''
		nombre, edad, genero, ocupacion = linea
		edad = int(edad)
		genero = int(genero)
		'''

		datos_procesados.append((nombre, edad, genero, ocupacion))

	return datos_procesados


def insertar_datos_desde_csv(nombre_archivo):
	try:
		conexion = mysql.connector.connect(
			host='localhost',
			user='HR',
			password='hr',
			database='HR',
			# Especifica la codificacion utf8mb4
			charset='utf8mb4'
		)
		cursor = conexion.cursor()
		crear_tabla(cursor)
		datos_csv = leer_csv(nombre_archivo)
		datos_procesados = procesar_datos(datos_csv)

		for datos in datos_procesados:
			insertar_datos(cursor, datos)

		conexion.commit()

	except mysql.connector.Error as error:
		print("Error de conexión a la base de datos:", error)

	finally:
		cursor.close()
		conexion.close()


# Ejemplo de uso
nombre_archivo = 'datos.csv'
insertar_datos_desde_csv(nombre_archivo)
