# Ejercicios de Bucles
# Day 6 - 06/06/2023

'''
Ejercicio 4
Escribir un programa que pida al usuario un número entero positivo y muestre por
pantalla la cuenta atrás desde ese número hasta cero separados por comas.
'''
import time

print('\n*** EJERCICIO 4 ***')

entero = int(input('Entero: '))
counter = 0
cuentaAtras = ''

while(entero<0):
	entero = int(input('Entero: '))


print('\nCuenta atras con timer: ')

while (counter <= entero):
	print(entero)
	# esto en realidad no es tiempo real porque no tiene en cuenta
	# el tiempo de procesamiento
	time.sleep(0.5)

	if (counter==entero):
		cuentaAtras += str(entero)
	else:
		cuentaAtras += (str(entero) +',')

	entero -= 1


print('\nCuenta atras:', cuentaAtras)




print('\n*** EJERCICIO 4 - SOLUCION PROFE ***')
numero = int(input("Dame numero entero positivo: "))

for i in range(numero, -1, -1):
	print(i, end='')
	if i:
		print(',', end='')
print()

print('\n*** EJERCICIO 4 - OTRA SOLUCION 1 ***')
#################################################################
#  Otra solucion
#################################################################
for i in range(numero, 0, -1):
	print(i, end=',')
print(0)

print('\n*** EJERCICIO 4 - OTRA SOLUCION 2 ***')
#################################################################
#  Otra solucion
#################################################################
for i in range(0, numero):
	print(numero-i, end=',')
print(0)