# Day 16 - 20/06/2023

from tkinter import *
from tkinter import ttk


# Funcion para manejar la opcion "Salir" del menu
def salir():
    ventanaPrincipal.destroy()


ventanaPrincipal = Tk()

# title
ventanaPrincipal.title('1º prueba de clase')

# size de la ventana
ventanaPrincipal.geometry('800x600')

# frame
frame = ttk.Frame(ventanaPrincipal, padding=10, border=1)

# grid
frame.grid(column=10, row=10)

# label
ttk.Label(frame, text='Hello World!').grid(column=3, row=0)

# boton
ttk.Button(frame, text='Salir', command=salir).grid(column=5, row=5)


'''
Esta linea inicia el bucle principal de la ventana, que espera a que ocurran 
eventos (como hacer clic en el botón) y responde a ellos. 
El programa seguira ejecutandose en este bucle hasta que se cierre la ventana.
'''
ventanaPrincipal.mainloop()