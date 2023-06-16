# Day 13 - 15/06/2023
# Ejercicios Mix
# En esto es lo que consiste Data Warehouse

datos_iniciales = ['Juan Pérez;30;Masculino;Ingeniero', 'María García;25;Femenino;Doctora']
datos_finales = []

# Creando las listas de campos []
for i, dato in enumerate(datos_iniciales):
	print()
	print(i, '- Lista: ')
	campos = dato.split(';')
	print(campos)
	campos[2] = 0 if campos[2] == 'Masculino' else 1
	print(campos)

	# Casteando de lista a tupla
	print(i, '- Tupla: ')
	tupla_datos = tuple(campos)
	print(tupla_datos)

	campos[3] = campos[3].upper()
	print(campos)
	datos_finales.append(tupla_datos)


print('\nDatos finales:')
print(datos_finales)
