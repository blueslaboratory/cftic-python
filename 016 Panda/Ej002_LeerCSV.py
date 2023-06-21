# Day 17 - 21/06/2023
# Ejercicios Libreria Panda.docx
# pip install panda

'''
Ejercicio 2
Lee un archivo CSV y muestra las primeras diez filas.
'''

import pandas as pd 


# Cargar datos desde un archivo CSV
df = pd.read_csv('./016 Panda/datos.csv', delimiter=';')


# Mostrar el DataFrame
print('\n*** DATA FRAME ***')
print(df)

print('\n*** PRIMERAS 10 FILAS ***')
print(df.head(10))


print('\n*** DICCIONARIO ***')
'''
Convertir el DataFrame en un diccionario de registros
Cada registro es un diccionario con:
* claves correspondientes a los nombres de las columnas
* valores correspondientes a los datos de cada fila.
'''
diccionario = df.head(10).to_dict(orient='records')

for registro in diccionario: 
    print(registro)