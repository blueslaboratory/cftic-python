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


def dividir4(numerador, denominador):
	try:
		resultado = numerador / denominador
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

