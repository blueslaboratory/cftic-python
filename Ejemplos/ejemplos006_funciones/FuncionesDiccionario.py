# Day 11 - 13/06/2023

def imprimir_ficha(**datos_persona):
    print(type(datos_persona))
    for clave_ficha in datos_persona:
        print(clave_ficha,'->', datos_persona[clave_ficha])


print('Inicio programa')
ficha_persona={'nombre':'Pepe','apellido':'Perez Mesa','edad':35}

print('\nImprimir ficha persona imprimir_ficha(**ficha_persona):')
imprimir_ficha(**ficha_persona)

print('\nImprimir ficha persona pasando un diccionario a pelo:')
imprimir_ficha(nombre='Manolo',apellido='Perez Mesa',edad=35, dni='5534354H')