# Ejercicios de Listas y Tuplas
# Day 4 - 02/06/2023

'''
Ejercicio 1
Escribir un programa que almacene las asignaturas de un curso (por ejemplo
Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.
'''
print('\n*** EJERCICIO 1 ***')

asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
print(asignaturas)



'''
Ejercicio 2
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, 
Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje: 
Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.
'''
print('\n*** EJERCICIO 2 ***')

asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
for asignatura in asignaturas:
	print('Yo estudio ', asignatura)



'''
Ejercicio 3
Escribir un programa que almacene las asignaturas de un curso (por ejemplo 
Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario 
la nota que ha sacado en cada asignatura, y después las muestre por pantalla con 
el mensaje: En <asignatura> has sacado <nota> donde <asignatura> es cada una de las 
asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas 
por el usuario.
'''
print('\n*** EJERCICIO 3 ***')

asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
notas = []
i = 0

for asignatura in asignaturas:
	nota = round(float(input('Nota ' +asignatura +': ')), 2)
	notas.append(nota)

# 1º Forma de hacer el for:
print('\n1. Tus notas son: ')
for asignatura in asignaturas:
	print(asignatura +':' +str(notas[i]))
	i+=1

# 2º Forma de hacer el for:
print('\n2. Tus notas son: ')
for i in range(len(asignaturas)):
    print("En la asignatura " +asignaturas[i] +" has sacado: " +str(notas[i]))



'''
Ejercicio 4
Escribir un programa que pregunte al usuario los números ganadores de la lotería 
primitiva, los almacene en una lista y los muestre por pantalla ordenados de 
menor a mayor.
'''
print('\n*** EJERCICIO 4 ***')

numerosGanadores = []

for i in range(0,6):
	n = int(input('Numero ' +str(i+1) +': '))
	numerosGanadores.append(n)

complementario = int(input('Complementario: '))
reintegro = int(input('Reintegro: '))

numerosGanadores.sort()

print()
print('Numeros ganadores: ', numerosGanadores, sep='')
print('Complementario: ', complementario, sep='')
print('Reintegro: ', reintegro, sep='')



'''
Ejercicio 5
Escribir un programa que almacene en una lista los números del 1 al 10 y los
muestre por pantalla en orden inverso separados por comas.
'''
print('\n*** EJERCICIO 5 ***')

numeros = []

# Cargar la lista con los numeros
for i in range(1,11):
	numeros.append(i)

# Imprimir inverso
print(numeros[::-1])

# Solucion
for i in range(1,11):
	print(numeros[-i], end=',')



'''
Ejercicio 6
Escribir un programa que almacene las asignaturas de un curso (por ejemplo 
Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario 
la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas 
aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el 
usuario tiene que repetir.
'''


'''
Ejercicio 7
Escribir un programa que almacene el abecedario en una lista, elimine de la 
lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la 
lista resultante.
'''

'''
Ejercicio 8
Escribir un programa que pida al usuario una palabra y muestre por pantalla si 
es un palíndromo.
'''

'''
Ejercicio 9
Escribir un programa que pida al usuario una palabra y muestre por pantalla el 
número de veces que contiene cada vocal.
'''

'''
Ejercicio 10
Escribir un programa que almacene en una lista los siguientes precios: 
50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.
'''

'''
Ejercicio 11
Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas 
y muestre por pantalla su producto escalar.
'''

'''
Ejercicio 12
Escribir un programa que almacene las matrices

en una lista y muestre por pantalla su producto.
Nota: Para representar matrices mediante listas usar listas anidadas, representando 
cada vector fila en una lista.
'''

'''
Ejercicio 13
Escribir un programa que pregunte por una muestra de números, separados por comas, 
los guarde en una lista y muestre por pantalla su media y desviación típica.
'''