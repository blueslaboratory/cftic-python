# Day 25 - 03/07/2023
# Modulo Random

'''
Ejercicio 5
Escribe una función que genere un código de verificación aleatorio de 6
dígitos. El código debe contener solo dígitos numéricos y no puede tener
dígitos repetidos.
'''

import random

# 6 digitos aleatorios no repetidos:
codigoList = random.sample(range(10), 6)
codigoString = ''.join(str(d) for d in codigoList)

print(codigoList)
print(codigoString)
