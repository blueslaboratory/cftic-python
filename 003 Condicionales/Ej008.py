# Ejercicios de Condicionales
# Day 4 - 02/06/2023

'''
Ejercicio 8
En una determinada empresa, sus empleados son evaluados al final de cada año.
Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir
aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir
los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre
las cifras mencionadas. A continuación se muestra una tabla con los niveles
correspondientes a cada puntuación. La cantidad de dinero conseguida en cada
nivel es de 2.400€ multiplicada por la puntuación del nivel.

Nivel	        Puntuación
Inaceptable	    0.0
Aceptable	    0.4
Meritorio	    0.6 o más

Escribir un programa que lea la puntuación del usuario e indique su nivel de
rendimiento, así como la cantidad de dinero que recibirá el usuario.
'''

print('\n*** EJERCICIO 8 ***')

puntuacion = float(input('Puntuacion usuario: '))
nivelRendimiento = 'NO VALIDO'
flag = True

if (puntuacion == 0.0):
	nivelRendimiento = 'Inaceptable'
elif (puntuacion == 0.4):
	nivelRendimiento = 'Aceptable'
elif (puntuacion >= 0.6):
	nivelRendimiento = 'Meritorio'
else:
	flag = False


print('Nivel de rendimiento:', nivelRendimiento)

if (flag):
	print('Dinero conseguido:', 2400*puntuacion, '€')