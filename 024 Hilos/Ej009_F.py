# Day 26 - 04/07/2023
# Ejercicios de Hilos.docx
# Ejercicios de Hilos


'''
Ejercicio 9
Crea un programa que simule una sala de cine con 3 asientos disponibles. Se deben
crear 5 hilos, donde cada hilo representa a una persona intentando reservar un
asiento. El programa debe imprimir si cada persona pudo reservar el asiento o no.
'''

# SOLUCION PROFE


import threading

sala_cine = threading.Semaphore(3)


def persona(numero):
	sala_cine.acquire()
	print("Persona {} reservó un asiento".format(numero))
	sala_cine.release()


# Crear e iniciar los hilos
hilos = []
for i in range(5):
	hilo = threading.Thread(target=persona, args=(i + 1,))
	hilos.append(hilo)
	hilo.start()

# Esperar a que todos los hilos terminen
for hilo in hilos:
	hilo.join()
