# Day 16 - 20/06/2023
# Libreria tkinter.docx

import tkinter as tk
 
def mostrar_mensaje():
    etiqueta.config(text="¡Hola, Tkinter!")

# Ventana 
ventana = tk.Tk()
ventana.title("Ejemplo de funcionalidad")

# Etiqueta
etiqueta = tk.Label(ventana, text="Presiona el botón", font=('Arial', 24))
etiqueta.pack()

# Boton
boton = tk.Button(ventana, text="Mostrar mensaje", command=mostrar_mensaje)
boton.pack()


'''
Esta linea inicia el bucle principal de la ventana, que espera a que ocurran 
eventos (como hacer clic en el botón) y responde a ellos. 
El programa seguira ejecutandose en este bucle hasta que se cierre la ventana.
'''
ventana.mainloop()