# Day 24 - 30/06/2023
# Modulo Random

'''
Ejercicio 1
Escribe un programa que genere un número aleatorio entre 1 y 10, y le pida al
usuario que lo adivine. El programa debe indicar si el número ingresado por el
usuario es mayor, menor o igual al número generado.
'''


import random

numero_secreto = random.randint(1, 10)
adivinanza = int(input("Adivina el número (entre 1 y 10): "))


while(numero_secreto!= adivinanza):

	if adivinanza > numero_secreto:
		print("Demasiado alto")
	else:
		print("Demasiado bajo")

	adivinanza = int(input("Adivina el número (entre 1 y 10): "))


print("¡Adivinaste!")