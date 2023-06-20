# Day 16 - 20/06/2023
# pip install pandas
# pip install openpyxl

import pandas as pd 

# Cargar datos desde un archivo CSV
df = pd.read_csv('./Ejemplos/ejemplos013_panda/datos.csv')

# Escribir datos a un archivo Excel
# Solo sale bien en el Excel original
df.to_excel('./Ejemplos/ejemplos013_panda/excel/personas.xlsx', index=False)


# Cargar datos desde una base de datos SQL
import mysql.connector
conexion = mysql.connector.connect(host='localhost',
									port='3306',
									database='hr',
									user='HR',
									password='hr')

df = pd.read_sql_query('SELECT * FROM persona', conexion)

print('*** DATA FRAME PERSONAS ***')
print(df)

