# Ejercicios de Diccionarios
# Day 6 - 06/06/2023

'''
Ejercicio 4
Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por
pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre
del mes.
'''

print('\n*** EJERCICIO 4 ***')

fecha = input('Fecha (formato dd/mm/aaaa): ')
fechaList = fecha.split(sep='/')

dd = fechaList[0]
mm = fechaList[1]
aaaa = fechaList[2]

meses = {
	1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre"
}

mes = meses.get(int(mm), False)

if(mes == False):
	print('Mes existe:', mes)
else:
	print(dd, 'de', mes, 'de', aaaa)