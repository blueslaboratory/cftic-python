# Day 20 - 26/06/2023
# Ejercicios Herencia.docx

'''
Ejercicio 10
Crear una clase Persona con atributos nombre y edad. Luego, crear una clase
Estudiante que herede de Persona y agregue un atributo adicional curso.
Sobrescribe el método __str__() para que al imprimir un objeto de tipo
Estudiante muestre el nombre, la edad y el curso del estudiante.
'''

# SOLUCION PROFE


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


class Estudiante(Persona):
    def __init__(self, nombre, edad, curso):
        super().__init__(nombre, edad)
        self.curso = curso

    def __str__(self):
        return f"Estudiante: {self.nombre}, Edad: {self.edad}, Curso: {self.curso}"


estudiante = Estudiante("Juan", 20, "12° grado")
print(estudiante)  # Imprime: Estudiante: Juan, Edad: 20, Curso: 12° grado