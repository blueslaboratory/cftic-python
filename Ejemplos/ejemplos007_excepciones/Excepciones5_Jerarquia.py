# Day 8 - 08/06/2023

try:
    numero = int(input('Dame numero: '))
    division=numero/0
except ValueError:
    print('Has introducido un valor no válido - ValueError')
except Exception as e:
    print('Mensaje de excepción:',e)