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

# En la vida real se tributa por tramos, el tipo impositivo te va por tramos

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
elif(rentaAnual>=60000):
	tipo = 45

print('Tipo impositivo:', tipo, '%')




print('\n*** EJERCICIO 7 - SOLUCION PROFE ***')

renta = int(input("Dame renta anual:"))
tipo = 0

if renta < 10000:
	tipo = 5
elif renta < 20000:
	tipo = 15
elif renta < 35000:
	tipo = 20
elif renta < 60000:
	tipo = 30
else:
	tipo = 45

print("El tipo es " + str(tipo))
print("Tienes que pagar ", renta*tipo/100, "€", sep='')