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

print('\n*** EJERCICIO 8 *** - SOLUCION PROFE CLASE 3')

# Las funciones van arriba y en el mismo orden en el que se usan
def establecer_diccionario():
	diccionario={}
	while True:
		palabras = input('Palabras formato (castellano:ingles) ->')
		itemDiccionario = palabras.split(':')
		diccionario[itemDiccionario[0]] = itemDiccionario[1]
		valor = input('Continuar (S/N) -> ').upper()
		if valor != 'S':
			print('\nEsta establecido el diccionario:')
			print(diccionario)
			return diccionario

def traducir(frase):
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
	return fraseTraducida


#Crear diccionario
diccionario=establecer_diccionario()

# Traducir una frase
frase = input('\nDame frase:')
frase_traducida = traducir(frase)
print('La frase traducida es:', frase_traducida)
