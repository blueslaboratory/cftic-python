# Day 0 - 30/05/2023

"""
Pycharm
CTRL + ALT + S: Cambiar el interprete de Python
CTRL + SHIFT + F10: Runear el codigo
"""


# Hello World
mensaje='hola mundo'

print ('*** HELLO WORLD ***')
print (mensaje)


"""

This is a multi-line comment with docstrings

print("Hello world")
print("Hello universe")
print("Hello everyone")

"""



# Numeros
n0 = 33
n1 = 42
n2 = 7


# print solo saca cadenas, pero n0 sigue siendo un numero
print (n0)


# Recoger tus datos (input solo recoge strings)
print ('\n*** INPUTS ***')
myStringInput = input ('Dame input (String): ')
print (myStringInput)

myNumberInput = input ('Dame input (Number): ')
print (myNumberInput)


# Multiplicar la cadena myNumberInput n2 veces: concatenar
n3 = n2 * myNumberInput 
print (n3)


# Conseguir la multiplicacion: castear
n3 = n2 * int(myNumberInput)


# Print solo puede imprimir Strings, hay que castear los numeros a Strings:
print ('\n*** MULTIPLICACION CASTEANDO ***')
print (str(n2) +'*' +str(myNumberInput) +' = ' +str(n3))


# Division no entera: float
print ('\n*** DIVISION FLOTANTE ***')
print (str(n0) +'/' +str(n1) +' = ' +str(n0/n1))
print (n0/n1)


# Numeros complejos
print ('\n*** NUMEROS COMPLEJOS ***')
nComplex = complex (int(input('Parte real numero complejo: ')),4)
print(nComplex)


# Booleanos
# Palabras reservadas: and (&), or (|)
# Se recomienda facilidad de lectura: and y or
print ('\n*** BOOLEANOS ***')
true = True

print ('true: no es palabra reservada')
print (str(true) + ': es palabra reservada')

b0 = False
b1 = True

b2 = b0 and b1 
print(b2)
b2 = b0 & b1
print(b2)


# Separador
print ('\n*** SEPARADOR, END ***')
print('Hola', 'Mundo', 'Cruel', sep='#')
print('Hola', 'Mundo', 'Feliz', end='&\n')
