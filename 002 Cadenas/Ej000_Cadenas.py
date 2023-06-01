# Ejercicios de Cadenas


'''
Ejercicio 1
Escribir un programa que pregunte el nombre del usuario en la consola y un
número entero e imprima por pantalla en líneas distintas el nombre del usuario
tantas veces como el número introducido.
'''
print('\n *** EJERCICIO 1 ***')
nombre = input('Nombre: ') + '\n'
n = int(input('Numero de veces: '))
print(nombre*n)



'''
Ejercicio 2
Escribir un programa que pregunte el nombre completo del usuario en la consola y 
después muestre por pantalla el nombre completo del usuario tres veces, una con 
todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con 
la primera letra del nombre y de los apellidos en mayúscula. El usuario puede 
introducir su nombre combinando mayúsculas y minúsculas como quiera.
'''
print('\n *** EJERCICIO 2 ***')
nombre = input('Nombre completo: ').lower() + '\n'

print('Nombre en minusculas: ')
print(nombre*3)
print('Nombre en mayusculas: ')
print(nombre.upper())
print('Nombre con iniciales en mayusculas: ')
print(nombre.title())



'''
Ejercicio 3
Escribir un programa que pregunte el nombre del usuario en la consola y después de 
que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, 
donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras 
que tienen el nombre.
'''
print('\n *** EJERCICIO 3 ***')
nombre = input('Nombre: ').upper() + '\n'
print('Nombre: ' + nombre
      +'Letras: ' +str(len(nombre)-1))
print()



'''
Ejercicio 4
Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension 
donde el prefijo es el código del país +34, y la extensión tiene dos dígitos 
(por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de 
teléfono con este formato y muestre por pantalla el número de teléfono sin el 
prefijo y la extensión.
'''
print('\n *** EJERCICIO 4 ***')
telefono = input('Telefono (formato: prefix-nº-extension, e.g. +34-913146921-55): ')
# Elemento del primer numero sin prefijo: 4
# Elemento del ultimo numero sin extension: 13
print('Telefono sin extension: ', telefono[4:13])



'''
Ejercicio 5
Escribir un programa que pida al usuario que introduzca una frase en la consola y 
muestre por pantalla la frase invertida.
'''
print('\n *** EJERCICIO 5 ***')
frase = input('Frase: ')
print('Frase reverse: ', frase[::-1])



'''
Ejercicio 6
Escribir un programa que pida al usuario que introduzca una frase en la consola y 
una vocal, y después muestre por pantalla la misma frase pero con la vocal 
introducida en mayúscula.
'''
print('\n *** EJERCICIO 6 ***')
frase = input('Frase: ')
vocal = input('Vocal: ')
print(frase.replace(vocal, vocal.upper()))



'''
Ejercicio 7
Escribir un programa que pregunte el correo electrónico del usuario en la consola y 
muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante 
de la arroba @) pero con dominio ceu.es.
'''
print('\n *** EJERCICIO 7 ***')
correo = input('Correo (e.g. blueslaboratory@labs.com): ')
correoList = correo.split('@')
print(correoList[0] + '@' + 'ceu.es')



'''
Ejercicio 8
Escribir un programa que pregunte por consola el precio de un producto en euros con 
dos decimales y muestre por pantalla el número de euros y el número de céntimos del 
precio introducido.
'''
print('\n *** EJERCICIO 8 ***')
precio = input('Precio producto (€) con 2 decimales (e.g. 69.77€): ')
precioSplit = precio.split('.')

print('Euros:', precioSplit[0])
print('Centimos:', precioSplit[1])



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



'''
Ejercicio 10
Escribir un programa que pregunte por consola por los productos de una cesta de la 
compra, separados por comas, y muestre por pantalla cada uno de los productos en una 
línea distinta.
'''
print('\n *** EJERCICIO 10 ***')
cesta = input('Cesta (e.g. baguette,croisant,dinosaurus...): ')
cestaList = cesta.split(',')
for producto in cestaList:
	print('\t' +producto)



'''
Ejercicio 11
Escribir un programa que pregunte el nombre el un producto, su precio y un número de 
unidades y muestre por pantalla una cadena con el nombre del producto seguido de su: 
--> precio unitario con 6 dígitos enteros y 2 decimales, 
--> número de unidades con 3 dígitos y 
--> coste total con 8 dígitos enteros y 2 decimales.
'''
print('\n *** EJERCICIO 11 ***')

producto = input('Nombre del producto: ')
precioUnitario = float(input('Precio unitario: '))
unidades = int(input('Unidades: '))
costeTotal = precioUnitario * unidades


cadenaFinal = f'Producto: {producto}\n'

cadenaFinal += f'Precio unitario con 0s: {precioUnitario:06.2f}\n'
cadenaFinal += f'Precio unitario: {precioUnitario:06.2f}\n'

cadenaFinal += f'Unidades con 0s: {unidades:03d}\n'
cadenaFinal += f'Unidades: {unidades:03d}\n'

cadenaFinal += f'Coste total con 0s: {costeTotal:08.2f}\n'
cadenaFinal += f'Coste total: {costeTotal:08.2f}'


print(cadenaFinal)