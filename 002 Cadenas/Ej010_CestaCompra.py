# Ejercicios de Cadenas
# Day 2 - 31/05/2023

'''
Ejercicio 10
Escribir un programa que pregunte por consola por los productos de una cesta de la
compra, separados por comas, y muestre por pantalla cada uno de los productos en una
línea distinta.
'''
print('\n *** EJERCICIO 10 ***')
cesta = input('Cesta (e.g. baguette,croisant,dinosaurus...): ')
cestaList = cesta.split(',')
for producto in cestaList:
	print('\t' +producto)


## Solucion Profe
print('\n *** EJERCICIO 10 - SOLUCION PROFE 1 ***')
productos_compra = input("Productos compra (separados por comas): ")
print('Productos:\n' + productos_compra.replace(',', '\n'))



## Otra solucion
## Aunque modifiquemos los items de la lista, EN LA LISTA NO SE MODIFICAN
print('\n *** EJERCICIO 10 - SOLUCION PROFE 2 ***')

lista_productos_compra = productos_compra.split(',')

for item in lista_productos_compra:
     item = item.strip().upper()
     print(item)

print(lista_productos_compra)



## Otra solucion
## Aqui la lista SE MODIFICA
print('\n *** EJERCICIO 10 - SOLUCION PROFE 3 ***')

lista_productos_compra = productos_compra.split(',')

for index in range (0, len(lista_productos_compra)):
     lista_productos_compra[index]= lista_productos_compra[index].strip().upper()
     print(lista_productos_compra[index])

print(lista_productos_compra)