# Day 2 - 31/02/2023


print('\n*** CADENA 1 - LONGITUD Y SUBSTR ***')
cadena = 'Hola mundo'

print(cadena)

print('Longitud Cadena: ', len(cadena))
print('\ncadena: ' +cadena,
      '\ncadena[0]: ' +cadena[0],
      '\ncadena[len(cadena)-1]: ' +cadena[len(cadena)-1])



print('\n*** CADENA 2 - MULTIPLICAR CADENAS ***')
cadena2 = 'Otro' +' ' +'mundo' +'\n'
cadena2 = cadena2*3
print(cadena2)



print('\n*** CADENA 3 - CAPITALIZE ***')
print('Reverse de cadena: ', ''.join(reversed(cadena)))

cadena3 = 'clase'
cadena3.capitalize()
print('No capitaliza porque apunta a otra direccion de memoria: ', cadena3)
# funciona asi porque es mucho mas rapido

cadena3 = 'clase'.capitalize()
print('Capitaliza porque apunta a la direccion de memoria correcta: ', cadena3)



print('\n*** CADENA 4 - TIPOS ***')
print('Para saber el type en Pycharm, puedes poner la variable y el . o usar el type')
# cadena.
cadena4 = 'mucho-texto'
print(type(cadena4))
print(type(55))
print(type(6.9))



print('\n*** CADENA 5 - ORDEN Y UNICODE ***')
cadena5 = 'abcxyz'
print(type(cadena5))

# print(max(cadena5)) imprime el caracter de mayor valor (segun su codigo Unicode) en la cadena
print(max(cadena5))

# ord() se utiliza para obtener el valor numerico del codigo Unicode de un caracter
print(ord(max(cadena5)))



print('\n*** CADENA 6 - RELLENAR ***')
cadena6 = 'hi'
print(cadena6.rjust(7,'#'))



print('\n*** CADENA 7 - SPLITS ***')
cadena7 = 'Fast;And;Furious;X'
lista = cadena7.split(';')
print(type(lista))
print(lista)

cadena7 = 'Tokyo\nDrift\nTeriyaki\nMagodofu'
lista = cadena7.splitlines()
print(lista)



print('\n*** CADENA 8 - SUBSTRINGS ***')
cadena8 = 'mi carro me lo robaron'
print('cadena8[5:] -->', cadena8[5:])
print('cadena8[8:] -->', cadena8[:8])
print('cadena8[15:19] --> ', cadena8[15:19])
print('cadena8[9:-3] + n --> ', cadena8[9:-3] + 'n')

# Imprime hasta la posicion -1 y rellename hasta los 40 caracteres con 'O'
print('\nImprime hasta la posicion -1 y rellename hasta los 40 caracteres con \'O\'')
print(cadena8[:-1].ljust(40, '0').upper())

numeros = '0123456789'
# Desde las posiciones [0:7] saltame cada 3 caracteres
print('\nDesde las posiciones [0:7] saltame cada 3 caracteres')
print(numeros[0:7:3])

# Imprimir la cadena del reves
print('\nImprimir la cadena del reves')
print(numeros[::-1])

# Replace
print('\nReplace')
print(numeros.replace('67', '\__replace__/'))



print('\n*** CADENA 9 - FORMATEAR ***')
cadena9 = 'Mi nombre es %s y estudio en %s en el year %d'

# %s --> string
# %x --> enteros representados en hexadecimal
# %d --> enteros representados en decimal

nombre = 'Alejandro'
localidad = 'CFTIC'
year = 2022

print(cadena9 % ('Alejandro', 'CFTIC', 2022))
print(cadena9 % (nombre, localidad, year))


cadena9 = 'Mi nombre es {0} y estudio en {1} en el year {2}'
print(cadena9.format(nombre, localidad, year))
# La f es totalmente necesaria
print(f'Mi nombre es {nombre} y estudio en {localidad} en el year {year}')

cadena9 = 'Mi nombre es %s y estudio en %s en el year %d' % (nombre,localidad,year)
print(cadena9)
cadena9 = 'Mi nombre es {0} y estudio en {1} en el year {2}'.format(nombre, localidad, year)
print(cadena9)