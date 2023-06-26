# Day 20 - 26/06/2023
# Ejercicios Herencia.docx

'''
Ejercicio 8
Crear una clase Figura con un método calcular_area() que muestre un mensaje
genérico. Luego, crear clases Rectangulo y Triangulo que hereden de Figura
y sobrescriban el método calcular_area() para calcular y mostrar el área
específica de cada figura.
'''

# SOLUCION PROFE


class Figura:
    def calcular_area(self):
        print("Método calcular_area() de la clase Figura")


class Rectangulo(Figura):
    def calcular_area(self, base, altura):
        super().calcular_area()
        area = base * altura
        print("Área del rectángulo:", area)


class Triangulo(Figura):
    def calcular_area(self, base, altura):
        area = 0.5 * base * altura
        print("Área del triángulo:", area)


rectangulo = Rectangulo()
rectangulo.calcular_area(5, 3)  # Imprime: Área del rectángulo: 15

triangulo = Triangulo()
triangulo.calcular_area(4, 6)  # Imprime: Área del triángulo: 12.0
