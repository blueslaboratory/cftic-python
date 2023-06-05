# Day 5 - 05/06/2023
# Funciones en Python.docx

print('\n*** Funciones incorporadas ***')
print('Len toma como parametros, inputs: colecciones e iterables')

print(len('a'))
print(len((2,3)))
print(len({1,2,3,}))
print(len([1,2,3,4]))



print('\n*** Funciones definidas por el usuario ***')
def suma(a, b):
    return a + b

resultado = suma(1, 2)
print('Funcion suma: ', resultado)



print('\n*** Funciones de biblioteca (modulos) ***')
import math

raiz_cuadrada = math.sqrt(16)
print(raiz_cuadrada)



print('\n*** Funciones lambda (funciones anonimas) ***')
'''
Las funciones lambda son funciones pequeñas y anónimas que se definen sin un 
nombre utilizando la palabra clave lambda. Estas funciones suelen utilizarse 
cuando se requiere una función rápida y sencilla sin necesidad de definirla por 
separado.
'''
# Suelen ser sentencias de 2 lineas a lo sumo
doble = lambda x: x*2
resultado = doble(5)
print(resultado)