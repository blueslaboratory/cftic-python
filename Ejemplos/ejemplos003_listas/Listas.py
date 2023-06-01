# 01/06/2023

cesta_compra = []


print('\n*** cesta_compra ***')
cesta_compra += ['pan', 'cafe', 'leche', '$$$$']
print(cesta_compra)


print('\n*** cesta_compra*3 ***')
cesta_compra *= 3
print(cesta_compra)


print('\n*** cesta_compra.clear() ***')
cesta_compra.clear()
print(cesta_compra)


print('\n*** cesta_compra = None ***')
cesta_compra = None
print(cesta_compra)
print(type(cesta_compra))


print('\n*** cesta_compra types ***')
cesta_compra = ['pan', 2, 3.33, None]
for item in cesta_compra:
	print(type(item))


print('\n*** cesta_compra recorrer ***')
# Ejemplo para recorrer
numeros = [0,1,2,3,4,5,6,7,8,9]
for item in numeros[2:9]:
	print(item)


print('\n*** cesta_compra continue  ***')
for item in numeros[1:]:
	if(item%2 == 0):
		continue
	print(item)


print('\n*** cesta_compra break  ***')
for item in numeros[1:]:
	if(item%2 == 0):
		break
	print(item)


print('\n*** for: cadena fin de bucle ***')
cadena = '    xxx'
for caracter in cadena:
	print(caracter)
else:
	print('fin de bucle')


print('\n*** for: cadena fin de bucle ***')
for item in range(3):
	print(item)
else:
	print('Se ha acabado el range, el alcance')
	print('Imprimamos el ultimo valor de item en el else:')
	print(item)


print('-----------------------')
for index in range(1,10,2):
	print(index)