# Day 20 - 26/06/2023
# Ejercicios Herencia.docx

'''
Ejercicio 5
Crear una clase Fruta con un atributo color y un método mostrar_color()
que imprima el color de la fruta. Luego, crear una clase Manzana que herede
de Fruta y tenga un atributo adicional sabor. Sobrescribir el método
mostrar_color() de Manzana para imprimir el color y el sabor de la manzana.
'''

# SOLUCION PROFE


class Fruta:
    def __init__(self, color):
        self.color = color

    def mostrar_color(self):
        print("Color de la fruta:", self.color)


class Manzana(Fruta):
    def __init__(self, color, sabor):
        super().__init__(color)
        self.sabor = sabor

    def mostrar_color(self):
        super().mostrar_color()
        print("Sabor de la manzana:", self.sabor)


manzana = Manzana("rojo", "dulce")
manzana.mostrar_color()
