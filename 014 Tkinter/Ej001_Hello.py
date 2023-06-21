# Day 17 - 21/06/2023
# Ejercicios Libreria tkinter.docx


'''
Ejercicio 1
Crea una ventana con un botón que imprima "¡Hola, mundo!" en 
la consola cuando se haga clic en él.
'''

import tkinter as tk
 
def mostrar_mensaje():
    print('¡Hello World!')

# Ventana 
ventana = tk.Tk()
ventana.title('Ejercicio 1 - Hello')

# Size
ventana.geometry('240x100')

# Boton
boton = tk.Button(ventana, text='print en consola', command=mostrar_mensaje)
# Centrando el boton
boton.pack(pady=30, padx=50, anchor='center')


'''
Esta linea inicia el bucle principal de la ventana, que espera a que ocurran 
eventos (como hacer clic en el botón) y responde a ellos. 
El programa seguira ejecutandose en este bucle hasta que se cierre la ventana.
'''
ventana.mainloop()