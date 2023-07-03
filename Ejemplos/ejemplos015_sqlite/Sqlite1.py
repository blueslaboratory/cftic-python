# Day 16 - 20/06/2023
# Operaciones de acceso a datos en 2 tipos diferentes de bases de datos: MySQL y SQLite3.

import pandas as pd




# MYSQL
# Cargar datos de una base de datos
import mysql.connector

conexion1 = mysql.connector.connect(
			host='localhost',
			port='3306',
			database='hr',
			user='HR',
			password='hr'
		)

# Lee los datos de la tabla 'persona' en la base de datos MySQL 
# y los carga en un objeto DataFrame de pandas
df = pd.read_sql_query('SELECT * FROM persona', conexion1)

print('\n*** MYSQL: DATA FRAME PERSONAS ***')
print(df)

# Cerrar la conexion MYSQL
conexion1.close()




# SQLLITE3
import sqlite3

# Establece una conexion con una base de datos SQLite3 ubicada en:
# './Ejemplos/ejemplos015_sqlite/db/HR.db'.
conexion2 = sqlite3.connect('./Ejemplos/ejemplos015_sqlite/db/HR.db')

# Define el nombre de la tabla en la base de datos SQLite3 a la que se accederá
nombreTabla = 'persona'

df.to_sql(nombreTabla, conexion2, if_exists='replace', index=False)
# if_exists = 'append' --> los datos del DataFrame se agregarán a la tabla existente 
# if_exists = 'replace' --> los datos del DataFrame se reemplazan en la tabla 
# index = False --> el indice del DataFrame no se debe incluir como una columna adicional en la tabla de la DB


# Lee los datos de la tabla 'persona' en la base de datos SQLite3 y 
# los carga en un objeto DataFrame de pandas
df = pd.read_sql_query('SELECT * FROM persona', conexion2)

print('\n*** SQLITE3: DATA FRAME PERSONAS DE SQLITE3 ***')
print(df)


# Cerrar la conexion SQLLITE
conexion2.close()