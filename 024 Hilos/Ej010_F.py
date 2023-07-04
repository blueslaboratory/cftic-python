# Day 26 - 04/07/2023
# Ejercicios de Hilos.docx
# Ejercicios de Hilos


'''
Ejercicio 10
Enunciado: Crea un programa que simule un juego de ping-pong entre dos jugadores
utilizando hilos. El programa debe imprimir el nombre del jugador actual y alternar
entre los dos jugadores en cada iteración. El juego debe tener un total de 10 puntos
y se debe imprimir el nombre del ganador al final.
'''

# SOLUCION PROFE


import threading

puntos = 0
mutex = threading.Lock()


def jugador(nombre):
	global puntos
	while puntos < 10:
		with mutex:
			puntos += 1
			print("{} anotó un punto (Total: {})".format(nombre, puntos))


# Crear e iniciar los hilos
hilo_jugador1 = threading.Thread(target=jugador, args=("Jugador 1",))
hilo_jugador2 = threading.Thread(target=jugador, args=("Jugador 2",))

hilo_jugador1.start()
hilo_jugador2.start()

# Esperar a que ambos jugadores anoten 10 puntos
hilo_jugador1.join()
hilo_jugador2.join()

ganador = "Jugador 1" if puntos >= 10 else "Jugador 2"
print("¡{} ha ganado!".format(ganador))
