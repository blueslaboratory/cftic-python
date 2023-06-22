# Day 17 - 21/06/2023
# Ejercicios Libreria Matplotlib.docx
# pip install matplotlib

'''
Ejercicio 1
Escribe un programa que cree un grafico de barras para mostrar las 
ventas mensuales de una tienda. El programa debe utilizar los siguientes datos:
meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May']
ventas = [120, 85, 95, 150, 110]
'''

import matplotlib.pyplot as plt 

# Datos
meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May']
ventas = [120, 85, 95, 150, 110]

# Crear el grafico de barras
plt.bar(meses, ventas)

# Personalizar el grafico
plt.title(f'Ventas de {meses[0]} - {meses[len(meses)-1]}')
# plt.title(f'Ventas de {meses[0]} - {meses[len(meses)-1]}', loc='left')
plt.xlabel('Meses')
plt.ylabel('Ventas') 

# Salvar imagen en un fichero
# Tiene que estar antes de mostrar grafico, sino no funciona
# La ruta parte de raiz
plt.savefig('./015 Matplotlib/images/Ej001_Barras.png')

# Mostrar el grafico
plt.show()