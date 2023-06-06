# Ejercicios de Bucles
# Day 6 - 06/06/2023

'''
Ejercicio 4
Escribir un programa que pida al usuario un número entero positivo y muestre por
pantalla la cuenta atrás desde ese número hasta cero separados por comas.
'''
import time

print('*** EJERCICIO 4 ***')

entero = int(input('Entero: '))
counter = 0
cuentaAtras = ''

while(entero<0):
	entero = int(input('Entero: '))


print('\nCuenta atras con timer: ')

while (counter <= entero):
	print(entero)
	time.sleep(0.5)

	if (counter==entero):
		cuentaAtras += str(entero)
	else:
		cuentaAtras += (str(entero) +',')

	entero -= 1


print('\nCuenta atras:', cuentaAtras)