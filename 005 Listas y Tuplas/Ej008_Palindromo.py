# Ejercicios de Listas y Tuplas
# Day 7 - 07/06/2023

'''
Ejercicio 8
Escribir un programa que pida al usuario una palabra y muestre por pantalla si
es un palíndromo.
'''

print('\n*** EJERCICIO 8 ***')

palabra = input('Palabra: ')
palindromo = ''.join(reversed(palabra))
flag = False

if (palabra == palindromo):
	flag = True

print()
print('Palabra introducida:', palabra)
print('Palabra revertida:', palindromo)
print('Palindromos:', flag)




print('\n*** EJERCICIO 8 - SOLUCION PROFE ***')

palabra = input("Deme una palabra: ")

letras = list(palabra)
letrasReves = list(palabra)

letrasReves.reverse()

if letras == letrasReves:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")