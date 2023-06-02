# Ejercicios de Condicionales
# Day 4 - 02/06/2023


'''
Ejercicio 7
Los tramos impositivos para la declaración de la renta en un determinado país son
los siguientes:

Renta	                    Tipo impositivo
Menos de 10000€	            5%
Entre 10000€ y 20000€	    15%
Entre 20000€ y 35000€	    20%
Entre 35000€ y 60000€	    30%
Más de 60000€	            45%

Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla
el tipo impositivo que le corresponde.
'''

print('\n*** EJERCICIO 7 ***')

rentaAnual = float(input('Renta anual: '))
tipo = 5

if(rentaAnual<10000):
	tipo = 5
elif(rentaAnual>=10000 and rentaAnual<20000):
	tipo = 15
elif(rentaAnual>=20000 and rentaAnual<35000):
	tipo = 20
elif(rentaAnual>=35000 and rentaAnual<60000):
	tipo = 30
if(rentaAnual>=60000):
	tipo = 45

print('Tipo impositivo:', tipo, '%')