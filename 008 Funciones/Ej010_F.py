# 12/06/2023 - Day 10
# Ejercicios de Funciones

'''
Ejercicio 10
Escribir una función que convierta un número decimal en binario y otra que
convierta un número binario en decimal.
'''


print('\n*** EJERCICIO 10 - SOLUCION PROFE ***')

def mcd(n1, n2):
    resto = 0
    while (n2 > 0):
        resto = n2
        n2 = n1 % n2
        n1 = resto
    return resto

def mcm(n1, n2):
    if n1 > n2:
        grande = n1
    else:
        grande = n2
    while (grande % n1 != 0) or (grande % n2 != 0):
        grande += 1
    return grande

numero1 = int(input('Numero 1: '))
numero2 = int(input('Numero 2: '))

print()
print('El maximo comun divisor es: ' +str(mcd(numero1,numero2)))
print('El minimo comun multiplo es: ' +str(mcm(numero1,numero2)))