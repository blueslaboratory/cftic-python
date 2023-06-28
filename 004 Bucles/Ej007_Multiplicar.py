# Ejercicios de Bucles
# Day 6 - 06/06/2023


'''
Ejercicio 7
Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
'''

print('\n*** EJERCICIO 7 ***')

numero = int(input('Numero: '))


print('\nTabla de multiplicar del', numero)
for i in range(1, 10+1):
	print(numero, '*', i, '=', numero*i)



# Todas las tablas de multiplicar
print('\n*** EJERCICIO 7 - SOLUCION PROFE ***')

for i in range(1, 11):
	print("\nTabla del " + str(i))
	for j in range(1, 11):
		print(i, '*', j, '=', i * j)