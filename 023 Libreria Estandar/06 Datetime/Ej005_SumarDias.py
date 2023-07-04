# Day 26 - 04/07/2023
# Ejercicios Librerias Estandar.docx
# Modulo Datetime

'''
Ejercicio 5
Escribe un programa que sume una cantidad específica de días a una fecha dada.
'''

# SOLUCION PROFE


import datetime


def sumar_dias(fecha, dias):
    nueva_fecha = fecha + datetime.timedelta(days=dias)
    return nueva_fecha


fecha_inicial = datetime.date(2022, 1, 1)
dias_a_sumar = 30

fecha_resultante = sumar_dias(fecha_inicial, dias_a_sumar)
print("Fecha resultante:", fecha_resultante)