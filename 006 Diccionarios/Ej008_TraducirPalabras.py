# Ejercicios de Diccionarios
# Day 7 - 07/06/2023

'''
Ejercicio 8
Escribir un programa que cree un diccionario de traducción español-inglés.
El usuario introducirá las palabras en español e inglés separadas por dos puntos,
y cada par <palabra>:<traducción> separados por comas. El programa debe crear
un diccionario con las palabras y sus traducciones. Después pedirá una frase
en español y utilizará el diccionario para traducirla palabra a palabra.
Si una palabra no está en el diccionario debe dejarla sin traducir.
'''

print('\n*** EJERCICIO 8 *** - SOLUCION PROFE')

diccionario = {}


print('String par palabras')
print('e.g. hola:hello,mister:mister,presidente:president,una:a,botellita:bottle,agua:water')
stringPalabras = input('> ')

for parTraduccion in stringPalabras.split(','):
	clave, valor = parTraduccion.lower().split(':')
	diccionario[clave] = valor

print(diccionario)


print('\nFrase en español')
print('e.g. Hola Mister Presidente una botellita de agua please')
frase = input('> ').lower()


print('\nTraduccion')
for palabra in frase.split(' '):
	if palabra in diccionario:
		print(diccionario[palabra], end=' ')
	else:
		print(palabra, end=' ')
