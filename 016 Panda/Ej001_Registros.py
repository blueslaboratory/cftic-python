# Day 17 - 21/06/2023
# Ejercicios Libreria Panda.docx
# pip install panda

'''
Ejercicio 1
Crea un DataFrame a partir de un diccionario y muestra los primeros 
cinco registros.
'''

import pandas as pd 


# Crear un DataFrame a partir de un diccionario
datos0 = {'Nombre': ['Juan', 'María', 'Pedro', 'Ana', 'Luis', 'Laura', 'Miguel', 'Sara', 'Carlos', 'Lucía'],
         'Edad': [25, 30, 35, 28, 32, 27, 31, 29, 33, 26],
         'Ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Valencia', 'Málaga', 'Bilbao', 'Alicante', 'Granada', 'Murcia', 'Zaragoza']}


df = pd.DataFrame(datos0)

# Mostrar el DataFrame
print('\n*** DATA FRAME: DATOS 0 ***')
print(df)

print('\n*** PRIMERAS 5 FILAS: DATOS 0 ***')
print(df.head(5))


print('\n*** ULTIMAS 5 FILAS: DATOS 0 ***')
print(df.tail(5))

print('\n*** SLICING 7 PRIMEROS: DATOS 0 ***')
print(df[:7])

print('\n*** SLICING 7 ULTIMOS ORDEN NATURAL: DATOS 0 ***')
print(df[-7:])

print('\n*** SLICING 7 ULTIMOS ORDEN INVERSO: DATOS 0 ***')
print(df[-1:-8:-1])

print('\n*** PARES: DATOS 0 ***')
print(df[::2])

print('\n*** LISTA AL REVES: DATOS 0 ***')
print(df[::-1])


print('\n*** ILOC ***')
# dataframe.iloc[filas, columnas]
# Acceder a una fila específica por su índice
# Accede a la tercera fila del DataFrame
print('*** df.iloc[2] ***')
print(df.iloc[2])

# Acceder a un valor específico por su posición
# Accede al valor en la tercera fila y segunda columna del DataFrame
print('\n*** df.iloc[2, 1] ***')
print(df.iloc[2, 1])

# Acceder a un rango de filas y columnas
# Accede a las filas 2 y 3 y columnas 2 y 3 del DataFrame
print('\n*** df.iloc[1:3, 1:3] ***')
print(df.iloc[1:3, 1:3])




# Crear un DataFrame a partir de un diccionario
datos1 = {'c0':['v0'],
          'c1':['v1'],
          'c2':['v2'],
          'c3':['v3'],
          'c4':['v4'],
          'c5':['v5'],
          'c6':['v6'],
          'c7':['v7'],
          'c8':['v8'],
          'c9':['v9']}

df1 = pd.DataFrame(datos1)

# Mostrar el DataFrame
print('\n*** DATA FRAME: DATOS 1 ***')
print(df1)



# Obtener las 5 primeras columnas
# df.iloc[:, :5] 
# (:) selecciona todas las filas del DataFrame "df1".
# (:5) selecciona las primeras 5 columnas del DataFrame "df1".

primeras_columnas = df1.iloc[:, :5]

print('\n*** PRIMEROS 5 COLUMNAS: DATOS 1 ***')
print(primeras_columnas)