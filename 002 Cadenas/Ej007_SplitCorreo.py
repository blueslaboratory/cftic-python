# Ejercicios de Cadenas
# Day 2 - 31/05/2023


'''
Ejercicio 7
Escribir un programa que pregunte el correo electrónico del usuario en la consola y
muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante
de la arroba @) pero con dominio ceu.es.
'''

print('\n *** EJERCICIO 7 ***')

correo = input('Correo (e.g. blueslaboratory@labs.com): ')
correoList = correo.split('@')

print(correoList[0] +'@' +'ceu.es')



print('\n *** EJERCICIO 7 - SOLUCION PROFE***')

correo = input("Correo:")

correo_sin_dominio = correo[:correo.find('@')]
correo = correo_sin_dominio + "@ceu.es"

print("Correo:" + correo)