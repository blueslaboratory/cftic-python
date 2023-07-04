# Day 26 - 04/07/2023
# Ejercicios Librerias Estandar.docx
# Modulo Datetime

'''
Ejercicio 2
Escribe un programa que calcule la diferencia en días entre dos fechas.
'''

# SOLUCION PROFE

import datetime

fecha1 = datetime.date(2022, 1, 1)
fecha2 = datetime.date(2023, 1, 1)

diferencia = fecha2 - fecha1

print("Diferencia en days:", diferencia.days)