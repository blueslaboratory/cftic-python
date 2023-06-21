# Day 17 - 21/06/2023
# Ejercicios Libreria Panda.docx
# pip install panda

'''
Ejercicio 3
Calcula el promedio de una columna específica en un DataFrame.
'''

import pandas as pd 


# Crear un DataFrame a partir de un diccionario
datos0 = {'Nombre': ['Juan', 'María', 'Pedro', 'Ana', 'Luis', 'Laura', 'Miguel', 'Sara', 'Carlos', 'Lucía'],
         'Edad': [25, 30, 35, 28, 32, 27, 31, 29, 33, 26],
         'Ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Valencia', 'Málaga', 'Bilbao', 'Alicante', 'Granada', 'Murcia', 'Zaragoza']}

df = pd.DataFrame(datos0)

# Mostrar el DataFrame
print('\n*** DATA FRAME ***')
print(df)


# Agrupar y resumir datos
print('\n*** DATA FRAME AGRUPAR Y RESUMIR ***')
df_agrupado = df['Edad'].mean()
print('Media de edad:', df_agrupado)


print('\n*** DATA FRAME ILOC ***')
# toda la columna 1 (Edad)
df_filtrado = df.iloc[:, 1]
print(df_filtrado) 
