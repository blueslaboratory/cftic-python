# Day 24 - 30/06/2023
# Ejercicios Lambda


# Nivel basico
'''
Ejercicio 1
Escribe una función lambda que reciba dos números como parámetros y devuelva
la suma de ambos.
'''

x = 3
y = 6

def sumar(x,y):
	return x+y


lambda x, y: x + y
suma = lambda x, y: x + y


print((lambda x, y: x + y)(x, y))
print(suma(x, y))


print(sumar(x, y))