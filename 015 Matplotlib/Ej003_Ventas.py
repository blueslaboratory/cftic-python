# Day 17 - 21/06/2023
# Ejercicios Libreria Matplotlib.docx
# pip install matplotlib

'''
Ejercicio 3
Dibuja un diagrama de barras que muestre la cantidad de ventas por mes 
para un año determinado. El usuario debe ingresar los datos de ventas para 
cada mes.
'''

import matplotlib.pyplot as plt 

# Datos
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio']
ventas = []

# Insertar las ventas
for mes in meses:
    venta = float(input(f'Ventas {mes}: '))
    ventas.append(venta)


# Crear el grafico de barras
plt.bar(meses, ventas)

# Personalizar el grafico
plt.title(f'Ventas de {meses[0]} - {meses[len(meses)-1]}')
plt.xlabel('Meses')
plt.ylabel('Ventas') 

# Salvar imagen en un fichero
# Tiene que estar antes de mostrar grafico, sino no funciona
# La ruta parte de raiz
plt.savefig('./015 Matplotlib/images/Ej003_Barras.png')

# Mostrar el grafico
plt.show()