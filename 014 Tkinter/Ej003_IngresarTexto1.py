# Day 17 - 21/06/2023
# Ejercicios Libreria tkinter.docx


'''
Ejercicio 3
Crea una ventana con una entrada de texto y un boton. Al hacer clic 
en el boton, muestra el texto ingresado en la entrada en una etiqueta.
'''

import tkinter as tk


def mostrar_texto():
    texto = cuadro.get()
    etiqueta1.config(text=texto)


# Ventana
ventana = tk.Tk()
ventana.title('Ejercicio 3 - Ingresar Texto')

# Size
ventana.geometry('270x100')

# Etiqueta 0
etiqueta0 = tk.Label(ventana, text='Ingresa un texto:')
etiqueta0.pack()

# Cuadro
cuadro = tk.Entry(ventana)
cuadro.pack()

# Boton
boton = tk.Button(ventana, text='Mostrar texto', command=mostrar_texto)
boton.pack()

# Etiqueta 1
etiqueta1 = tk.Label(ventana, text='*** mi texto ***')
etiqueta1.pack()


'''
Esta linea inicia el bucle principal de la ventana, que espera a que ocurran 
eventos (como hacer clic en el botón) y responde a ellos. 
El programa seguira ejecutandose en este bucle hasta que se cierre la ventana.
'''
ventana.mainloop()