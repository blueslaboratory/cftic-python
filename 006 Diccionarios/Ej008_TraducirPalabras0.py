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
print('e.g. Hola Mister Presidente una boteLLita de agua please')
frase = input('> ').lower()


print('\nTraduccion')
for palabra in frase.split(' '):
	if palabra in diccionario:
		print(diccionario[palabra], end=' ')
	else:
		print(palabra, end=' ')



print()
print('\n*** EJERCICIO 8 *** - SOLUCION PROFE CLASE 0')

diccionario = {}

# Crear diccionario de 2 palabras
for i in range(2):
	palabra_castellano = input('Palabra en castellano: ')
	palabra_ingles = input('Palabra en ingles: ')
	diccionario[palabra_castellano] = palabra_ingles


# Crear diccionario 2
continuar = True
while continuar:
	palabras = input('Palabras formato (castellano:ingles) ->')
	itemDiccionario = palabras.split(':')
	diccionario[itemDiccionario[0]] = itemDiccionario[1]
	valor = input('Continuar (S/N)-> ').upper()
	# Operador ternario (Java: valor=='s'?true:false;)
	# Normalmente suele estar prohibido
	continuar = True if valor=='S' else False



frase = input('\nDame frase: ')

fraseList = frase.split()
fraseListTraducida = fraseList.copy()

# for: recorro frase list
# enumerate me da un par de valores, el indice del elemento y el elemento
# 'la' 'casa' 'es' 'azul'
#  0      1     2     3
# el for se recorre con el par de valores:
# 1º iteracion: 0 y 'la'
# 2º iteracion: 1 y 'casa'
# 3º iteracion: 2 y 'es'
# 4º iteracion: 3 y 'azul'

for index, palabra in enumerate(fraseList):
	# mirar si esta la palabra en las keys
	# es mejor no modificar los elementos de una lista mientras la estas recorriendo
	if palabra in diccionario.keys():
		fraseListTraducida[index] = diccionario[palabra]


# Para que no imprima una lista, para que nos imprima una frase
fraseTraducida = ' '.join(fraseListTraducida)

print('\nLa frase traducida es:', fraseTraducida)