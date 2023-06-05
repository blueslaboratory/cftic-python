# Day 5 - 05/06/2023

print('\n*** Funcion saludar ***')
def saludar():
	print('hola')
	return 'mundo'

print('Esta es la primera sentencia que se ejecuta')
print(saludar())
print(saludar)




print('\n*** Funcion saludarParametros ***')
def saludarParametros(nombre, apellido):
	print('hola', nombre, apellido)
	return 'Bienvenido'

print(saludarParametros('Pepe', 'Gomez'))
# Esto de a continuacion no se debe hacer
print(saludarParametros(apellido='Gomez', nombre='Pepe'))




# Con valor por defecto year=2022
print('\n*** Funcion saludarParametros2 ***')
def saludarParametros2(nombre, apellido, year=2022):
	print('Hola', nombre, apellido)
	print('Estamos en el year:', year)
	return 'Bienvenido'

saludarParametros2('Pepe', 'Gomez')
# Esto de a continuacion no se debe hacer
saludarParametros2(apellido='Gomez', nombre='Pepe', year=1)




# Con valor *nombres pasamos una tupla
print('\n*** Funcion saludarParametros3 ***')
def saludarParametros3(*nombres, year=2022):
	print('hola', end=' ')

	print(nombres)

	for nombre in nombres:
		print(nombre, end=', ')

	print('\nEstamos en el year:', year)
	return 'Bienvenido'

saludarParametros3('Pepe', 'Juan', 'Maria', 'Ana', year=2023)




# Con valor **nombres pasarimos un diccionario
print('\n*** Funcion saludarParametros4 ***')
def saludarParametros4(year=2022, **nombresCompletos):
	print('hola', end=' ')

	print(nombresCompletos)
	print()

	for nombreClave in nombresCompletos:
		print('Hola', nombreClave, nombresCompletos[nombreClave], end='\n')

	print('\nEstamos en el year:', year)
	return 'Bienvenido'


diccionarioPersonas = {'Pepe':'Leon Esvinito',
                       'Susana':'Oria Estaqui',
                       'Alejandro':'Medario Bebagua'}

# Ojo que aqui hay que meter **
saludarParametros4(1999, **diccionarioPersonas)




# Con valor **nombres pasariamos un diccionario
print('\n*** Funcion saludarParametros5 ***')
def saludarParametros5(**nombresCompletos):

	for clave, valor in nombresCompletos.items():
		print(clave, ': ', valor, sep='')

	print()
	return 'Bienvenido'

diccionarioPersonas = {'nombre':'Pepe',
                       'apellido': 'Leon Esvinito'}

saludarParametros5(**diccionarioPersonas)
# Pasando un diccionario por parametro directamente
saludarParametros5(name='Susana', surname='Oria Estaqui')




print('\n*** Funcion imprimirFicha ***')

fichaPersona = {'nombre':'Pepe', 'apellido':'Pere Sa', 'edad':42}

def imprimirFicha(datosPersona):
	for claveFicha in datosPersona:
		print(claveFicha, '->', datosPersona[claveFicha])

imprimirFicha(fichaPersona)




print('\n*** Funcion imprimirFicha2 ***')
# Cuando no tenemos el diccionario hecho es cuando queremos los 2 asteriscos (doble puntero)

# esto no funcionaria
# def imprimirFicha(datosPersona):
def imprimirFicha(**datosPersona):
	print(type(datosPersona))
	for claveFicha in datosPersona:
		print(claveFicha, '->', datosPersona[claveFicha])

imprimirFicha(nombre='Susana', apellido='Oria Estaqui', edad=23)