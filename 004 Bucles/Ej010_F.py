# Ejercicios de Bucles
# Day 7 - 07/06/2023


'''
Ejercicio 10
Escribir un programa que pida al usuario un número entero y muestre por pantalla
si es un número primo o no.
'''

print('\n*** EJERCICIO 10 - SOLUCION PROFE ***')


numero = int(input("Dame numero entero positivo: "))
i = 2

while numero % i != 0:
	i += 1
if i == numero:
	print(str(numero) + " es primo")
else:
	print(str(numero) + " no es primo")



print('\n*** EJERCICIO 10 - CHATGPT ***')
flag = True

if numero < 2:
	flag = False
# [2, int(numero^0.5)+1)
for i in range(2, int(numero**0.5) +1):
	if numero%i == 0:
		flag = False

print('Primo:', flag)