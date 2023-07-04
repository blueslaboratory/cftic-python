# Day 26 - 04/07/2023
# Ejercicios de Hilos.docx
# Ejercicios de Hilos


'''
Ejercicio 2
Crea un programa que calcule la suma de los números del 1 al 100 utilizando hilos.
Cada hilo debe calcular la suma de una parte del rango y al final se debe imprimir
la suma total.
'''

# SOLUCION PROFE


import threading

def calcular_suma(inicio, fin, resultado):
    suma = sum(range(inicio, fin + 1))
    resultado.append(suma)

# Crear e iniciar los hilos
num_hilos = 5
hilos = []
rango = 100
paso = rango // num_hilos
resultados = []

for i in range(num_hilos):
    inicio = i * paso + 1
    fin = (i + 1) * paso
    hilo = threading.Thread(target=calcular_suma, args=(inicio, fin, resultados))
    hilos.append(hilo)
    hilo.start()

# Esperar a que todos los hilos terminen su ejecución
for hilo in hilos:
    hilo.join()

# Calcular la suma total
suma_total = sum(resultados)

print("Suma total:", suma_total)
