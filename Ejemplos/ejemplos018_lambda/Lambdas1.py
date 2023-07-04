# Day 26 - 04/07/2023
# Lambdas.dox
# Ejemplos de uso: Nivel intermedio


# Ordenar una lista de objetos por un atributo especifico
class Objeto:
	def __init__(self, atributo):
		self.atributo = atributo

	def __repr__(self):
		return f"Objeto({self.atributo})"


print('\n*** Ordenar objetos ***')
objetos = [Objeto(3), Objeto(1), Objeto(2)] # Lista de objetos
ordenados = sorted(objetos, key=lambda x: x.atributo)
print(ordenados)


# Filtrar elementos de una lista que cumplan cierta condicion
print('\n*** Filtra pares ***')
numeros = [1,2,3,4,5,6,7,8,9]  # Lista de números
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)


# Mapear una funcion a una lista de elementos:
print('\n*** Duplicar cada numero ***')
numeros = [1,2,3,4,5,6,7,8,9]  # Lista de números
duplicados = list(map(lambda x: x * 2, numeros))
print(duplicados)


# Realizar operaciones aritmeticas complejas
print('\n*** Operacion matematica ***')
operacion = lambda x, y: (x + y) * (x - y)  # (x + y) * (x - y)
resultado = operacion(3, 2)  # Aplicando la lambda a los valores 3 y 2
print(resultado)


# Definir funciones de orden superior
print('\n*** Funciones de orden superior ***')
def operador_matematico(operacion):
	return lambda x, y: operacion(x, y)

suma = operador_matematico(lambda x, y: x + y)
resta = operador_matematico(lambda x, y: x - y)

resultado_suma = suma(3, 2)  # 5
resultado_resta = resta(3, 2)  # 1

print(resultado_suma)
print(resultado_resta)