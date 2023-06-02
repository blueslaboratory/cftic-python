# Ejercicios de Cadenas
# Day 2 - 31/05/2023

'''
Ejercicio 4
Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension
donde el prefijo es el código del país +34, y la extensión tiene dos dígitos
(por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de
teléfono con este formato y muestre por pantalla el número de teléfono sin el
prefijo y la extensión.
'''
print('\n *** EJERCICIO 4 ***')
telefono = input('Telefono (formato: prefix-nº-extension, e.g. +34-913146921-55): ')
# Elemento del primer numero sin prefijo: 4
# Elemento del ultimo numero sin extension: 13
print('Telefono sin extension: ', telefono[4:13])

