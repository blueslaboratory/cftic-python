# Ejercicios Datos Simples
# Day 1 - 30/05/2023


"""
Ejercicio 7
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el
índice de masa corporal (IMC) y lo almacene en una variable, y muestre por pantalla la frase:
Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado
redondeado con dos decimales.
Cálculo de imc: consiste en dividir el peso, expresado en kilos, entre la estatura,
en metros, elevada al cuadrado (kg/m^2)
"""

print('\n *** EJERCICIO 7 ***')

masa = float(input('Masa corporal (kg): '))
estatura = float(input('Estatura (m): '))

IMC = masa/(estatura**2)
IMC_rounded = round(IMC, 2)

print('IMC = ', IMC_rounded)


