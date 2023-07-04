# Day 26 - 04/07/2023
# No hay .docx (Ejemplo basico de ChatGPT)


# Definicion de la clase base (superclase)
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print(f"{self.nombre} esta comiendo.")


# Definicion de la clase derivada (subclase)
class Perro(Animal):
    def __init__(self, nombre, raza):
        # Llamada al constructor de la clase base
        super().__init__(nombre)
        self.raza = raza

    def ladrar(self):
        print(f"{self.nombre} ({self.raza}) está ladrando.")


# Creación de una instancia de la clase derivada
mi_perro = Perro("Bobby", "Labrador")


# Acceso a los atributos y métodos de la clase base y derivada
print(mi_perro.nombre)  # Bobby
mi_perro.comer()  # Bobby está comiendo.
mi_perro.ladrar()  # Bobby (Labrador) está ladrando.
