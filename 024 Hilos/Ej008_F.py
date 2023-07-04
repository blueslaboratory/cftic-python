# Day 26 - 04/07/2023
# Ejercicios de Hilos.docx
# Ejercicios de Hilos


'''
Ejercicio 8
Enunciado: Crea un programa que genere 5 hilos y cada uno imprima los números del
1 al 5 en orden ascendente, con un retraso de 0.5 segundos entre cada número.
'''

# SOLUCION PROFE


import threading
import time


def imprimir_numeros():
	for i in range(1, 6):
		print("Hilo {}: {}".format(threading.current_thread().name, i))
		time.sleep(0.5)


# Crear e iniciar los hilos
hilos = []
for i in range(5):
	hilo = threading.Thread(target=imprimir_numeros, name="Hilo {}".format(i + 1))
	hilos.append(hilo)
	hilo.start()

# Esperar a que todos los hilos terminen
for hilo in hilos:
	hilo.join()