# Day 16 - 20/06/2023
# pip install pandas

import pandas as pd 


# Crear un DataFrame a partir de un diccionario
datos = {'Nombre': ['Juan', 'María', 'Pedro', 'Ana'],
         'Edad': [25, 30, 35, 28],
         'Ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Valencia']}

'''
Los diccionarios son útiles para asociar valores con claves únicas.
diccionario = {'clave1': valor1, 'clave2': valor2, 'clave3': valor3} 

Las listas son útiles para almacenar una colección ordenada y mutable de elementos.
lista = [elemento1, elemento2, elemento3]

Las tuplas son útiles cuando necesitas una secuencia inmutable de valores.
tupla = (elemento1, elemento2, elemento3)
'''


df = pd.DataFrame(datos) 

# Mostrar el DataFrame
print('\n*** DATA FRAME ***')
print(df) 

# Obtener información del DataFrame
print('\n*** DATA FRAME INFO ***')
print(df.info()) 

# Obtener estadísticas descriptivas del DataFrame
print('\n*** ESTADISTICAS ***')
print(df.describe()) 

# Filtrar filas basado en una condición
print('\n*** DATA FRAME FILTRADO ***')
df_filtrado = df[df['Edad'] > 30]
print(df_filtrado) 

# Ordenar el DataFrame por una columna
print('\n*** DATA FRAME ORDENADO POR EDAD ***')
df_ordenado = df.sort_values('Edad')
print(df_ordenado)