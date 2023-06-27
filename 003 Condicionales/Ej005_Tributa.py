# Ejercicios de Condicionales
# Day 4 - 02/06/2023

'''
Ejercicio 5
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos
ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte
al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario
tiene que tributar o no.
'''

print('\n*** EJERCICIO 5 ***')

edad = int(input('Edad: '))
ingresos = float(input('Ingresos mensuales: '))
tributa = False


# si ya no es >= 16 años, no evalua la siguiente condicion
# esto se conoce como operador de cortocircuito.

# Operadores de cortocircuito:
# - and
# - or
# Operadores de no cortocircuito:
# - &
# - |

if(edad>=16 and ingresos>=1000):
	tributa = True

print('Tributar:', tributa)




# El operador de cortocircuito and hace que el codigo anterior y este
# sean equivalentes

print('\n*** EJERCICIO 5 - OTRA SOLUCION ***')

EDAD = 16
INGRESO = 1000

persona = int(input('Por favor, introduce tu edad: '))

if persona >= EDAD:

	nomina = float(input('Introduce tu ingreso mensual: '))

	if nomina > INGRESO:
		print('Este usuario tiene que tributar')
	else:
		print('Este usuario no llega al mínimo ingreso')

else:
	print('Este usuario no tiene que tributar')




print('\n*** OPERADOR DE CORTOCIRCUITO: AND ***')

# si pones menor que 15 ya NO EVALUA la siguiente condicion
if int(input("Dame edad :"))>15 and int(input("Dame ingresos mensuales :"))>1000:
	print("Tienes que tributar")
else:
	print("No tienes que tributar")

# si pones menor que 15 ya SI EVALUA la siguiente condicion
print('\n*** OPERADOR: & ***')
if int(input("Dame edad :"))>15 & int(input("Dame ingresos mensuales :"))>1000:
	print("Tienes que tributar")
else:
	print("No tienes que tributar")