# Ejercicios de Diccionarios
# Day 9 - 09/06/2023

'''
Ejercicio 9
Escribir un programa que gestione las facturas pendientes de cobro de una empresa.
Las facturas se almacenarán en un diccionario donde la clave de cada factura será
el número de factura y el valor el coste de la factura. El programa debe preguntar
al usuario si quiere añadir una nueva factura, pagar una existente o terminar.
Si desea añadir una nueva factura se preguntará por el número de factura y su coste
y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el
número de factura y se eliminará del diccionario. Después de cada operación el
programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad
pendiente de cobro.
'''


print('\n*** EJERCICIO 9 *** - SOLUCION PROFE')

facturas={'2023001':900.90,'2023044':89.5}
opcion=0;
cantidad_cobrada=0;
cantidad_pendiente_cobro=0;

for factura in facturas:
    cantidad_pendiente_cobro += facturas[factura]

while opcion != 3:

    if opcion == 1:
        print('Agregar factura:')
        num_factura = input('Número de factura: ')
        facturas[num_factura] = float(input('Importe factura: '))
        cantidad_pendiente_cobro += facturas[num_factura]

    elif opcion == 2:
        print('Pagar factura:')
        print(facturas)
        num_factura = input('Número de factura: ')
        cantidad_cobrada += facturas[num_factura]
        cantidad_pendiente_cobro -= facturas[num_factura]
        facturas.pop(num_factura)

    print('Cantidad cobrada:', cantidad_cobrada, '€')
    print('Cantidad pendiente de cobro:', cantidad_pendiente_cobro, '€')

    opcion = int(input('Menú:'+
                       '\n 1.Añadir Factura '+
                       '\n 2.Pagar Factura '+
                       '\n 3.Terminar'+
                       '\n Opción:'))
