# Day 20 - 26/06/2023
# Ejercicios Herencia.docx

'''
Ejercicio 9
Crear una clase Vehiculo con atributos marca y modelo. Luego, crear una
clase Automovil que herede de Vehiculo y agregue un atributo adicional color.
Sobrescribe el método __str__() para que al imprimir un objeto de tipo
Automovil muestre la marca, el modelo y el color del automóvil.
'''

# SOLUCION PROFE


class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo


class Automovil(Vehiculo):
    def __init__(self, marca, modelo, color):
        super().__init__(marca, modelo)
        self.color = color

    def __str__(self):
        return f"Automóvil: {self.marca} {self.modelo}, Color: {self.color}"


automovil = Automovil("Toyota", "Corolla", "Rojo")
print(automovil)  # Imprime: Automóvil: Toyota Corolla, Color: Rojo