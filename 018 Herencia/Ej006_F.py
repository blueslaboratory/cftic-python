# Day 20 - 26/06/2023
# Ejercicios Herencia.docx

'''
Ejercicio 6
Crear una clase Persona con atributos nombre y edad. Luego, crear una clase
Empleado que herede de Persona y tenga un atributo adicional salario.
Agrega métodos para obtener y establecer el salario del empleado.
'''

# SOLUCION PROFE

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.salario = salario

    def obtener_salario(self):
        return self.salario

    def establecer_salario(self, nuevo_salario):
        self.salario = nuevo_salario


empleado = Empleado("Juan", 30, 5000)
print(empleado.obtener_salario())  # Imprime: 5000

empleado.establecer_salario(6000)
print(empleado.obtener_salario())  # Imprime: 6000