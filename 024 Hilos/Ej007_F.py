# Day 26 - 04/07/2023
# Ejercicios de Hilos.docx
# Ejercicios de Hilos


'''
Ejercicio 7
Crea un programa que simule una cola utilizando hilos. El programa debe tener dos
hilos: uno para encolar elementos y otro para desencolar elementos. Se debe imprimir
cada acción realizada y asegurarse de que no haya conflicto en el acceso a la cola.
'''

# SOLUCION PROFE


import threading
import queue
import time

cola = queue.Queue()


def encolar_elemento(elemento):
	cola.put(elemento)
	print("Elemento {} encolado".format(elemento))


def desencolar_elemento():
	while True:
		if not cola.empty():
			elemento = cola.get()
			print("Elemento {} desencolado".format(elemento))
			time.sleep(1)


# Crear e iniciar los hilos
hilo_encolador = threading.Thread(target=encolar_elemento, args=("A",))
hilo_desencolador = threading.Thread(target=desencolar_elemento)

hilo_encolador.start()
hilo_desencolador.start()

# Esperar a que el encolador termine (el desencolador se ejecuta en un ciclo infinito)
hilo_encolador.join()
