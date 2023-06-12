# 09/06/2023 - Day 9
# Ejercicios de Funciones

'''
Ejercicio 3
Escribir una función que reciba un número entero positivo y devuelva su factorial.
'''

print('\n*** EJERCICIO 3 ***')


def factorialWhile(n):
	factorialCadena = str(n) + '!='
	factorial = 1

	while n > 1:
		factorial = factorial * n
		factorialCadena += str(n) + '*'
		# print(factorialCadena)
		n = n-1
	else:
		factorialCadena += '1' # str(n) = 1

	factorialCadena += f'={factorial}' # factorialCadena += '=' + str(factorial)

	print(factorialCadena)

	return factorial

def factorialFor(n):
	factorialCadena = str(n) + '!' + '='
	factorial = 1

	# Desde (1, n] empezando con n con un paso de -1
	for i in range (n, 1, -1):
		factorial = factorial * i
		factorialCadena += str(i) + '*'
		# print(factorialCadena)
		i = i - 1

	factorialCadena += str(i) +'=' +str(factorial)

	print(factorialCadena)

	return factorial


def factorialRecursivoString(n):
	if n == 0 or n == 1:
		return "1"

	stringOperacion = str(n) +"*" +factorialRecursivoString(n-1)
	return stringOperacion


def factorialRecursivo(n):
	if n==0: return 1
	if n==1: return 1

	return n*factorialRecursivo(n-1)


def factorialElegante(n):
	if n>0:
		return n*factorialElegante(n-1)
	return 1




n = int(input('Numero entero: '))

print('\nFactorial while:')
print(factorialWhile(n))

print('\nFactorial for:')
print(factorialFor(n))

print('\nFactorial recursivo:')
print(str(n) +'!' +'=' +factorialRecursivoString(n))
print(factorialRecursivo(n))

print('\nFactorial elegante:')
print(factorialElegante(n))




print('\n*** EJERCICIO 3 - SOLUCION PROFE ***')

def factorial(numero):
    resultado = 1
    for valor in range(1, numero+1):
        resultado *= valor
    return resultado
numero = 5

print('El factorial de', numero, 'es', factorial(numero))
