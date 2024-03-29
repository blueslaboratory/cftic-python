# Ejercicios de Diccionarios
# Day 5 - 05/06/2023

'''
Ejercicio 1
Escribir un programa que guarde en una variable el diccionario:
{'Euro':'€', 'Dollar':'$', 'Yen':'¥'},
pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si
la divisa no está en el diccionario.
'''

print('\n*** EJERCICIO 1 ***')

diccionarioDivisas = {'Euro':'€',
                      'Dollar':'$',
                      'Yen':'¥'}


divisa = input('Buscar divisa: ')


# No se puede usar, da una excepcion si NO existe la divisa, usar get()
simbolo = diccionarioDivisas[divisa.lower().capitalize()]
# simbolo = diccionarioDivisas.get(divisa.lower().capitalize())

# Miramos si la variable no esta vacia
# True: variable definida + cualquier valor, 1
# False: None, o variable vacia '', 0

# simbolo=''
# print(str(simbolo))

if (simbolo):
    print('Existe:', simbolo)
else:
    print('No existe', divisa)