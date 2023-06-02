# Ejercicios de Condicionales
# Day 4 - 02/06/2023

'''
Ejercicio 5
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos
ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte
al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario
tiene que tributar o no.
'''

print('\n*** EJERCICIO 5 ***')

edad = int(input('Edad: '))
ingresos = float(input('Ingresos mensuales: '))
tributa = False

if(edad>=16 and ingresos >= 1000):
	tributa = True

print('Tributar: ', tributa)

