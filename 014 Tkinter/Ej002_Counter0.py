# Day 17 - 21/06/2023
# Ejercicios Libreria tkinter.docx


'''
Ejercicio 2
Crea una ventana con dos botones, uno para incrementar y otro para 
decrementar un contador. Muestra el valor del contador en una etiqueta.
'''

import tkinter as tk

# Variable global
counter = 0


def decrease():
    global counter
    counter -= 1
    updateEtiqueta(counter)
    

def increase():
    global counter
    counter += 1
    updateEtiqueta(counter)


def updateEtiqueta(counter):
    etiqueta.config(text=f'Counter: {counter}')


# Ventana 
ventana = tk.Tk()
ventana.title('Ejercicio 2 - Counter')

# Size
ventana.geometry('270x69')

# Boton
botonDecrease = tk.Button(ventana, text='Decrease', command=decrease)
botonDecrease.grid(row=0, column=0, padx=10, pady=10)
botonIncrease = tk.Button(ventana, text='Increase', command=increase)
botonIncrease.grid(row=0, column=2, padx=10, pady=10)

# Etiqueta
etiqueta = tk.Label(ventana, text=f'Counter: {counter}', font=('Calibri', 12))
etiqueta.grid(row=0, column=1, padx=10, pady=10)

'''
Esta linea inicia el bucle principal de la ventana, que espera a que ocurran 
eventos (como hacer clic en el boton) y responde a ellos. 
El programa seguira ejecutandose en este bucle hasta que se cierre la ventana.
'''
ventana.mainloop()