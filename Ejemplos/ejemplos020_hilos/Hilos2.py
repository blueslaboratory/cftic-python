# Day 25 - 03/07/2023
# Hilos - Módulo threading.docx
# Control de concurrencia con bloqueo (Lock)

import threading
import queue

cola = queue.Queue()


def productor():
	for i in range(5):
		mensaje = "Mensaje {}".format(i)
		cola.put(mensaje)
		print("Productor: mensaje '{}' producido".format(mensaje))


def consumidor():
	while True:
		mensaje = cola.get()
		print("Consumidor: mensaje '{}' consumido".format(mensaje))
		cola.task_done()


# Crear los objetos Thread para cada funcion
hilo_productor = threading.Thread(target=productor)
hilo_consumidor = threading.Thread(target=consumidor)

# Iniciar la ejecucion de los hilos
hilo_productor.start()
hilo_consumidor.start()

# Esperar a que el productor termine
# (en este caso, el consumidor se ejecuta en un ciclo infinito)
hilo_productor.join()
print("Programa principal")