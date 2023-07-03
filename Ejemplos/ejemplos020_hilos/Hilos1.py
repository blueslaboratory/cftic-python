# Day 25 - 03/07/2023
# Hilos - Módulo threading.docx
# Control de concurrencia con bloqueo (Lock)

import threading

contador = 0
lock = threading.Lock()


def incrementar():
	global contador
	for _ in range(100000):
		lock.acquire()
		print('*** incrementar ***')
		contador += 1
		lock.release()


def decrementar():
	global contador
	for _ in range(100000):
		lock.acquire()
		print('decrementar')
		contador -= 1
		lock.release()


# Crear los objetos Thread para cada función
hilo1 = threading.Thread(target=incrementar)
hilo2 = threading.Thread(target=decrementar)

# Iniciar la ejecucion de los hilos
hilo1.start()
hilo2.start()

# Esperar a que ambos hilos terminen
hilo1.join()
hilo2.join()
print("Valor final del contador:", contador)