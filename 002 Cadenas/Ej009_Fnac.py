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