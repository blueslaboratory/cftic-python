# Ejercicios de Cadenas
# Day 2 - 31/05/2023


'''
Ejercicio 6
Escribir un programa que pida al usuario que introduzca una frase en la consola y
una vocal, y después muestre por pantalla la misma frase pero con la vocal
introducida en mayúscula.
'''

print('\n *** EJERCICIO 6 ***')

frase = input('Frase: ')
vocal = input('Vocal: ')

print(frase.replace(vocal, vocal.upper()))



print('\n *** EJERCICIO 6 - OTRA SOLUCION PROPUESTA PROFE ***')

frase = input("Frase: ")
vocal = input("Vocal: ")

partes = frase.split(vocal)
frase = vocal.upper().join(partes)

print("Frase modificada:" + frase)