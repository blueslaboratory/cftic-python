# Ejercicios de Cadenas
# Day 2 - 31/05/2023

'''
Ejercicio 8
Escribir un programa que pregunte por consola el precio de un producto en euros con
dos decimales y muestre por pantalla el número de euros y el número de céntimos del
precio introducido.
'''
print('\n *** EJERCICIO 8 ***')
precio = input('Precio producto (€) con 2 decimales (e.g. 69.77€): ')
precioSplit = precio.split('.')

print('Euros:', precioSplit[0])
print('Centimos:', precioSplit[1])



print('\n *** EJERCICIO 8 - SOLUCION PROFE ***')
precio = input("Precio (con dos decimales): ")

euros = precio[:precio.find('.')]
centimos = precio[precio.find('.')+1:]

print("Euros:", euros)
print("Centimos:", centimos)