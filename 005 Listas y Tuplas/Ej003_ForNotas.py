# Ejercicios de Listas y Tuplas
# Day 4 - 02/06/2023

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
	print(asignatura +': ' +str(notas[i]))
	i+=1

# 2º Forma de hacer el for:
print('\n2. Tus notas son: ')
for i in range(len(asignaturas)):
	print("En la asignatura " +asignaturas[i] +" has sacado: " +str(notas[i]))




#################################################################
# Otra forma
#################################################################

print('\n*** EJERCICIO 3 - OTRA SOLUCION ***')
print('ID sin concatenacion: mejor rendimiento')

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []

for asignatura in asignaturas:
    nota = input("¿Qué nota has sacado en " + asignatura + "? ")
    notas.append(nota)
    print(id(notas))
print(type(enumerate(asignaturas)))

for index,asignatura in enumerate(asignaturas):
    print("En la asignatura "+asignatura+" has sacado la nota "+notas[index])




#################################################################
# Otra forma
#################################################################

# CASTEO: CONVERTIR STRING A LISTA

print('\n*** EJERCICIO 3 - OTRA SOLUCION 2 ***')
print('ID con concatenacion: peor rendimiento')

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []

for asignatura in asignaturas:
    nota = input("¿Qué nota has sacado en " + asignatura + "? ")
    # Convierte nota que es str a un elemento de lista
    notas = notas + [nota]
    print(id(notas))

print(type(enumerate(asignaturas)))

for index,asignatura in enumerate(asignaturas):
    print("En la asignatura "+asignatura+" has sacado la nota "+notas[index])