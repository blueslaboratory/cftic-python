# Ejercicios Datos Simples
# Day 1 - 30/05/2023

"""
Ejercicio 12
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es del día tiene un
descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas
que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan,
el descuento que se le hace por no ser fresca y el coste final total.
"""

print('\n *** EJERCICIO 12 ***')

PRECIO_NORMAL = 3.49
DESCUENTO = 0.6

num_barras_no_dia = int(input('Nº barras vendidas que no son del dia: '))

costeNormal = round(num_barras_no_dia * PRECIO_NORMAL, 2)
print('Coste normal:', costeNormal)

descuento = round(num_barras_no_dia * DESCUENTO, 2)
print('Descuento:', descuento)

costeFinal = costeNormal - descuento
print('Coste Final:', costeFinal)

