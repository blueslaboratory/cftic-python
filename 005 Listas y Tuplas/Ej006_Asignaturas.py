# Ejercicios de Listas y Tuplas
# Day 4 - 02/06/2023


'''
Ejercicio 6
Escribir un programa que almacene las asignaturas de un curso (por ejemplo
Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario
la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas
aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el
usuario tiene que repetir.
'''

print('\n*** EJERCICIO 6 ***')

asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
asignaturasSuspensas = asignaturas.copy();
notas = []

for i in range(len(asignaturas)):
	nota = round(float(input('Nota ' +asignaturas[i] +': ')), 2)
	if(nota<5.0):
		notas.append(nota)
	else:
		asignaturasSuspensas.remove(asignaturas[i])


print()
print('len(asignaturasSuspensas):', len(asignaturasSuspensas))
print('len(notas):', len(notas))


print('\nDebes repetir: ')
for i in range(len(asignaturasSuspensas)):
	print(asignaturasSuspensas[i], ':', notas[i])




#################################################################
# Otra manera
#################################################################
print('\n*** EJERCICIO 6 - OTRA FORMA ***')

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
asignaturasSuspendidas = [];

for asignatura in asignaturas:
	nota = int(input("Nota en la asignatura " + asignatura +":"))
	if nota < 5:
		asignaturasSuspendidas.append(asignatura)

print("Asignaturas suspendidas "+str(asignaturasSuspendidas))