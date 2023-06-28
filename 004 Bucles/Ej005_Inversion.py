# Ejercicios de Bucles
# Day 6 - 06/06/2023

'''
Ejercicio 5
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés
anual y el número de años, y muestre por pantalla el capital obtenido en la
inversión cada año que dura la inversión.

capitalFinal = cantidadInvertir*(1+interesAnual/100)**yearInversion
'''

print('\n*** EJERCICIO 5 ***')

cantidad = float(input('Cantidad a invertir (₿): '))
interesAnual = float(input('Interes anual (%):  '))
years = int(input('Years: '))


print('Interes compuesto')
print('\nYear[i]: capitalObtenido')
# [1, years+1)
for i in range(1, years+1):
	capitalObtenido = cantidad*(1+interesAnual/100)**i
	print(f'Year[{i}]: {capitalObtenido:.2f}')



print('\n*** EJERCICIO 5 - SOLUCION PROFE ***')
capital = float(input("Dame capital a invertir: "))
interes = int(input("Dame interes: "))
anios = int(input("Dame anios: "))

for i in range(anios):
	capital *= (1+interes/100)
	print("Año " +str(i) +":" +str(round(capital, 2)))