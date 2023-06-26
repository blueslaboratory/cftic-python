# Day 20 - 26/06/2023
# Ejercicios Herencia.docx

'''
Ejercicio 4
Crear una clase Persona con atributos nombre y edad. Luego, crear una clase
Estudiante que herede de Persona y tenga un atributo adicional grado.
Sobrescribir el método __init__() de Estudiante para aceptar el nombre,
la edad y el grado al crear un objeto de tipo Estudiante.
'''

# SOLUCION PROFE

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado


estudiante = Estudiante("Juan", 18, "10° grado")
print(estudiante.nombre)
print(estudiante.edad)
print(estudiante.grado)
