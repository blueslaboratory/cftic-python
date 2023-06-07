# Ejercicios de Bucles
# Day 7 - 07/06/2023


'''
Ejercicio 12
Escribir un programa en el que se pregunte al usuario por una frase y una letra,
y muestre por pantalla el número de veces que aparece la letra en la frase.
'''

print('\n*** EJERCICIO 12 - SOLUCION PROFE ***')


frase = input("Dame frase: ")
letra = input("Dame letra: ")
contador = 0

for i in frase:
    if i == letra:
        contador += 1

print("Numero de coincidencias: "+str(contador))
