# Day 24 - 30/06/2023
# Ejercicios Lambda


# Nivel básico
'''
Ejercicio 2
Escribe una función lambda que tome una cadena de texto como parámetro y devuelva
la longitud de dicha cadena.
'''

cadena = 'xD'

lambda cadena: len(cadena)
longitud = lambda cadena: len(cadena)

print((lambda cadena: len(cadena))(cadena))
print(longitud(cadena))