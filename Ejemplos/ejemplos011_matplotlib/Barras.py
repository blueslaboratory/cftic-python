# Day 16 - 20/06/2023
# Libreria Matplotlib.docx
# pip install matplotlib

import matplotlib.pyplot as plt 

# Datos
x = ['A', 'B', 'C', 'D']
y = [10, 20, 15, 25]

# Crear el gráfico de barras
plt.bar(x, y)

# Personalizar el gráfico
plt.title('Gráfico de barras')
plt.xlabel('Categorías')
plt.ylabel('Valores') 

# Salvar imagen en un fichero
# Tiene que estar antes de mostrar grafico, sino no funciona
# La ruta parte de raiz
plt.savefig('./Ejemplos/ejemplos011_matplotlib/images/barras.png')

# Mostrar el gráfico
plt.show()