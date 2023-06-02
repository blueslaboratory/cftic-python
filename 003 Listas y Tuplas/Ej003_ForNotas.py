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
	print(asignatura +':' +str(notas[i]))
	i+=1

# 2º Forma de hacer el for:
print('\n2. Tus notas son: ')
for i in range(len(asignaturas)):
    print("En la asignatura " +asignaturas[i] +" has sacado: " +str(notas[i]))