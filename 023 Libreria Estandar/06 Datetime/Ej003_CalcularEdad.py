# Day 26 - 04/07/2023
# Ejercicios Librerias Estandar.docx
# Modulo Datetime

'''
Ejercicio 3
Escribe un programa que calcule la edad de una persona dada su fecha de nacimiento.
'''

# CHATGPT

from datetime import datetime


def calcular_edad(fecha_nacimiento):

    fecha_actual = datetime.now().date()
    edad = fecha_actual.year - fecha_nacimiento.year

    if fecha_actual.month < fecha_nacimiento.month:
        edad -= 1
    elif fecha_actual.month == fecha_nacimiento.month and fecha_actual.day < fecha_nacimiento.day:
        edad -= 1

    return edad


# Pedir la fecha de nacimiento al usuario: 21/06/1993
fecha_str = input("Ingrese su fecha de nacimiento (formato: DD/MM/AAAA): ")

# Convertir la cadena de texto a un objeto de fecha
fecha_nacimiento = datetime.strptime(fecha_str, "%d/%m/%Y").date()

# Calcular la edad
edad = calcular_edad(fecha_nacimiento)

# Imprimir el resultado
print("Su edad es:", edad)