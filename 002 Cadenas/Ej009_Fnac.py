# Ejercicios de Cadenas
# Day 2 - 31/05/2023

'''
Ejercicio 9
Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato
dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior
para que también funcione cuando el día o el mes se introduzcan con un solo carácter.
'''

print('\n *** EJERCICIO 9 ***')

fnac = input('Fecha nacimiento (formato: dd/mm/aaaa): ')
fnacSplit = fnac.split('/')

dd = fnacSplit[0].rjust(2, '0')
mm = fnacSplit[1].rjust(2, '0')
aaaa = fnacSplit[2].rjust(4, '0')

print('Fecha de nacimiento introducida: '
		+'\n\tDia:', dd
		+'\n\tMes:', mm
		+'\n\tYear:', aaaa)



print('\n *** EJERCICIO 9 - SOLUCION PROFE ***')

# fecha_nacimiento = input("Fecha nacimiento: ")
fecha_nacimiento = fnac

dia = fecha_nacimiento[:fecha_nacimiento.find('/')]
# Desde la 1º / hasta la 2º barra /
mes = fecha_nacimiento[fecha_nacimiento.find('/')+1:fecha_nacimiento.find('/', fecha_nacimiento.find('/')+1)]
# Desde la 2º / hasta el final
anyo = fecha_nacimiento[fecha_nacimiento.find('/', fecha_nacimiento.find('/')+1)+1:]

print("Dia: " + dia)
print("Mes: " + mes)
print("Anyo: " + anyo)



##Otra solucion
print('\n *** EJERCICIO 9 - OTRA SOLUCION PROFE ***')

posicion = fecha_nacimiento.find('/')
print("Dia:" + fecha_nacimiento[:posicion])

# sobreescribiendo fecha_nacimiento
fecha_nacimiento = fecha_nacimiento[posicion+1:]
posicion = fecha_nacimiento.find('/')
print("Mes:" + fecha_nacimiento[:posicion])

# sobreescribiendo fecha_nacimiento
fecha_nacimiento = fecha_nacimiento[posicion+1:]
print("Anyo:" + fecha_nacimiento)