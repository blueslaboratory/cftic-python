# 12/06/2023 - Day 10
# Ejercicios de Funciones

'''
Ejercicio 6
Escribir una función que reciba una muestra de números en una lista y devuelva
su media.
'''

print('\n*** EJERCICIO 6 ***')

def media(listaNumeros):
	acumulador = 0.0

	for index, n in enumerate(listaNumeros):
		print(str(index) +'.', 'Numero:', n)
		acumulador += float(n)
		print('Acumulador:', acumulador)
		print('Media:', acumulador/(index+1))
		print()

	media = acumulador/len(listaNumeros)

	return acumulador, media



print('Lista de numeros (e.g. 3,3,4,2,5,1,6,0)')
listaNumeros = list(input('> ').split(','))

acm, m = media(listaNumeros)
print('Media de la lista:', m)
print('Acumulador: ', acm)
print('len(listaNumeros):', len(listaNumeros))




print('\n*** EJERCICIO 6 - SOLUCION PROFE ***')

def media(lista):
	return sum(lista)/ len(lista)

# *lista: permite un numero variable de argumentos
# mediaConParametros(1,2,3)
def mediaConParametros(*lista):
	return sum(lista)/ len(lista)

lista = [1,2,3]

print('La media de los numeros de ', str(lista), ' es ', media(lista))
print('La media de los numeros 1,2,3  es ', mediaConParametros(1,2,3))