# Day 17 - 21/06/2023
# Ejercicios Libreria tkinter.docx


'''
Ejercicio 4
Crea una root con un campo de entrada y un boton. Al hacer clic en 
el boton, muestra un mensaje de alerta con el texto ingresado en la 
entrada.
'''

import tkinter as tk
from tkinter import messagebox


def mostrar_warning():
    texto = cuadro.get()
    messagebox.showwarning('OMG a wArNiNg', texto)


# root
root = tk.Tk()

# Etiqueta 0
etiqueta = tk.Label(root, text='Ingresa un texto:')
etiqueta.pack()

# Cuadro
cuadro = tk.Entry(root)
cuadro.pack()

# Boton
diccionario = {'command':mostrar_warning, 'text':'Mostrar Alerta', 'activeforeground':'#09fa00'}
boton = tk.Button(**diccionario)
boton.pack()

'''
Esta linea inicia el bucle principal de la root, que espera a que ocurran 
eventos (como hacer clic en el botón) y responde a ellos. 
El programa seguira ejecutandose en este bucle hasta que se cierre la root.
'''
root.mainloop()