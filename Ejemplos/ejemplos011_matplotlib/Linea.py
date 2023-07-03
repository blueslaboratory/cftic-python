# Day 16 - 20/06/2023
# Libreria Matplotlib.docx
# pip install matplotlib

import matplotlib.pyplot as plt 

# Datos
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10] 

# Crear el gráfico de línea
plt.plot(x, y) 

# Personalizar el gráfico
plt.title('Gráfico de línea')
plt.xlabel('Eje X')
plt.ylabel('Eje Y') 

# Salvar imagen en un fichero
# Tiene que estar antes de mostrar grafico, sino no funciona
# La ruta parte de raiz
plt.savefig('./Ejemplos/ejemplos011_matplotlib/images/linea.png')

# Mostrar el gráfico
plt.show()