# Ejercicios de Bucles
# Day 6 - 06/06/2023

'''
Ejercicio 5
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés
anual y el número de años, y muestre por pantalla el capital obtenido en la
inversión cada año que dura la inversión.

capitalFinal = cantidadInvertir*(1+interesAnual/100)**yearInversion
'''

print('*** EJERCICIO 5 ***')

cantidad = float(input('Cantidad a invertir (₿): '))
interesAnual = float(input('Interes anual (%):  '))
years = int(input('Years: '))

# [1-6)
print('\nYear[i]: capitalObtenido')
for i in range(1, years+1):
	capitalObtenido = cantidad*(1+interesAnual/100)**i
	print(f'Year[{i}]: {capitalObtenido:.2f}')