# Day 17 - 21/06/2023
# Ejercicios Libreria tkinter.docx


'''
Ejercicio 5
Crea una ventana con tres botones, uno para cambiar el color de fondo 
a rojo, otro a verde y otro a azul.
'''

import tkinter as tk
from functools import partial


def cambiarColor(color):
    # Opcion 1:
    ventana.config(bg=color)
    # Opcion 2:
    # ventana['bg']=color


# Ventana
ventana = tk.Tk()
ventana.title('Ejercicio 5 - Colores')

# Size
ventana.geometry('240x100')

# Botones con lambda
botonRed = tk.Button(ventana, text='RED', command=lambda:cambiarColor('red')) #FF0000
botonRed.grid(row=0, column=0, padx=10, pady=10)

botonRed = tk.Button(ventana, text='GREEN', command=lambda:cambiarColor('#00FF00')) #green
botonRed.grid(row=0, column=1, padx=10, pady=10)

# Botones con partial
botonRed = tk.Button(ventana, text='BLUE', command=partial(cambiarColor,'blue')) #0000FF
botonRed.grid(row=0, column=2, padx=10, pady=10)

botonRed = tk.Button(ventana, text='PINK', command=partial(cambiarColor,'pink'))
botonRed.grid(row=0, column=3, padx=10, pady=10)


'''
Esta linea inicia el bucle principal de la ventana, que espera a que ocurran 
eventos (como hacer clic en el botón) y responde a ellos. 
El programa seguira ejecutandose en este bucle hasta que se cierre la ventana.
'''
ventana.mainloop()