# Day 18 - 22/06/2023
# Ejercicios Libreria tkinter.docx


'''
Ejercicio 2
Crea una ventana con dos botones, uno para incrementar y otro para 
decrementar un contador. Muestra el valor del contador en una etiqueta.
'''

import tkinter as tk


def incrementar():
    label['text'] += 1
    
def decrementar():
    label['text'] -= 1
    

valor = 0
root = tk.Tk()

# Label
label = tk.Label(root, text=valor)
label.pack()

# Botones
bt_inc = tk.Button(root, text='+', command=incrementar)
bt_inc.pack()

bt_dec = tk.Button(root, text='-', command=decrementar)
bt_dec.pack()


'''
Esta linea inicia el bucle principal de la ventana, que espera a que ocurran 
eventos (como hacer clic en el boton) y responde a ellos. 
El programa seguira ejecutandose en este bucle hasta que se cierre la ventana.
'''
root.mainloop()