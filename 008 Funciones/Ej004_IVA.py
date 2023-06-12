# 12/06/2023 - Day 10
# Ejercicios de Funciones

'''
Ejercicio 4
Escribir una función que calcule el total de una factura tras aplicarle el IVA.
La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar,
y devolver el total de la factura. Si se invoca la función sin pasarle el
porcentaje de IVA, deberá aplicar un 21%.
'''

print('\n*** EJERCICIO 4 ***')
def calcularIva(importe, iva=21):
	return importe*(1+iva/100)

importe = float(input('Importe: '))
iva = float(input('Iva: '))

print('\nEl iva (€) de', importe, 'es', calcularIva(importe, iva))