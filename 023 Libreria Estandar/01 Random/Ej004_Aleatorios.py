# Day 25 - 03/07/2023
# Modulo Random

'''
Ejercicio 4
Escribe un programa que genere una lista de 5 números enteros aleatorios
entre 1 y 100, y luego muestre por pantalla la suma de todos los números
generados.
'''



import random


def generarAleatorios():
	return random.randint(1,100)


numeros = []

for i in range(5):
	numeros.append(generarAleatorios())


sumatorio = sum(numeros)

print('Lista generada:', numeros)
print('Suma de los numeros:', sumatorio)