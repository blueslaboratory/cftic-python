# Day 26 - 04/07/2023
# Ejercicios de Hilos.docx
# Ejercicios de Hilos


'''
Ejercicio 5
Crea un programa que simule un semáforo utilizando hilos. El semáforo debe tener
tres estados: rojo, amarillo y verde. Cada estado debe durar 2 segundos y se debe
imprimir el estado actual del semáforo en cada iteración.
'''

# SOLUCION PROFE


import threading
import time


def semaforo():
	estados = ["rojo", "amarillo", "verde"]

	while True:
		for estado in estados:
			print("Semáforo:", estado)
			time.sleep(2)


# Crear e iniciar el hilo
hilo_semaforo = threading.Thread(target=semaforo)
hilo_semaforo.start()

# Esperar a que el hilo termine (esto no sucederá en este caso)
hilo_semaforo.join()