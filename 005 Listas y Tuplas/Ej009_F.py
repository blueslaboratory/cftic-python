# Ejercicios de Listas y Tuplas
# Day 4 - 02/06/2023

'''
Ejercicio 9
Escribir un programa que pida al usuario una palabra y muestre por pantalla el
número de veces que contiene cada vocal.
'''

print('\n*** EJERCICIO 9 - SOLUCION PROFE ***')

n_a, n_e, n_i, n_o, n_u = 0,0,0,0,0;

palabra = input("Deme una palabra: ").lower()
letras = list(palabra)

for i in letras:
    if i == 'a':
        n_a += 1
    if i == 'e':
        n_e += 1
    if i == 'i':
        n_i += 1
    if i == 'o':
        n_o += 1
    if i == 'u':
        n_u += 1

print()
print("Número de letras a: "+str(n_a))
print("Número de letras e: "+str(n_e))
print("Número de letras i: "+str(n_i))
print("Número de letras o: "+str(n_o))
print("Número de letras u: "+str(n_u))