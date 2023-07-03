# Day 16 - 20/06/2023
# Libreria Matplotlib.docx
# pip install matplotlib

import matplotlib.pyplot as plt 

# Datos
etiquetas = ['Manzanas', 'Naranjas', 'Plátanos', 'Fresas']
valores = [30, 25, 20, 15]

# Crear el gráfico de torta
plt.pie(valores, labels=etiquetas) 

# Personalizar el gráfico
plt.title('Gráfico de torta') 

# Salvar imagen en un fichero
# Tiene que estar antes de mostrar grafico, sino no funciona
# La ruta parte de raiz
plt.savefig('./Ejemplos/ejemplos011_matplotlib/images/pie.png')

# Mostrar el gráfico
plt.show()