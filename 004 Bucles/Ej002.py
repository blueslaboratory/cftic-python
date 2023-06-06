# Ejercicios de Bucles
# Day 6 - 06/06/2023

'''
Ejercicio 2
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos
los años que ha cumplido (desde 1 hasta su edad).
'''

print('*** EJERCICIO 2 ***')

edad = int(input('Edad: '))

cumplidos = 1

while (cumplidos <= edad):
	print('Has cumplido', cumplidos, 'years')
	cumplidos += 1