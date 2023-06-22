# Day 17 - 21/06/2023
# Ejercicios Libreria tkinter.docx


'''
Ejercicio 3
Crea una ventana con una entrada de texto y un boton. Al hacer clic 
en el boton, muestra el texto ingresado en la entrada en una etiqueta.
'''

import tkinter as tk


def mostrarMensaje():
    label['text'] = entry.get()

root = tk.Tk()

# Cuadro
entry = tk.Entry(root)
entry.pack()

# Boton
boton = tk.Button(root, text='Mostrar texto', command=mostrarMensaje)
boton.pack()

# Label
label = tk.Label(root, text='')
label.pack()

'''
Esta linea inicia el bucle principal de la ventana, que espera a que ocurran 
eventos (como hacer clic en el botón) y responde a ellos. 
El programa seguira ejecutandose en este bucle hasta que se cierre la ventana.
'''
root.mainloop()