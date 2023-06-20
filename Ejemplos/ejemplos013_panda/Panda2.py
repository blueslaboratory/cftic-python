# Day 16 - 20/06/2023

import pandas as pd


# Crear un DataFrame a partir de un diccionario
datos = {'Nombre': ['Juan', 'María', 'Pedro', 'Ana'],
         'Edad': [25, 30, 35, 28],
         'Ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Valencia']}


print('\n*** DATA FRAME ORIGINAL ***')
df = pd.DataFrame(datos)
print(df)


print('\n*** DATA FRAME COLUMNA CALCULADA ***')
#  Agregar una columna calculada
df['Edad_Doble'] = df['Edad'] * 2
print(df['Edad_Doble'])


# Aplicar una funcion a una columna
# el lambda es un for
print('\n*** DATA FRAME df[\'Ciudad_Mayusculas\'] ***')
df['Ciudad_Mayusculas'] = df['Ciudad'].apply(lambda x: x.upper())

'''
df['Ciudad_Mayusculas'] = df['Ciudad']
for index, x in enumerate(df['Ciudad']):
    df['Ciudad_Mayusculas'][index] = x.upper()
'''


print(df['Ciudad_Mayusculas'])


# Agrupar y resumir datos
print('\n*** DATA FRAME AGRUPAR Y RESUMIR ***')
df_agrupado = df.groupby('Ciudad')['Edad'].mean()
print(df_agrupado)


# Eliminar filas o columnas
print('\n*** DATA FRAME ELIMINAR FILAS O COLUMNAS ***')
df = df.drop(['Edad'], axis=1)
print(df)


# Combinar DataFrames
print('\n*** DATA FRAME CONCATENADO ***')

df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})

df_concatenado = pd.concat([df1, df2])

print(df_concatenado)