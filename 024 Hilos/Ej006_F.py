# Day 26 - 04/07/2023
# Ejercicios de Hilos.docx
# Ejercicios de Hilos


'''
Ejercicio 6
Enunciado: Crea un programa que simule una barrera utilizando hilos. El programa
debe crear 5 hilos, y cada hilo debe imprimir un mensaje cuando llegue a la barrera.
Después de que todos los hilos hayan llegado, se debe imprimir un mensaje indicando
que todos han llegado.
'''

# SOLUCION PROFE


import threading

barrera = threading.Barrier(5)


def hilo():
	print("Hilo {} llegó a la barrera".format(threading.current_thread().name))
	barrera.wait()
	print("Todos los hilos han llegado")


# Crear e iniciar los hilos
hilos = []
for i in range(5):
	hilo_actual = threading.Thread(target=hilo, name="Hilo {}".format(i))
	hilos.append(hilo_actual)
	hilo_actual.start()

# Esperar a que todos los hilos terminen
for hilo_actual in hilos:
	hilo_actual.join()
