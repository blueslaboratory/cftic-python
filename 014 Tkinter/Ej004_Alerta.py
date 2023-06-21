# Day 17 - 21/06/2023
# Ejercicios Libreria tkinter.docx


'''
Ejercicio 4
Crea una ventana con un campo de entrada y un boton. Al hacer clic en 
el boton, muestra un mensaje de alerta con el texto ingresado en la 
entrada.
'''

import tkinter as tk
from tkinter import messagebox


def mostrar_warning():
    texto = cuadro.get()
    messagebox.showwarning('OMG a wArNiNg', texto)


# Ventana
ventana = tk.Tk()
ventana.title('Ejercicio 4 - Mensaje de Alerta')

# Size
ventana.geometry('270x100')

# Etiqueta 0
etiqueta0 = tk.Label(ventana, text='Ingresa un texto:')
etiqueta0.pack()

# Cuadro
cuadro = tk.Entry(ventana)
cuadro.pack()

# Boton
boton = tk.Button(ventana, text='Warning!', command=mostrar_warning)
boton.pack()

'''
Esta linea inicia el bucle principal de la ventana, que espera a que ocurran 
eventos (como hacer clic en el botón) y responde a ellos. 
El programa seguira ejecutandose en este bucle hasta que se cierre la ventana.
'''
ventana.mainloop()