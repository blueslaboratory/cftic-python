# Day 8 - 08/06/2023

print('\n*** DIVIDIR 0 ***')
def dividir0(numerador, denominador):
	return numerador/denominador

try:
	n1 = int(input('Dame n1: '))
	n2 = int(input('Dame n2: '))

	dividir0(n1, n2)

except ZeroDivisionError:
	print('Se ha producido una division por cero')




# OTRA FORMA DE HACERLO 1
print('\n*** DIVIDIR 1 ***')
def dividir1 (numerador, denominador):
	try:
		return numerador/denominador
	except ZeroDivisionError:
		return 'Se ha intentado dividir por cero'

n1 = int(input('Dame n1: '))
n2 = int(input('Dame n2: '))

print('Resultado: ', dividir1(n1, n2))




# OTRA FORMA DE HACERLO 2
print('\n*** DIVIDIR 2 ***')
def dividir2 (numerador, denominador):
	try:
		resultado = numerador/denominador
	except StopIteration:
		return 'Se ha intentado dividir por cero'
	finally:
		return resultado

try:
	n1 = int(input('Dame n1: '))
	n2 = int(input('Dame n2: '))

	print('Resultado: ', dividir2(n1, n2))

except ZeroDivisionError:
	print('ZeroDivisionError: Se ha intentado dividir por cero')
except UnboundLocalError:
	print('UnboundLocalError: Resultado no disponible')




# OTRA FORMA DE HACERLO 3
print('\n*** DIVIDIR 3 ***')
def dividir3 (numerador, denominador):
	try:
		resultado = numerador/denominador
		return resultado
	except ZeroDivisionError:
		return 'Se ha intentado dividir por cero'

try:
	n1 = int(input('Dame n1: '))
	n2 = int(input('Dame n2: '))

	print('Resultado: ', dividir2(n1, n2))

except Exception:
	print('Excepcion General')

# except a secas es equivalente a except BaseException
except:
	print('Excepcion General Abreviada')




# PEDIR UN VALOR 0
print('\n*** PEDIR UN VALOR 0 ***')

def pedirNumero():
	while True:
		try:
			# me piro de esta funcion cuando se ejecuta este return
			# me da igual lo que este pasando
			resultado = int(input('Dame numero: '))
			return resultado
		except ValueError:
			print('Ha introducido un dato erroneo')

def dividir4 (numerador, denominador):
	try:
		resultado = numerador/denominador
		return resultado
	except ZeroDivisionError:
		return 'Se ha intentado dividir por cero'


try:
	n1 = pedirNumero()
	n2 = pedirNumero()

	print('Resultado: ', dividir4(n1, n2))

except Exception:
	print('Excepcion General')

# except a secas es equivalente a except BaseException
except:
	print('Excepcion General Abreviada')


