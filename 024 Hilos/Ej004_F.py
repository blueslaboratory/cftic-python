# Day 26 - 04/07/2023
# Ejercicios de Hilos.docx
# Ejercicios de Hilos


'''
Ejercicio 4
Crea un programa que simule una carrera entre dos corredores utilizando hilos.
Cada corredor debe imprimir su nombre y avanzar un paso en cada iteración.
El primer corredor en llegar a la meta debe ser anunciado como el ganador.
'''

# SOLUCION PROFE


import threading
import time


def corredor(nombre):
	distancia = 0
	while distancia < 10:
		distancia += 1
		print(nombre, "avanzó un paso")
		time.sleep(0.1)

	print(nombre, "ha llegado a la meta")


# Crear e iniciar los hilos
hilo_corredor1 = threading.Thread(target=corredor, args=("Corredor 1",))
hilo_corredor2 = threading.Thread(target=corredor, args=("Corredor 2",))

hilo_corredor1.start()
hilo_corredor2.start()

# Esperar a que ambos corredores lleguen a la meta
hilo_corredor1.join()
hilo_corredor2.join()

print("Carrera finalizada")
