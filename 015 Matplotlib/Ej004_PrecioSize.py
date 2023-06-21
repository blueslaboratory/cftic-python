# Day 17 - 21/06/2023
# Ejercicios Libreria Matplotlib.docx
# pip install matplotlib

'''
Ejercicio 4
Dibuja un gráfico de dispersión que muestre la relación entre el precio y 
el tamaño de una serie de productos. El usuario debe ingresar los datos de 
precio y tamaño para cada producto.
'''

import matplotlib.pyplot as plt 

# Datos
precios = []
sizes = []

n = int(input('Numero de productos: '))

# Insertar los precios y sizes
for i in range(n):
    p = float(input(f'{i}. - Precio Producto (€): '))
    s = float(input(f'{i}. - Size (cm^2): '))
    
    precios.append(p)
    sizes.append(s)


# Crear el grafico de dispersion
plt.scatter(precios, sizes)

# Personalizar el grafico
plt.title('Relacion precio (€) vs size (cm^2)')
plt.xlabel('Precio (€)')
plt.ylabel('Size (cm^2)') 

# Salvar imagen en un fichero
# Tiene que estar antes de mostrar grafico, sino no funciona
# La ruta parte de raiz
plt.savefig('./015 Matplotlib/images/Ej004_Dispersion.png')

# Mostrar el grafico
plt.show()