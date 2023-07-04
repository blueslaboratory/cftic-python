# Day 26 - 04/07/2023
# Lambdas.dox
# Ejemplos de uso: Nivel avanzado



# 1. Ordenar una lista de objetos utilizando múltiples criterios de clasificación
class Objeto:
	def __init__(self, atributo1, atributo2):
		self.atributo1 = atributo1
		self.atributo2 = atributo2


	def __repr__(self):
		return f"Objeto({self.atributo1})({self.atributo2})"


print('\n*** Ordenar objetos por 2 atributos ***')
objetos = [Objeto(1, 2), Objeto(2, 4), Objeto(1, 3)]  # Lista de objetos
ordenados = sorted(objetos, key=lambda x: (x.atributo1, x.atributo2))
print(ordenados)



# 2. Crear una función generadora infinita utilizando una lambda:
print('\n*** Funcion generadora infinita ***')
generador_infinito = lambda: (x for x in range(1, float('inf')))
print(generador_infinito)



# 3. Implementar una función de memorización utilizando una lambda:
# función de memorización que almacena en caché los resultados de llamadas anteriores.
print('\n*** Funcion de memorizacion ***')
memoize = lambda f: (lambda *args: memoize(f)(*args)) if isinstance(f, type(lambda:0)) else f
print(memoize)



# 4. Crear una función curried utilizando una lambda:
# curried permite aplicar parcialmente los argumentos de una función.
print('\n*** Crear una funcion curried ***')
curry = lambda f: (lambda x: curry(lambda *args: f(x, *args))) if f.__code__.co_argcount > 1 else f
print(curry)



# 5. Implementar un decorador personalizado utilizando una lambda:
print('\n*** Decorador personalizado ***')

def custom_decorator(arg):
	return lambda func: lambda *args, **kwargs: arg + func(*args, **kwargs)

@custom_decorator(10)
def my_function(x):
	return x * 2

resultado = my_function(5)  # 20
print(resultado)