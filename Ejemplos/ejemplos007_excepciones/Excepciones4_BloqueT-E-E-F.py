# Day 8 - 08/06/2023

try:
    numero = int(input('Dame numero: '))
except ValueError as ve:
    print('Has introducido un valor no válido')
else:
    print('La operación se ha ejecutado bien')
finally:
    print('La operación se ha ejecutado')
