# Ejercicios Datos Simples
# Day 1 - 30/05/2023

"""
Ejercicio 5
Escribir un programa que pregunte al usuario por el número de horas trabajadas y el 
coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
"""

print('\n *** EJERCICIO 5 ***')
horas = int(input('Introduce las horas trabajadas: '))
satoshisPorHora = float(input('Introduce tu precio por hora (丰):' ))
paga = horas*satoshisPorHora
print('Paga correspondiente concatenacion: ' +str(paga))
print('Paga correspondiente con coma: ', paga)

