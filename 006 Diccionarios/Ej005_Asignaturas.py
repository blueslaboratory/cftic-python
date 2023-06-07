# Ejercicios de Diccionarios
# Day 7 - 07/06/2023

'''
Ejercicio 5
Escribir un programa que almacene el diccionario con los créditos de las
asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después
muestre por pantalla los créditos de cada asignatura en el formato <asignatura>
tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas
del curso, y <créditos> son sus créditos. Al final debe mostrar también el
número total de créditos del curso.
'''

print('\n*** EJERCICIO 5 ***')

asignaturas = {
	'Matematicas':6,
	'Fisica':4,
	'Quimica':5
}

creditos = 0

for clave in asignaturas:
	print(clave, 'tiene', asignaturas[clave], 'creditos')
	creditos += asignaturas[clave]

print('\nNumero total de creditos del curso:', creditos)
