# Day 24 - 30/06/2023
# Ejercicios Lambda


# Nivel básico
'''
Ejercicio 5
Escribe una función lambda que tome una lista de palabras como parámetro y
devuelva una nueva lista con las palabras que tengan más de 5 letras.
'''

listaPalabras = ['manzana', 'pera', 'mandarina', 'melon', 'tomate', 'naranja']

for p in listaPalabras:
	if len(p)>5:
		print(p)

# la primera p es lo que vas a hacer con la variable
lambda palabras: [p for p in palabras if len(p) > 5]
palabrasContarLetras = lambda palabras: [p for p in palabras if len(p) > 5]
palabrasContarLetras1 = lambda palabras: [p*2 for p in palabras if len(p) > 5]

print((lambda palabras: [p for p in palabras if len(p) > 5])(listaPalabras))
print(palabrasContarLetras(listaPalabras))
print(palabrasContarLetras1(listaPalabras))