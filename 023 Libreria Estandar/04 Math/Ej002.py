# Day 26 - 04/07/2023
# Ejercicios Librerias Estandar.docx
# Modulo Math

'''
Ejercicio 2
Escribe un programa que calcule el perímetro de un triángulo equilátero
dado el tamaño de uno de sus lados.
'''

# SOLUCION PROFE


def calcular_perimetro_triangulo(lado):
    perimetro = 3 * lado
    return perimetro


lado = 10

perimetro_triangulo = calcular_perimetro_triangulo(lado)
print(f"El perímetro del triángulo equilátero con lado {lado} es: {perimetro_triangulo}")