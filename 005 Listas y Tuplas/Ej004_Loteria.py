# Ejercicios de Listas y Tuplas
# Day 4 - 02/06/2023

'''
Ejercicio 4
Escribir un programa que pregunte al usuario los números ganadores de la lotería
primitiva, los almacene en una lista y los muestre por pantalla ordenados de
menor a mayor.
'''

print('\n*** EJERCICIO 4 ***')

numerosGanadores = []

# [0,6) --(i+1)--> [1,7)
for i in range(0,6):
	n = int(input('Numero ' +str(i+1) +': '))
	numerosGanadores.append(n)

complementario = int(input('Complementario: '))
reintegro = int(input('Reintegro: '))

numerosGanadores.sort()

# Recuerda: usando comas no hace falta castear a str()
print()
print('Numeros ganadores: ', numerosGanadores, sep='')
print('Numeros ganadores reversed: ', sorted(numerosGanadores, reverse=True), sep='')
print('Complementario: ', complementario, sep='')
print('Reintegro: ', reintegro, sep='')