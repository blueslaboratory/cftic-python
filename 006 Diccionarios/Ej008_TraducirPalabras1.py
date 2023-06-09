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

print()
print('\n*** EJERCICIO 8 *** - SOLUCION PROFE CLASE 1')

diccionario = {}

# Crear diccionario de n palabras
n = 2
print('\nCrear diccionario de ' +str(n) +' palabras')

for i in range(n):
	palabra_castellano = input('Palabra en castellano: ')
	palabra_ingles = input('Palabra en ingles: ')
	diccionario[palabra_castellano] = palabra_ingles


# Crear diccionario 2
print('\nCrear diccionario con un bucle')
continuar = True
while continuar:
	palabras = input('Palabras formato (castellano:ingles) ->')
	itemDiccionario = palabras.split(':')
	diccionario[itemDiccionario[0]] = itemDiccionario[1]
	valor = input('Continuar (S/N) -> ').upper()
	# Operador ternario (Java: valor=='s'?true:false;)
	# Normalmente suele estar prohibido
	continuar = True if valor=='S' else False



frase = input('\nDame frase: ')

fraseList = frase.split()
fraseListTraducida = []


for palabra in fraseList:
	# mirar si esta la palabra en las keys
	# es mejor no modificar los elementos de una lista mientras la estas recorriendo
	if palabra in diccionario.keys():
		fraseListTraducida.append(diccionario[palabra])
	else:
		fraseListTraducida.append(palabra)
	

# Para que no imprima una lista, para que nos imprima una frase
fraseTraducida = ' '.join(fraseListTraducida)

print('La frase traducida es:', fraseTraducida)