# 12/06/2023 - Day 10
# Ejercicios de Funciones

'''
Ejercicio 8
Escribir una función que reciba una muestra de números en una lista y devuelva
un diccionario con su media, varianza y desviación típica.
'''


print('\n*** EJERCICIO 8 - SOLUCION PROFE ***')

def fcuadrados(lista):
	cuadrados = []
	for numero in lista:
		cuadrados.append(numero**2)
	return cuadrados

def datos_numericos(lista):
	datos_numeros = {}
	datos_numeros['Media'] = sum(lista)/len(lista)
	datos_numeros['Varianza'] = sum(fcuadrados(lista)) / len(lista) - datos_numeros['Media'] ** 2
	datos_numeros['Desviacion tipica'] = datos_numeros['Varianza'] ** 0.5
	return datos_numeros

def datos_numericos_parametros(*lista):
	datos_numeros = {}
	datos_numeros['Media'] = sum(lista) / len(lista)
	datos_numeros['Varianza'] = sum(fcuadrados(lista)) / len(lista) - datos_numeros['Media'] ** 2
	datos_numeros['Desviacion tipica'] = datos_numeros['Varianza'] ** 0.5
	return datos_numeros


lista = [1,2,3]

print('Los datos numéricos de los numeros de la lista', str(lista), 'es', datos_numericos(lista))
print('Los datos numéricos 1,2,3  es', datos_numericos_parametros(1,2,3))