# Day 24 - 30/06/2023
# Ejercicios Lambda


# Nivel básico
'''
Ejercicio 3
Escribe una función lambda que tome una lista de números como parámetro y devuelva
la lista ordenada de forma ascendente.
'''

listaNumeros = [9, 8, 7, 6, 5, 4, 3, 2, 1]

# lista.sort() --> ordena la lista pero no devuelve ningun objeto
def funcionOrdenar(lista):
	lista.sort()
	return lista


lambda lista: sorted(lista)
ordenar0 = lambda lista: sorted(lista)

ordenar1 = lambda x:x.sort()



print(funcionOrdenar(listaNumeros))

print((lambda lista: sorted(lista))(listaNumeros))
print(ordenar0(listaNumeros))

ordenar1(listaNumeros)
print(listaNumeros)