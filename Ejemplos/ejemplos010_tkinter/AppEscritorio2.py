# Day 16 - 20/06/2023
# Libreria tkinter.docx

# importando un modulo (tkinter)
import tkinter as tk
# importando un submodulo (ttk) de tkinter
from tkinter import ttk

 
def mostrar_opcion():
    opcion = combo.get()
    etiqueta.config(text="Opción seleccionada: " + opcion) 

# ventana
ventana = tk.Tk()
ventana.title("Ejemplo de funcionalidad")

# etiqueta
etiqueta = tk.Label(ventana, text="Selecciona una opción:")
etiqueta.pack()

# opciones 
opciones = ["Opción 1", "Opción 2", "Opción 3"]
combo = ttk.Combobox(ventana, values=opciones)
combo.pack()

# boton 
boton = tk.Button(ventana, text="Mostrar opción", command=mostrar_opcion)
boton.pack()


'''
Esta linea inicia el bucle principal de la ventana, que espera a que ocurran 
eventos (como hacer clic en el botón) y responde a ellos. 
El programa seguira ejecutandose en este bucle hasta que se cierre la ventana.
'''
ventana.mainloop()