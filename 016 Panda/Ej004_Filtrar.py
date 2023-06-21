# Day 17 - 21/06/2023
# Ejercicios Libreria Panda.docx
# pip install panda

'''
Ejercicio 4
Filtra un DataFrame para mostrar solo las filas que cumplan una 
determinada condicion.
'''


import pandas as pd 


# Crear un DataFrame a partir de un diccionario
datos0 = {'Nombre': ['Juan', 'María', 'Pedro', 'Ana', 'Luis', 'Laura', 'Miguel', 'Sara', 'Carlos', 'Lucía'],
         'Edad': [25, 30, 35, 30, 32, 27, 31, 29, 33, 30],
         'Ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Valencia', 'Málaga', 'Bilbao', 'Alicante', 'Granada', 'Murcia', 'Zaragoza']}

df = pd.DataFrame(datos0)


# Mostrar el DataFrame
print('\n*** DATA FRAME: SORTED ***')
print(df.sort_values('Edad'))


# Filtrar filas basado en una condición
print('\n*** DATA FRAME FILTRADO ***')
df_filtrado = df[df['Edad'] == 30]
print(df_filtrado) 