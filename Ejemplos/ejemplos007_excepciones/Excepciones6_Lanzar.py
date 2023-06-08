# Day 8 - 08/06/2023

# numero1 = int(input('Dame numero1: '))
# numero2 = int(input('Dame numero2: '))
# if(numero2==0):
#     raise ZeroDivisionError
# print('hola')
# division=numero1/numero2


try:
	numero1 = int(input('Dame numero1: '))
	numero2 = int(input('Dame numero2: '))

	if (numero2 == 0):
		raise ZeroDivisionError('Numero2 es cero')

	print('Hacemos la division')
	division = numero1 / numero2

except ValueError:
	# Si se produce una excepcion de tipo ValueError, imprime un mensaje de error
	print('Has introducido un valor no válido - ValueError')
	# Ademas, genera una excepcion ZeroDivisionError
	raise ZeroDivisionError('Dato introducido no válido')

except ZeroDivisionError as zde:
	# Si se produce una excepcion ZeroDivisionError, la eleva para que sea manejada en un nivel superior
	raise zde

except Exception as e:
	# Si se produce cualquier otra excepcion, genera una excepcion ZeroDivisionError
	raise ZeroDivisionError('Error general')

