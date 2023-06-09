# 08/06/2023
# Construir Colecciones
print('\n*** Construir lista, tupla y cuadrado***')

cuadradosLista = [x**2 for x in range(1,11)] #Lista
print(type(cuadradosLista))
print(cuadradosLista)

cuadradosTupla = tuple(x**2 for x in range(1,11)) #Tuplas
print(type(cuadradosTupla))
print(cuadradosTupla)

cuadradosSet = {x**2 for x in range(1,11)} #Set
print(type(cuadradosSet))
print(cuadradosSet)

cuadradosDiccionario = {x:x**2 for x in range(1,11)} #Diccionarios
print(type(cuadradosDiccionario))
print(cuadradosDiccionario)

cuadradosSetTuplas = {(x, x**2) for x in range(1,11)} #cuadradosSetTuplas
print(type(cuadradosSetTuplas))
print(cuadradosSetTuplas)
