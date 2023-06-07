# Ejercicios de Bucles
# Day 6 - 06/06/2023


'''
Ejercicio 8
Escribir un programa que pida al usuario un número entero y muestre por pantalla
un triángulo rectángulo como el de más abajo.

1
3 1
5 3 1
7 5 3 1
9 7 5 3 1
'''

print('\n*** EJERCICIO 8 - SOLUCION PROFE ***')

numero = int(input("Dame numero entero positivo: "))

# impares
for i in range(1, numero+1, 2):
	# cuenta atras
	for j in range(i, 0, -2):
		print(str(j), end=" ")
	print("")
