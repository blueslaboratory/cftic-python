# Day 26 - 04/07/2023
# Ejercicios Librerias Estandar.docx
# Modulo Datetime

'''
Ejercicio 4
Escribe un programa que verifique si un año dado es un año bisiesto.
* Un año es bisiesto si es divisible por 4.
* Pero los años que son divisibles por 100 no son bisiestos,
  a menos que también sean divisibles por 400.
'''

# CHATGPT


es_bisiesto = lambda year: year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# Pedir al usuario que ingrese un año: 1600, 2024, 999
y = int(input("Ingrese un year: "))

# Verificar si el año es bisiesto
print(y, "es un year bisiesto:", es_bisiesto(y))