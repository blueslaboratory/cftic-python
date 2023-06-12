# Day 10 - 12/06/2023

'''
Ejercicio 4 Suma de números
Escribe una función llamada sumar_numeros que reciba una lista de números y
devuelva su suma. La función debe manejar la excepción en caso de que la lista
contenga elementos que no sean numéricos y devolver un mensaje de error adecuado.
'''

print('\n*** EJERCICIO 4 ***')

def sumarNumeros(listaString):
	try:
		# mapear la lista a un conjunto de floats
		listFloat = list(map(float, listaString))
		suma = sum(listFloat)
		return suma
	except ValueError:
		return 'ValueError - Valor no numerico'



# lista = [0,1,2,3,4,5,6,7,8,9,10]
lista = []

print('Introduzca una lista (e.g. 0,1,2,3,4,5,6,7,8,9.9,10)')
print('Lista no valida (e.g. 0,1,2,hola,4,5,cara,7,8,bola,10)')

listaString = input('> ').split(',')

# Sumar los 100 primeros numeros: [0, 101)
# for i in range(0, 101, 1):
# 	lista.append(int(i))

print('Resultado:', sumarNumeros(listaString))




print('\n*** EJERCICIO 4 - SOLUCION PROFE ***')

def sumar_numeros(lista):
  try:
     suma = sum(lista)
     return suma
  except TypeError:
      return "¡Error: La lista contiene elementos no numéricos!" # Ejemplo de uso numeros = [1, 2, 3, 4, 5]
numeros = [1, 2, 3, 4, 5]
resultado = sumar_numeros(numeros)
print(resultado)