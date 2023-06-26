# Day 20 - 26/06/2023
# Ejercicios Herencia.docx

'''
Ejercicio 7
Crear una clase Animal con un método hacer_sonido() que imprima
"Sonido del animal". Luego, crear una clase Perro que herede de Animal y
sobrescriba el método hacer_sonido() para imprimir "Guau guau".
Agrega una clase adicional Gato que también herede de Animal y sobrescriba
el método hacer_sonido() para imprimir "Miau".
'''

# SOLUCION PROFE


class Animal:
    def hacer_sonido(self):
        print("Sonido del animal")


class Perro(Animal):
    def hacer_sonido(self):
        print("Guau guau")


class Gato(Animal):
    def hacer_sonido(self):
        print("Miau")


perro = Perro()
perro.hacer_sonido()  # Imprime: Guau guau

gato = Gato()
gato.hacer_sonido()  # Imprime: Miau
