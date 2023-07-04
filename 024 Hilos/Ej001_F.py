# Day 26 - 04/07/2023
# Ejercicios de Hilos.docx
# Ejercicios de Hilos


'''
Ejercicio 1
Crea un programa que imprima los números del 1 al 10 utilizando hilos, de
manera que cada hilo imprima un número. Asegúrate de que los números se impriman
en orden.
'''

# SOLUCION PROFE


import threading


def imprimir_numero(numero):
	print(numero)


# Crear e iniciar los hilos
for i in range(1, 11):
	hilo = threading.Thread(target=imprimir_numero, args=(i,))
	hilo.start()


# Esperar a que todos los hilos terminen
main_thread = threading.current_thread()
for hilo in threading.enumerate():
	if hilo is not main_thread:
		hilo.join()
