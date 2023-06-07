# Ejercicios de Bucles
# Day 7 - 07/06/2023


'''
Ejercicio 9
Escribir un programa que almacene la cadena de caracteres contraseña en una
variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña
correcta.
'''

print('\n*** EJERCICIO 9 - SOLUCION PROFE ***')

contra = "alguna"
password = ""

while contra != password:
    password = input("Dame contraseña: ").lower()

print("Contraseña correcta")