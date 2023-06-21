# Day 17 - 21/06/2023
# Ejercicios Libreria Matplotlib.docx
# pip install matplotlib

'''
Ejercicio 2
Escribe un programa que cree un grafico de dispersion para mostrar la 
relacion entre la temperatura y la humedad en diferentes momentos del dia. 
Utiliza los siguientes datos:
temperatura = [20, 25, 30, 35, 40]
humedad = [40, 35, 30, 25, 20]
'''

import matplotlib.pyplot as plt 

# Datos
temperatura = [20, 25, 30, 35, 40]
humedad = [40, 35, 30, 25, 20]

# Crear el grafico de barras
plt.scatter(temperatura, humedad)

# Personalizar el grafico
plt.title('Temperatura (x) vs Humedad (y)')
plt.xlabel('Temperatura')
plt.ylabel('Humedad')

# Salvar imagen en un fichero
# Tiene que estar antes de mostrar grafico, sino no funciona
# La ruta parte de raiz
plt.savefig('./015 Matplotlib/images/Ej002_Dispersion.png')

# Mostrar el grafico
plt.show()