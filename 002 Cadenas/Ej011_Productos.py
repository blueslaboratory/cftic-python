# Ejercicios de Cadenas
# Day 2 - 31/05/2023

'''
Ejercicio 11
Escribir un programa que pregunte el nombre el un producto, su precio y un número de
unidades y muestre por pantalla una cadena con el nombre del producto seguido de su:
--> precio unitario con 6 dígitos enteros y 2 decimales,
--> número de unidades con 3 dígitos y
--> coste total con 8 dígitos enteros y 2 decimales.
'''

print('\n *** EJERCICIO 11 ***')

producto = input('Nombre del producto: ')
precioUnitario = float(input('Precio unitario: '))
unidades = int(input('Unidades: '))
costeTotal = precioUnitario * unidades


cadenaFinal = f'\nProducto: {producto}\n'

cadenaFinal += f'\nPrecio unitario con 0s: {precioUnitario:09.2f}\n'
cadenaFinal += f'Precio unitario: {precioUnitario:9.2f}\n'

cadenaFinal += f'\nUnidades con 0s: {unidades:03d}\n'
cadenaFinal += f'Unidades: {unidades:3d}\n'

cadenaFinal += f'\nCoste total con 0s: {costeTotal:011.2f}\n'
cadenaFinal += f'Coste total: {costeTotal:11.2f}'


print(cadenaFinal)