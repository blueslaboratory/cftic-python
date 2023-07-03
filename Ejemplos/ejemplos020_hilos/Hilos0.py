# Day 25 - 03/07/2023
# Hilos - Módulo threading.docx
# Ejemplo basico

import threading


def funcion1():
	print('Funcion 1 ejecutandose')

def funcion2():
	print('Funcion 2 ejecutandose')


print('Programa principal de inicio')

# Crear los objetos Thread para cada funcion
hilo1 = threading.Thread(target=funcion1)
hilo2 = threading.Thread(target=funcion2)

# Iniciar la ejecucion de los hilos
hilo1.start()
hilo2.start()

# Esperar a que ambos hilos terminen
hilo1.join()
hilo2.join()

print('Programa principal final')