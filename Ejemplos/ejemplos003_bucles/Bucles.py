# 01/06/2023

print('\n*** for del 0-9: 10 numeros ***')
for item in range(10):
	print(item)


print('\n*** for del 6-9: 4 numeros ***')
for item in range(6,10):
	print(item)


print('\n*** for del 1 al 5 saltando cada 2 (inicio, fin, salto) ***')
for item in range(1,5,2):
	print(item)


# gomenasai
print('\n*** Imprimir una cadena en vertical como una lista ***')
for item in 'ごめんなさい':
	print(item)


print('\n*** Imprimir una lista ***')
lista = [1, 4, 'hola', 5]
for item in lista:
	print(item)


print('\n*** for con un else ***')
lista2 = []
for item in lista2:
	print(item)
else:
	print('lista vacia')


print('\n*** for con un continue ***')
for item in range(10):
	if item%2 == 0:
		# dejar de hacer las sentencias de a continuacion, no hacemos el print
		continue
	print(item)


