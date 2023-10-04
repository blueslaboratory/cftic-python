# 08/06/2023
# Construir Colecciones
print('\n*** Construir lista, tupla y cuadrado***')

#Lista []
cuadradosLista = [x**2 for x in range(1,11)]
print(type(cuadradosLista))
print(cuadradosLista)

#Tuplas ()
cuadradosTupla = tuple(x**2 for x in range(1,11))
print(type(cuadradosTupla))
print(cuadradosTupla)

#Set {}
cuadradosSet = {x**2 for x in range(1,11)}
print(type(cuadradosSet))
print(cuadradosSet)

#Diccionarios {:}
cuadradosDiccionario = {x:x**2 for x in range(1,11)}
print(type(cuadradosDiccionario))
print(cuadradosDiccionario)

#cuadradosSetTuplas {()}
cuadradosSetTuplas = {(x, x**2) for x in range(1,11)}
print(type(cuadradosSetTuplas))
print(cuadradosSetTuplas)