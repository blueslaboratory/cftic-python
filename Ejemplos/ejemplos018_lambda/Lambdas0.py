# Day 26 - 04/07/2023
# Lambdas.dox
# Ejemplos de uso: Nivel basico

print('\n*** Suma de dos numeros ***')
suma = lambda a, b: a + b
resultado = suma(3, 4)
print(resultado)  # Salida: 7


print('\n*** Verificar si un numero es par ***')
es_par = lambda x: x % 2 == 0
print(es_par(4))  # Salida: True
print(es_par(5))  # Salida: False


print('\n*** Elevar un numero al cuadrado ***')
cuadrado = lambda x: x ** 2
resultado = cuadrado(3)
print(resultado)  # Salida: 9


print('\n*** Obtener el primer caracter de una cadena ***')
primer_caracter = lambda cadena: cadena[0]
resultado = primer_caracter("Hola")
print(resultado)  # Salida: 'H'


print('\n*** Comprobar si una cadena contiene una subcadena ***')
contiene_subcadena = lambda cadena, subcadena: subcadena in cadena
print(contiene_subcadena("Hola mundo", "mundo"))  # Salida: True
print(contiene_subcadena("Hola mundo", "Python"))  # Salida: False