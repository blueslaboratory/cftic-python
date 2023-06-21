# Day 17 - 21/06/2023
# Ejercicios Libreria Matplotlib.docx
# pip install matplotlib

'''
Ejercicio 6
Dibuja un grafico de lineas que muestre la evolucion de las temperaturas 
a lo largo de varios días. El usuario debe ingresar los datos de temperatura 
para cada día.
'''

import matplotlib.pyplot as plt 

# Datos (listas: semana y vacia)
semana = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
temps_semanales = []

# Solicitar la cantidad de semanas al usuario
numSemanas = int(input('Cantidad de semanas: '))

# Insertar las temperaturas
for semanaX in range(numSemanas):
    temperaturas_semana = []
    
    print(f'\n*** Semana {semanaX+1} ***')
    
    for dia in semana:
        t = float(input(f'{dia} - Temperatura (ºC): '))
        temperaturas_semana.append(t)
        
    temps_semanales.append(temperaturas_semana)


# Crear el grafico de lineas
for index, temperaturas_semana in enumerate(temps_semanales):
    plt.plot(semana, temperaturas_semana, label=f'Semana {index + 1}')


# Personalizar el grafico
plt.title('Temperatura a lo largo de la semana')
plt.xlabel('Dia de la semana')
plt.ylabel('Temperatura (ºC)')
plt.legend()

# Salvar imagen en un fichero
# Tiene que estar antes de mostrar grafico, sino no funciona
# La ruta parte de raiz
plt.savefig('./015 Matplotlib/images/Ej006_Linea.png')

# Mostrar el grafico
plt.show()