# Day 5 - 05/06/2023

def saludar(nombre, apellido, year = 2023):
	cadenaSaludo = 'Hola ' +nombre +' ' +apellido
	print('Estamos en el year:', year)
	return cadenaSaludo

print('\nInicio programa')

myFunction = saludar

print()
print(type(myFunction))
saludo = myFunction('Pepe', 'Pinoenor Mi')

print(saludo)