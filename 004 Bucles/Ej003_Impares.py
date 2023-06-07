# Ejercicios de Bucles
# Day 6 - 06/06/2023

'''
Ejercicio 3
Escribir un programa que pida al usuario un número entero positivo y muestre por
pantalla todos los números impares desde 1 hasta ese número separados por comas.
'''

print('\n*** EJERCICIO 3 ***')

entero = int(input('Entero: '))
counter = 1

impares = ''

while(counter <= entero):

	if(counter%2 != 0):
		if(counter != entero):
			impares += (str(counter) + ', ')
		else:
			impares += str(counter)

	counter += 1

print(impares)




print('\n*** EJERCICIO 3 - SOLUCION PROFE ***')

numero = int(input("Dame numero entero positivo: "))

for i in range(1, numero+1, 2):
	print(i, end=",")
print()


print('\n*** EJERCICIO 3 - OTRA SOLUCION 1 ***')
################################################
# Otra solucion
################################################
numero = int(input("Dame numero entero positivo: "))

for i in range(numero+1):
	if i%2 != 0:
		print(i, end=",")
print()


print('\n*** EJERCICIO 3 - OTRA SOLUCION 2 ***')
################################################
# Otra solucion
################################################
numero = int(input("Dame numero entero positivo: "))

contador=1
while contador <= numero:
	if contador%2 != 0:
		print(contador, end=",")
	contador += 1
print()


print('\n*** EJERCICIO 3 - OTRA SOLUCION 3 ***')
################################################
# Otra solucion
################################################
numero = int(input("Dame numero entero positivo: "))

for i in range(numero+1):
	if i%2: #0 (false)
		print(i, end=",")
print()