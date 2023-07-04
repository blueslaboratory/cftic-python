# Day 26 - 04/07/2023
# Ejercicios de Hilos.docx
# Ejercicios de Hilos


'''
Ejercicio 3
Crea un programa que simule una cuenta regresiva de 10 segundos utilizando hilos.
Cada hilo debe imprimir el número correspondiente en orden descendente y esperar
un segundo antes de imprimir el siguiente número.
'''

# SOLUCION PROFE


import threading
import time


def cuenta_regresiva(numero):
	while numero > 0:
		print(numero)
		time.sleep(1)
		numero -= 1


# Crear e iniciar el hilo
hilo = threading.Thread(target=cuenta_regresiva, args=(10,))
hilo.start()

# Esperar a que el hilo termine
hilo.join()

print("¡Cuenta regresiva finalizada!")