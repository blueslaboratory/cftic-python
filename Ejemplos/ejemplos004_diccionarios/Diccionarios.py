# Day 5 - 05/06/2023

diccionario = {'nombre': 'iJunio2023',
                202306: 4096,
               'codigo': 1,
               'popeame': 'yaNoHayStop'}

print(diccionario['nombre'])
print(diccionario['codigo'])


# Cambiar un valor
print('\n*** Cambiar un valor ***')
diccionario[202306] = 5060
print(diccionario[202306])


# Agregar un valor
print('\n*** Agregar un valor ***')
diccionario['fecha'] = '20230605'
print(diccionario['fecha'])


# Agregar un nuevo par clave-valor
print('\n*** Agregar un par clave-valor ***')
diccionario['profesion'] = 'Ingeniero'
print(diccionario['profesion'])
print(diccionario.get('profesion'))


# Eliminar un valor
print('\n*** Eliminar un valor ***')
del diccionario['fecha']
print('diccionario[\'fecha\'] eliminado')

# Eliminar un elemento y obtener su valor
print('\n*** Eliminar un elemento y obtener su valor ***')
noHayStop = diccionario.pop('popeame')
print('diccionario[\'popeame\'] eliminado, valor:', noHayStop)


# Verificar si una clave esta presente
print('\n*** Verificar si una clave esta presente ***')
presente = 'fecha' in diccionario
print('Presente clave fecha: ', presente)
presente = 'codigo' in diccionario
print('Presente clave codigo: ', presente)


# Recorrer un diccionario
print('\n*** Recorrer un diccionario 1: clave ***')
for clave in diccionario:
	print(clave)

for clave in diccionario.keys():
	print(clave)


print('\n*** Recorrer un diccionario 2: valor ***')
for clave in diccionario:
	print(diccionario[clave])

for valor in diccionario.values():
	print(valor)


print('\n*** Recorrer un diccionario 3: clave-valor ***')
for clave in diccionario:
	print(clave, '->', diccionario[clave])

for item in diccionario.items():
	print(item[0], '->', item[1])

for clave, valor in diccionario.items():
	print(clave, '->', valor)

