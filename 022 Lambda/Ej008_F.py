# Day 24 - 30/06/2023
# Ejercicios Lambda


# Nivel intermedio
'''
Ejercicio 8
Escribe una función lambda que reciba una lista de diccionarios como parámetro,
donde cada diccionario representa un estudiante con las claves 'nombre' y
'promedio', y devuelva una lista con los nombres de los estudiantes cuyo
promedio sea mayor a 80.
'''

estudiantes = [
    {"nombre": "Juan", "promedio": 75},
    {"nombre": "Maria", "promedio": 85},
    {"nombre": "Pedro", "promedio": 90},
    {"nombre": "Ana", "promedio": 78},
]



# Comprimida
lambda estudiantes: list(map(lambda estudiante: estudiante['nombre'], filter(lambda estudiante: estudiante['promedio'] > 80, estudiantes)))
promedioSuperior = lambda estudiantes: list(map(lambda estudiante: estudiante['nombre'], filter(lambda estudiante: estudiante['promedio'] > 80, estudiantes)))



# Expandida:
# Filtrar los estudiantes con un promedio mayor a 80
estudiantes_filtrados = filter(lambda estudiante: estudiante['promedio'] > 80, estudiantes)

# Obtener solo los nombres de los estudiantes filtrados
nombres_estudiantes = map(lambda estudiante: estudiante['nombre'], estudiantes_filtrados)

# Convertir el objeto map en una lista
resultado = list(nombres_estudiantes)



print(promedioSuperior(estudiantes))
print(resultado)