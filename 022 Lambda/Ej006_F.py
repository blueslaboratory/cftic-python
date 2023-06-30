# Day 24 - 30/06/2023
# Ejercicios Lambda


# Nivel intermedio
'''
Ejercicio 6
Escribe una función lambda que reciba una lista de números como parámetro y
devuelva la suma de todos los números impares elevados al cuadrado.
'''

listaNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]



# Comprimida
lambda numeros: sum(map(lambda x: x**2, filter(lambda x: x % 2 != 0, numeros)))
sumaNumeros = lambda numeros: sum(map(lambda x: x**2, filter(lambda x: x % 2 != 0, numeros)))



# Expandida:
# Filtrar los numeros impares
numeros_impares = filter(lambda x: x % 2 != 0, listaNumeros)

# Elevar al cuadrado los numeros impares
numeros_cuadrados = map(lambda x: x ** 2, numeros_impares)

# Calcular la suma de los numeros al cuadrado
resultado = sum(numeros_cuadrados)



print(sumaNumeros(listaNumeros))
print(resultado)