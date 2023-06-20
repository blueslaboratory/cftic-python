# Day 13 - 15/06/2023
# Ejercicios Mix

# Abrir el fichero cada que se lee
fichero = open('../datos.csv', 'r', encoding='utf-8')

print('\n*** fichero.read() ***')
contenido = fichero.read()
print(contenido)



fichero = open('../datos.csv', 'r', encoding='utf-8')

print('\n*** fichero.readlines() ***')
contenido = fichero.readlines()
print(contenido)



fichero = open('../datos.csv', 'r', encoding='utf-8')

print('\n*** fichero.readline() ***')
contenido = fichero.readline()
print(contenido)