# Day 17 - 21/06/2023
# Ejercicios Libreria Matplotlib.docx
# pip install matplotlib

'''
Ejercicio 5
Dibuja un grafico de sectores que muestre la proporcion de ventas de 
diferentes productos. El usuario debe ingresar los datos de ventas para 
cada producto.
'''

import matplotlib.pyplot as plt 

# Datos
productos = []
ventas = []

n = int(input('Numero de productos: '))

# Insertar los productos
for i in range(n):
    p = input(f'{i}. - Nombre producto: ')
    v = int(input(f'{i}. - Ventas: '))
    
    productos.append(p)
    ventas.append(v)


# Crear el grafico de torta
plt.pie(ventas, labels=productos) 

# Personalizar el grafico
plt.title('Pie Chart') 


# Salvar imagen en un fichero
# Tiene que estar antes de mostrar grafico, sino no funciona
# La ruta parte de raiz
plt.savefig('./015 Matplotlib/images/Ej005_Pie.png')

# Mostrar el grafico
plt.show()