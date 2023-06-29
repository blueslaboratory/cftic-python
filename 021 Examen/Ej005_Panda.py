# Day 23 - 29/06/2023

'''
5.Librería Panda

Tienes un archivo CSV que contiene información sobre los estudiantes de una escuela.
El archivo tiene las siguientes columnas: "Nombre", "Edad" y "Promedio".
Quieres realizar algunas operaciones de análisis de datos utilizando Pandas.

Implementa el código necesario para cargar el archivo CSV en un DataFrame
y realizar las siguientes tareas:

* Mostrar las primeras 5 filas del DataFrame.
* Calcular la edad promedio de los estudiantes.
* Obtener la información básica del DataFrame, incluyendo el recuento de filas,
los tipos de datos de las columnas y los valores no nulos.
* Filtrar los estudiantes que tienen un promedio mayor a 90.
* Ordenar el DataFrame por edad de forma ascendente.

'''


import pandas as pd


# Cargar datos desde un archivo CSV
df = pd.read_csv('estudiantes.csv', delimiter=',')


# Primeras 5 filas del DataFrame
print('\n*** PRIMERAS 5 FILAS ***')
print(df.head(5))


# Agrupar y resumir datos
print('\n*** EDAD PROMEDIO DE LOS ESTUDIANTES ***')
edad_promedio = round(df['Edad'].mean(), 2)
print('Media de edad:', edad_promedio)


print('\n*** INFORMACION BASICA ***')
df.info()


print('\n*** DATA FRAME FILTRADO: PROMEDIO > 90 ***')
df_filtrado = df[df['Promedio'] > 90]
print(df_filtrado)


print('\n*** DATA FRAME: SORTED EDAD***')
print(df.sort_values('Edad'))
