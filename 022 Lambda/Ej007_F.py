# Day 24 - 30/06/2023
# Ejercicios Lambda


# Nivel intermedio
'''
Ejercicio 7
Escribe una función lambda que tome una lista de palabras como parámetro y
devuelva una nueva lista con las palabras que comiencen con la letra 'A' y
tengan más de 3 letras.
'''

palabras = ["Hola", "Adios", "Amigo", "Casa", "Avion"]



# Comprimida
lambda palabras: list(filter(lambda palabra: len(palabra) > 3 and palabra[0] == 'A', palabras))
lambdaPalabras = lambda palabras: list(filter(lambda palabra: len(palabra) > 3 and palabra[0] == 'A', palabras))



# Expandida:
# Filtrar las palabras con longitud mayor a 3 y que empiecen con 'A'
palabras_filtradas = filter(lambda palabra: len(palabra) > 3 and palabra[0] == 'A', palabras)

# Convertir el objeto filter en una lista
resultado = list(palabras_filtradas)



print(lambdaPalabras(palabras))
print(resultado)