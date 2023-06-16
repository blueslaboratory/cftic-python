# Day 14 - 16/06/2023
# Ejercicios Mix

def tratar_datos(datos_iniciales):
    datos_finales = []
    for dato in datos_iniciales:
        campos=dato.split(';')
        campos[2]=0 if campos[2]=='Masculino' else 1
        campos[3] = campos[3].upper()
        datos_finales.append(tuple(campos))
    return datos_finales

datos_iniciales=['Juan Pérez;30;Masculino;Ingeniero', 'María García;25;Femenino;Doctora', 'Pedro Rodríguez;40;Masculino;Abogado', 'Ana López;35;Femenino;Profesora']
print(datos_iniciales)

datos_finales=tratar_datos(datos_iniciales)
print(datos_finales)