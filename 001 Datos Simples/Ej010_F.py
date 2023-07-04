# Ejercicios Datos Simples
# Day 1 - 30/05/2023

"""
Ejercicio 10
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer
venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben
calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada
payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y
muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.
"""

# SOLUCION PROFE

print('\n *** EJERCICIO 10 ***')

PESO_DOLLS = 75
PESO_PAYASOS = 112
num_dolls = int(input('Nº de muñecas: '))
num_payasos = int(input('Nº de payasos: '))

peso_pedido = ((num_dolls * PESO_DOLLS) + (num_payasos * PESO_PAYASOS)) / 1000

print('Peso pedido:', peso_pedido, 'kg')