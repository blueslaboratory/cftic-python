# Ejercicios Datos Simples
# Day 1 - 30/05/2023

"""
Ejercicio 11
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés
al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te
añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo
la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario.
Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el
primer, segundo y tercer años. Redondear cada cantidad a dos decimales.
"""

print('\n *** EJERCICIO 11 ***')

INTERES = 0.04
capital = int(input('Capital: '))

capital_anio_1 = round((capital + capital * INTERES), 2)
print('Capital 1:', capital_anio_1)

capital_anio_2 = round((capital_anio_1 + capital_anio_1 * INTERES), 2)
print('Capital 2:', capital_anio_2)

capital_anio_3 = round((capital_anio_2 + capital_anio_2 * INTERES), 2)
print('Capital 3:', capital_anio_3)