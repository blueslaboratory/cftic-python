# 09/06/2023 - Day 9
# Ejercicios de Funciones

'''
Ejercicio 3
Escribir una función que reciba un número entero positivo y devuelva su factorial.
'''

print('\n*** EJERCICIO 3 ***')


def factorialString(n):
    if n == 0 or n == 1:
        return "1"

    stringOperacion = str(n) +"*" +factorialString(n-1)
    return stringOperacion


def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n*factorial(n-1)




n = int(input('Numero entero: '))
print('Factorial:', factorialString(n), '=', factorial(n))
