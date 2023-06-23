# Day 19 - 23/06/2023
# Ejercicios Herencia.docx

'''
Ejercicio 1
Crear una clase Figura con un metodo calcular_area() que imprima
"Metodo calcular_area() de la clase Figura". Luego, crear una clase
Rectangulo que herede de Figura y sobrescriba el metodo calcular_area()
para calcular y mostrar el área de un rectangulo.
'''

from Ej001_Rectangulo import Rectangulo

# Crear el objeto
rectangulo = Rectangulo(5,5)
rectangulo.calcularArea()