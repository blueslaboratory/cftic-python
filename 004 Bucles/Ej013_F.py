# Ejercicios de Bucles
# Day 7 - 07/06/2023


'''
Ejercicio 13
Escribir un programa que muestre el eco de todo lo que el usuario introduzca
hasta que el usuario escriba “salir” que terminará.
'''

print('\n*** EJERCICIO 13 - SOLUCION PROFE ***')


texto = input("Dame texto: ").lower()

while texto != "salir":
    print(texto)
    texto = input("Dame texto: ").lower()

print("Has salido")