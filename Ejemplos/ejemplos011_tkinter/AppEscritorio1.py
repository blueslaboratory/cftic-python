# Day 16 - 20/06/2023
# Libreria tkinter.docx


import tkinter as tk
 
def mostrar_texto():
    texto = cuadro.get()
    etiqueta.config(text=texto)

# Ventana
ventana = tk.Tk()
ventana.title("Ejemplo de funcionalidad")

# Etiqueta
etiqueta = tk.Label(ventana, text="Ingresa un texto:")
etiqueta.pack()

# Cuadro
cuadro = tk.Entry(ventana)
cuadro.pack()

# Boton
boton = tk.Button(ventana, text="Mostrar texto", command=mostrar_texto)
boton.pack()


'''
Esta linea inicia el bucle principal de la ventana, que espera a que ocurran 
eventos (como hacer clic en el botón) y responde a ellos. 
El programa seguira ejecutandose en este bucle hasta que se cierre la ventana.
'''
ventana.mainloop()