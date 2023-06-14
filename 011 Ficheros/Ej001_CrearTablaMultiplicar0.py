# Day 12 - 14/06/2023
# Ejercicios de Ficheros


'''
Ejercicio 1
Escribir una función que pida un número entero entre 1 y 10 y guarde en un
fichero con el nombre tabla-n.txt la tabla de multiplicar de ese número,
donde n es el número introducido.
'''


print('\n*** EJERCICIO 1 - SOLUCION PROFE ***')

n = int(input('Numero [1,10]: '))
nombre_fichero = 'tabla-'+str(n)+'.txt'
fichero = open(nombre_fichero, 'w')

for i in range(1,11):
    multiplicacion = i * n
    cadena = str(n) + ' * ' + str(i) + ' = ' + str(multiplicacion) + '\n'
    fichero.write(cadena)

fichero.close()