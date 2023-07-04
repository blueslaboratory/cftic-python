# Day 26 - 04/07/2023
# Librerías Estándar.docx
# Modulo Random

import random


print('\n*** 1. Generacion de numeros aleatorios ***')
print(random.randint(0, 10)) # [1,10]
print(random.uniform(0.0, 10.0)) # [0.0, 10.0]


print('\n*** 2. Seleccion aleatoria de elementos ***')
print(random.choice(["manzana", "platano", "naranja"])) # [1,10]
# [1, 49] dame una muestra aleatoria de 7 valores
print(random.sample(range(1, 50), 7))


print('\n*** 3. Shuffle ***')
lista = [1, 2, 3, 4, 5]
random.shuffle(lista)
print(lista)


print('\n*** 4. Numeros pseudoaleatorios ***')
# Cada vez que se ejecuta el código, se obtendrán los mismos números
# pseudoaleatorios en el mismo orden debido a que la semilla se ha fijado en 42.
random.seed(42)

# Generar 5 numeros pseudoaleatorios
for i in range(5):
	numero_aleatorio = random.random() # [0.0, 1.0)
	print(numero_aleatorio)