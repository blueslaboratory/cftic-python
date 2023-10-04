# Ejercicios de Diccionarios
# Day 6 - 06/06/2023

'''
Ejercicio 3
Escribir un programa que guarde en un diccionario los precios de las frutas de la
tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla
el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario
debe mostrar un mensaje informando de ello.

Fruta	    Precio
Plátano	    1.35
Manzana	    0.80
Pera	    0.85
Naranja	    0.70
'''

print('\n*** EJERCICIO 3 ***')

diccionarioFrutas = {'platano': 1.35,
                     'manzana': 0.80,
                     'pera': 0.85,
                     'naranja': 0.70}

fruta = input('Fruta: ')
masa = float(input('Masa (kg): '))

# No se puede usar, da una excepcion si NO existe la fruta, usar get()
# existeFrutaPrecio = diccionarioFrutas[fruta.lower()]
existeFrutaPrecio = diccionarioFrutas.get(fruta.lower())

# Miramos si la variable no esta vacia
# True: variable definida + cualquier valor, 1
# False: None, o variable vacia '', 0

# existeFrutaPrecio=''
# print(str(existeFrutaPrecio))

if(existeFrutaPrecio):
    precio = existeFrutaPrecio*masa
    print(fruta.capitalize(), 'precio:', str(precio), '€')
else:
    print('No existe la fruta en el diccionario')