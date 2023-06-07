# Ejercicios de Diccionarios
# Day 7 - 07/06/2023

'''
Ejercicio 7
Escribir un programa que cree un diccionario simulando una cesta de la compra.
El programa debe preguntar el artículo y su precio y añadir el par al diccionario,
hasta que el usuario decida terminar. Después se debe mostrar por pantalla la
lista de la compra y el coste total, con el siguiente formato:

Lista de la compra
Artículo 1	Precio
Artículo 2	Precio
Artículo 3	Precio
…	    …
Total	Coste
'''

print('\n*** EJERCICIO 7 ***')

# Diccionario vacio
cesta = {}
continuar = True
costeTotal = 0

# Solicitar informacion al usuario
while continuar:
	clave = input("Articulo (clave): ").title()
	valor = float(input("Precio (valor): "))

	# Almacenar el dato en el diccionario
	cesta[clave] = valor

	# Preguntar al usuario si desea agregar más datos
	respuesta = input("\nAgregar mas articulos (s/n): ")

	# Salir del bucle si el usuario no desea agregar más datos
	if respuesta.lower() == "n":
		continuar = False


print('\nTicket lista de la compra:')
for clave in cesta:
	print(clave, '\t', cesta[clave])
	costeTotal += cesta[clave]

print('\nPrecio total:', costeTotal, '€')
