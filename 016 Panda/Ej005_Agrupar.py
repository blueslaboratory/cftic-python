# Day 17 - 21/06/2023
# Ejercicios Libreria Panda.docx
# pip install panda

'''
Ejercicio 5
Agrupa un DataFrame por una columna y muestra la cantidad de registros 
en cada grupo.
'''


import pandas as pd 


# Crear un DataFrame a partir de un diccionario
datos0 = {'Nombre': ['Juan', 'María', 'Pedro', 'Ana', 'Luis', 'Laura', 'Miguel', 'Sara', 'Carlos', 'Lucía'],
         'Edad': [25, 30, 35, 30, 32, 27, 31, 29, 33, 30],
         'Ciudad': ['Madrid', 'Bilbao', 'Sevilla', 'Valencia', 'Málaga', 'Bilbao', 'Madrid', 'Bilbao', 'Zaragoza', 'Zaragoza']}

df = pd.DataFrame(datos0)


# Mostrar el DataFrame
print('\n*** DATA FRAME: SORTED ***')
print(df.sort_values('Ciudad'))


# Filtrar filas basado en una condición
# Agrupar 
print('\n*** DATA FRAME AGRUPAR ***')
df_agrupado = df.groupby('Ciudad').size()
print(df_agrupado)
