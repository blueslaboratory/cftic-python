# Day 16 - 20/06/2023
# pip install pandas

import pandas as pd
import matplotlib.pyplot as plt


datos = {'Nombre': ['Juan', 'María', 'Pedro', 'Ana'],
         'Edad': [25, 30, 35, 28],
         'Altura': [175, 165, 190, 170],
         'Ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Valencia']}

df = pd.DataFrame(datos) 


# Gráfico de barras
df['Edad'].plot(kind='bar')
plt.show()
 
# Gráfico de dispersión
df.plot(x='Edad', y='Altura', kind='scatter') 
plt.show()

# Gráfico de caja
df['Edad'].plot(kind='box')
plt.show()