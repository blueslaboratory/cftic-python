# Day 23 - 29/06/2023

'''
4.Libreria Matplotlib

Quieres crear un gráfico de líneas que muestre la evolución de las ventas mensuales
de una tienda durante un año. Tienes los datos de las ventas mensuales en una
lista llamada ventas_mensuales, donde cada elemento representa las ventas de un mes
específico. Quieres utilizar la biblioteca Matplotlib para crear el gráfico de
líneas.

Implementa el código necesario para generar el gráfico de líneas siguiendo las
siguientes especificaciones:

* El eje x del gráfico debe representar los meses del año (por ejemplo, enero,
febrero, etc.).
* El eje y del gráfico debe representar las ventas mensuales.
* El gráfico debe tener una línea que conecte los puntos de las ventas mensuales.
* El gráfico debe tener un título descriptivo.
* Los ejes x e y deben tener etiquetas descriptivas.
'''

import matplotlib.pyplot as plt

# Datos
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
         'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
ventas_mensuales = [15000, 18000, 22000, 25000, 28000, 32000,
                    35000, 38000, 41000, 35000, 30000, 20000]


# Crear el grafico de barras
plt.plot(meses, ventas_mensuales, marker='o', color='b')

# Personalizar el grafico
plt.title(f'Ventas de {meses[0]} - {meses[len(meses)-1]}')
plt.xlabel('Meses')
plt.xticks(rotation=45)
plt.ylabel('Ventas Mensuales')

# Guardar el grafico como imagen en formato PNG
plt.savefig('images/Ej004_Matplotlib.png')

# Mostrar el grafico
plt.show()