# Day 14 - 16/06/2023
# Ejercicios Mix
# En esto es lo que consiste Data Warehouse


def tratar_datos(datos_iniciales):
	datos_finales = []

	# Creando las listas de campos []
	for dato in datos_iniciales:
		campos = dato.split(';')
		campos[2] = 0 if campos[2] == 'Masculino' else 1
		campos[3] = campos[3].upper()
		datos_finales.append(tuple(campos))

	return datos_finales

datos_iniciales = ['Juan Pérez;30;Masculino;Ingeniero', 'María García;25;Femenino;Doctora']
print(datos_iniciales)

print('\nDatos finales:')
print(tratar_datos(datos_iniciales))
